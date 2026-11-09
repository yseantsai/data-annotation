#!/usr/bin/env python3
"""task_status.py: resolve a task by sequence number and report where it stands.

    python3 tools/task_status.py NN          one task: folder, files, which sections are filled, log tail
    python3 tools/task_status.py --list      every task: seq, slug, prompt words, result present, rating
    python3 tools/task_status.py --next      the next unused sequence number
    python3 tools/task_status.py NN --json   the same as machine-readable JSON

Run from the project folder (finance-investing-prompt/) or anywhere: the project root is the
parent of this file's folder. A task is drafts/NN-slug/ holding prompt.md, result.md and task.md;
history/ inside the folder keeps earlier rounds (prompt-r1.md, result-r1.md).

Exit status: 0 found; 2 no task with that number or an ambiguous number; 3 bad usage.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "drafts"
SECTIONS = ["Prompt", "Failure target", "Design notes", "Self-check", "Generate response", "Outcome",
            "Rating", "Explanation", "Optional comments", "Log"]


def words(path):
    try:
        return len(path.read_text(encoding="utf-8", errors="ignore").split())
    except OSError:
        return 0


def sections(task_md):
    """{section: filled?} for task.md, ignoring HTML comments."""
    text = task_md.read_text(encoding="utf-8", errors="ignore") if task_md.is_file() else ""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    out = {}
    for name in SECTIONS:
        m = re.search(rf"^## {re.escape(name)}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        body = m.group(1).strip() if m else ""
        out[name] = bool(body)
    return out


def rating_of(task_md):
    text = task_md.read_text(encoding="utf-8", errors="ignore") if task_md.is_file() else ""
    m = re.search(r"^## Rating\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return ""
    body = re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S).strip()
    return body.split("\n")[0][:80] if body else ""


def log_tail(task_md, n=3):
    text = task_md.read_text(encoding="utf-8", errors="ignore") if task_md.is_file() else ""
    m = re.search(r"^## Log\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    lines = [l.strip() for l in (m.group(1) if m else "").splitlines() if l.strip().startswith("-")]
    return lines[-n:]


def task_dirs():
    if not DRAFTS.is_dir():
        return []
    return sorted(p for p in DRAFTS.iterdir() if p.is_dir() and re.match(r"^\d+-", p.name))


def describe(folder):
    m = re.match(r"^(\d+)-(.*)$", folder.name)
    seq = int(m.group(1))
    task_md = folder / "task.md"
    history = sorted(p.name for p in (folder / "history").iterdir()) if (folder / "history").is_dir() else []
    rounds = 1 + len([h for h in history if h.startswith("prompt-r")])
    return {
        "seq": f"{seq:02d}", "slug": m.group(2),
        "folder": str(folder.relative_to(ROOT)),
        "files": {name: (folder / name).is_file() for name in ("prompt.md", "result.md", "task.md")},
        "prompt_words": words(folder / "prompt.md"),
        "prompt_chars": len((folder / "prompt.md").read_text(encoding="utf-8", errors="ignore")) if (folder / "prompt.md").is_file() else 0,
        "result_words": words(folder / "result.md"),
        "sections": sections(task_md),
        "rating": rating_of(task_md),
        "round": rounds,
        "history": history,
        "log_tail": log_tail(task_md),
    }


def next_seq():
    seqs = [int(re.match(r"^(\d+)-", p.name).group(1)) for p in task_dirs()]
    return f"{(max(seqs) + 1) if seqs else 1:02d}"


def print_one(d):
    print(f"== task {d['seq']} {d['slug']}  ({d['folder']})  round {d['round']}")
    files = ", ".join(f"{k}{'' if v else ' (missing)'}" for k, v in d["files"].items())
    print(f"   files: {files}")
    print(f"   prompt: {d['prompt_words']} words, {d['prompt_chars']} characters;  result: "
          f"{d['result_words'] or 'empty'}{' words' if d['result_words'] else ''}")
    filled = [k for k, v in d["sections"].items() if v]
    empty = [k for k, v in d["sections"].items() if not v]
    print(f"   filled sections: {', '.join(filled) or 'none'}")
    print(f"   empty sections:  {', '.join(empty) or 'none'}")
    if d["rating"]:
        print(f"   rating line: {d['rating']}")
    if d["history"]:
        print(f"   history: {', '.join(d['history'])}")
    for l in d["log_tail"]:
        print(f"   log: {l}")


def main(argv):
    args = [a for a in argv[1:] if a != "--json"]
    as_json = "--json" in argv
    if not args:
        print(__doc__)
        return 3
    if args[0] == "--next":
        print(json.dumps({"next": next_seq()}) if as_json else next_seq())
        return 0
    if args[0] == "--list":
        rows = [describe(p) for p in task_dirs()]
        if as_json:
            print(json.dumps(rows, indent=2))
        else:
            print(f"{'seq':<4} {'slug':<36} {'prompt':>7} {'result':>7} {'round':>5}  rating")
            for d in rows:
                print(f"{d['seq']:<4} {d['slug'][:36]:<36} {d['prompt_words']:>7} "
                      f"{(d['result_words'] or '-'):>7} {d['round']:>5}  {d['rating']}")
            print(f"next: {next_seq()}")
        return 0
    m = re.match(r"^(\d+)$", args[0])
    if not m:
        print(f"expected a sequence number, got '{args[0]}'")
        return 3
    seq = int(m.group(1))
    hits = [p for p in task_dirs() if int(re.match(r"^(\d+)-", p.name).group(1)) == seq]
    if len(hits) != 1:
        msg = f"{'no task' if not hits else 'several tasks'} with sequence {seq:02d}; have: " + \
              ", ".join(p.name for p in task_dirs())
        print(json.dumps({"error": msg}) if as_json else msg)
        return 2
    d = describe(hits[0])
    print(json.dumps(d, indent=2) if as_json else "", end="")
    if not as_json:
        print_one(d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
