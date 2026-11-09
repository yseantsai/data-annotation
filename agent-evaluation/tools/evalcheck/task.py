"""The task folder as the checks read it.

One object that parses the folder once and hands every check the same view of
it. The layout, from the root README:

    tasks/NNN-name/
      inputs/                        the files as received          (source)
      outputs/<harness>/             result .md, output files, zip  (evidence)
      evaluation/converted/inputs/   Markdown of the inputs         (source)
      evaluation/converted/<harness>/  Markdown and renders of outputs (evidence)
      evaluation/rationale.md, confidence.md, ratings.md            (authored)
"""
import re
from pathlib import Path

from .common import read_text, markdown_headings

AUTHORED = "authored"
EVIDENCE = "evidence"
SOURCE = "source"

# The platform's five-point dimension scale, as its rating form shows it
# (captured 2026-11-05 from the Stage 2 form): Excellent means a strong
# professional would hand it in as-is on this dimension, Acceptable means it
# does the job with rough edges, Poor means it would be sent back.
SCALE = ("Poor", "Below par", "Acceptable", "Good", "Excellent")
DIMENSIONS = ("Instruction Following", "Correctness",
              "Professional Judgment", "Format & Presentation")
OVERALL = "Overall quality"


class Artifact(object):
    __slots__ = ("name", "path", "kind", "harness", "_text")

    def __init__(self, name, path, kind, harness=None):
        self.name = name
        self.path = path
        self.kind = kind
        self.harness = harness
        self._text = None

    @property
    def text(self):
        if self._text is None:
            try:
                self._text = read_text(self.path)
            except Exception:
                self._text = ""
        return self._text

    @property
    def headings(self):
        return markdown_headings(self.text)


_PREF_RE = re.compile(r"^\s*Preference:\s*(.+?)\s*$", re.I | re.M)
_ROW_RE = re.compile(r"^\|(.+)\|\s*$", re.M)


class Ratings(object):
    """evaluation/ratings.md, parsed. Absent file gives an empty, falsey object."""

    def __init__(self, path=None):
        self.path = path
        self.harnesses = []
        self.rows = {}           # dimension -> {harness: value}
        self.preference = None
        if path is not None and Path(path).is_file():
            self._parse(read_text(path))

    def __bool__(self):
        return bool(self.rows)

    __nonzero__ = __bool__

    def _parse(self, text):
        m = _PREF_RE.search(text)
        if m:
            self.preference = m.group(1).strip()
        for line in _ROW_RE.findall(text):
            cells = [c.strip() for c in line.split("|")]
            if not cells or set("".join(cells)) <= set("- :"):
                continue
            head = cells[0]
            if head.lower() in ("dimension", ""):
                self.harnesses = [c for c in cells[1:] if c]
                continue
            if not self.harnesses:
                continue
            self.rows[head] = dict(zip(self.harnesses, cells[1:]))

    def overall(self, harness):
        for name, row in self.rows.items():
            if name.lower().startswith(OVERALL.lower()):
                try:
                    return float(re.sub(r"[^0-9.]", "", row.get(harness, "")))
                except ValueError:
                    return None
        return None


class TaskContext(object):
    def __init__(self, folder):
        self.folder = Path(folder)
        self.name = self.folder.name
        self.artifacts = []
        self.harnesses = []
        self._load()
        self.ratings = Ratings(self.folder / "evaluation" / "ratings.md")

    # -- loading ---------------------------------------------------------
    def _add(self, path, kind, harness=None):
        rel = path.relative_to(self.folder).as_posix()
        self.artifacts.append(Artifact(rel, path, kind, harness))

    def _load(self):
        ev = self.folder / "evaluation"
        for name in ("rationale.md", "confidence.md", "ratings.md"):
            p = ev / name
            if p.is_file():
                self._add(p, AUTHORED)
        pr = self.folder / "prompt.md"
        if pr.is_file():
            self._add(pr, SOURCE)
        conv = ev / "converted"
        for d in (self.folder / "inputs", conv / "inputs"):
            for p in self._readable(d):
                self._add(p, SOURCE)
        out = self.folder / "outputs"
        for hd in sorted(out.iterdir()) if out.is_dir() else []:
            if not hd.is_dir() or hd.name.startswith("."):
                continue
            for p in self._readable(hd) + self._readable(conv / hd.name):
                self._add(p, EVIDENCE, hd.name)
            # A harness counts as run once anything at all sits in its
            # folder, a result file or a zip. An empty outputs/<harness>/ is
            # a folder waiting for a run, and E70 must not demand ratings
            # for a result that does not exist yet.
            if any(p.is_file() and not p.name.startswith(".") for p in hd.iterdir()):
                self.harnesses.append(hd.name)

    @staticmethod
    def _readable(d):
        """The .md and .docx files directly inside `d`, or none."""
        if not d.is_dir():
            return []
        return [p for p in sorted(d.glob("*"))
                if p.is_file() and p.suffix.lower() in (".md", ".docx")
                and not p.name.startswith(".")]

    # -- views the checks use --------------------------------------------
    def of_kind(self, kind):
        return [a for a in self.artifacts if a.kind == kind]

    def authored(self, basename=None):
        got = self.of_kind(AUTHORED)
        if basename:
            got = [a for a in got if Path(a.name).name == basename]
        return got

    def one(self, basename):
        got = self.authored(basename)
        return got[0] if got else None

    def evidence_of(self, harness):
        return [a for a in self.artifacts if a.kind == EVIDENCE and a.harness == harness]

    @property
    def prompt(self):
        p = self.folder / "prompt.md"
        return read_text(p) if p.is_file() else None

    def source_text(self):
        return "\n".join(a.text for a in self.of_kind(SOURCE))

    def harness_text(self, harness):
        return "\n".join(a.text for a in self.evidence_of(harness))


def find_tasks(root):
    """Every tasks/NNN-* folder under `root`, or `root` itself if it is one."""
    root = Path(root)
    if (root / "evaluation").is_dir() or (root / "outputs").is_dir():
        return [root]
    tasks = root / "tasks"
    base = tasks if tasks.is_dir() else root
    return [p for p in sorted(base.iterdir())
            if p.is_dir() and re.match(r"^\d+-", p.name)]
