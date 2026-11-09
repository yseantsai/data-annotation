# Tooling

Two layers. The checks (`evalcheck.py`, `selftest.py`) are stdlib Python 3 and
run on the system interpreter. The document tools need the project venv and
LibreOffice.

## Environment

Installed 2026-11-05. To recreate on another machine:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt     # pypdf, python-docx, openpyxl, pypdfium2, pillow
```

LibreOffice 26.8.2 (arm64) lives at `~/Applications/LibreOffice.app`, installed
from the official DMG with its SHA-256 verified. No Homebrew, no sudo. Rendering
uses it headless with a throwaway profile, so an open LibreOffice window does
not block it.

| Tool | Needs | Does |
| --- | --- | --- |
| `pdf_to_md.py` | venv | PDF to Markdown, one `## Page N` section per page, plus filled form fields |
| `docx_to_md.py` | venv | DOCX to Markdown in document order: headings, nested bullets, tables in place, headers and footers |
| `render.py` | venv + LibreOffice | DOCX/XLSX/PPTX/PDF to PDF and `page-N.png`, for pagination and layout |

`render.py` was verified against task 001: it reproduces both existing renders
page for page, including the page-2 break. LibreOffice's layout can still differ
from Word's by a line at a page break, so open a borderline result in Word
before marking it down on length.

Point each tool at `inputs/` or at `outputs/<harness>/`; it reads the files
there and writes to `evaluation/converted/inputs/` or
`evaluation/converted/<harness>/`. The folders you fill are never written to.

```bash
.venv/bin/python tools/docx_to_md.py tasks/NNN-name/outputs/<harness>
.venv/bin/python tools/render.py     tasks/NNN-name/outputs/<harness>
.venv/bin/python tools/pdf_to_md.py  tasks/NNN-name/inputs/*.pdf --out tasks/NNN-name/evaluation/converted/inputs
```

## Checks

```bash
python3 tools/evalcheck.py                    # every tasks/NNN-* folder
python3 tools/evalcheck.py tasks/001-alc-physio
python3 tools/evalcheck.py --codes A10,E50    # only these checks
python3 tools/evalcheck.py --save             # write evaluation/checks/evalcheck-<date>.json
python3 tools/evalcheck.py --catalog          # regenerate docs/reference/check-rules.md
python3 tools/selftest.py                     # prove the checks still fire
```

Exit 1 on any ERROR. The rules are in
[docs/reference/check-rules.md](../docs/reference/check-rules.md).

## Two levels, because there are two kinds of artifact

This workspace checks two different things, and collapsing them to one level
would be wrong in both directions.

- **ERROR** on what we wrote: the rationale, the confidence note, the ratings.
  A defect, to fix before submitting.
- **NOTE** on a harness output. We cannot edit a model's deliverable. A prose
  tell there is an observation for the Format & Presentation rating, carried
  with its quote so the rating can cite it. It never blocks.
- **REC** never blocks and is used where the program has already ruled a
  finding non-blocking.

## What the E-codes are

A-codes are the prose checks. E-codes encode the platform's own Stage 5 rules
from
[the instruction transcript](../docs/reference/evaluation-instructions.md), and
each finding carries the quote it rests on, so a disagreement goes to the
source rather than to the tool.

E50 is the one worth running first. It extracts every money figure the
rationale states and resolves it against the outputs and the source files, so a
figure attributed to the wrong harness, or to nothing, surfaces before a
reviewer finds it.

## What this cannot do

It cannot tell whether a rating is right, and it cannot confirm a calculation
in a model's output. E50 proves a figure exists in the files; it does not prove
the figure is correct, and nothing here replaces recomputing from the source. A
clean run means nothing is mechanically wrong with the submission.
