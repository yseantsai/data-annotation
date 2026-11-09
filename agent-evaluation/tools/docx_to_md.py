#!/usr/bin/env python3
"""Convert a .docx deliverable to readable Markdown, in document order.

    .venv/bin/python tools/docx_to_md.py <in.docx> [--out <file.md>]
    .venv/bin/python tools/docx_to_md.py tasks/NNN-name/outputs/<harness>

Headings keep their level, list paragraphs become bullets (nested by indent
level), tables become pipe tables where they sit, and bold runs stay bold. With
a task's inputs/ or outputs/<harness> folder, every .docx in it is written to
evaluation/converted/<inputs|harness>/ (or --out).

The conversion is for reading, grepping and the prose checks. It drops page
layout entirely: judge length and pagination from tools/render.py output.
"""
import argparse
import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph


def _runs(p):
    out = []
    for r in p.runs:
        t = r.text
        if not t:
            continue
        if r.bold and t.strip():
            lead = t[:len(t) - len(t.lstrip())]
            trail = t[len(t.rstrip()):]
            t = "%s**%s**%s" % (lead, t.strip(), trail)
        out.append(t)
    return "".join(out).strip()


def _list_level(p):
    ppr = p._p.pPr
    if ppr is not None and ppr.numPr is not None:
        ilvl = ppr.numPr.find(qn("w:ilvl"))
        return int(ilvl.get(qn("w:val"))) if ilvl is not None else 0
    if p.style is not None and p.style.name.lower().startswith("list"):
        return 0
    return None


def _para(p):
    text = _runs(p)
    if not text:
        return ""
    style = (p.style.name if p.style is not None else "").lower()
    if style == "title":
        return "# " + text.replace("**", "")
    if style.startswith("heading"):
        try:
            lvl = int(style.split()[-1])
        except ValueError:
            lvl = 1
        return "#" * min(lvl + 1, 6) + " " + text.replace("**", "")
    lvl = _list_level(p)
    if lvl is not None:
        return "  " * lvl + "- " + text
    return text


def _table(t):
    rows = []
    for r in t.rows:
        cells = []
        for c in r.cells:
            cells.append(" ".join(_runs(p) for p in c.paragraphs if _runs(p)).replace("|", "/"))
        rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out)


def convert(src):
    doc = Document(str(src))
    blocks = ["# %s" % src.stem, ""]
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            s = _para(Paragraph(child, doc))
        elif child.tag == qn("w:tbl"):
            s = _table(Table(child, doc))
        else:
            continue
        if s:
            blocks.append(s)
            blocks.append("")
    # headers and footers carry things like confidentiality labels and page text
    hf = []
    for sec in doc.sections:
        for part, label in ((sec.header, "Header"), (sec.footer, "Footer")):
            txt = " ".join(_runs(p) for p in part.paragraphs if _runs(p))
            if txt and (label, txt) not in hf:
                hf.append((label, txt))
    if hf:
        blocks.append("## Headers and footers")
        blocks.append("")
        for label, txt in hf:
            blocks.append("- %s: %s" % (label, txt))
        blocks.append("")
    return "\n".join(blocks).rstrip() + "\n"


def converted_dir(folder):
    """Where conversions of a task folder go: tasks/X/inputs and
    tasks/X/outputs/<h> both map to tasks/X/evaluation/converted/<name>."""
    folder = Path(folder).resolve()
    if folder.name == "inputs":
        task, name = folder.parent, "inputs"
    elif folder.parent.name == "outputs":
        task, name = folder.parent.parent, folder.name
    else:
        return folder / "converted"
    return task / "evaluation" / "converted" / name


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target")
    ap.add_argument("--out")
    a = ap.parse_args()
    t = Path(a.target)
    if t.is_dir():
        srcs = sorted(t.glob("*.docx"))
        if not srcs:
            sys.exit("no .docx in %s" % t)
        out = Path(a.out) if a.out else converted_dir(t)
        out.mkdir(parents=True, exist_ok=True)
        for s in srcs:
            dest = out / (s.stem + ".md")
            dest.write_text(convert(s), encoding="utf-8")
            print("%s -> %s" % (s.name, dest))
    else:
        md = convert(t)
        if a.out:
            Path(a.out).write_text(md, encoding="utf-8")
            print("%s -> %s" % (t.name, a.out))
        else:
            sys.stdout.write(md)


if __name__ == "__main__":
    main()
