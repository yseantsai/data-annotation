#!/usr/bin/env python3
"""Convert PDFs to Markdown with page markers, for citation checking.

    .venv/bin/python tools/pdf_to_md.py <in.pdf> [<in.pdf> ...] --out <dir>

Each page becomes a `## Page N` section so a cited page locator can be checked
directly. Text is pypdf's extraction, unedited: no reflow, no cleanup, so a
paragraph number in the source survives as printed. A page with no extractable
text is marked as such rather than silently dropped, since that usually means a
scanned image or a filled form field the extractor cannot see.
"""
import argparse
import sys
from pathlib import Path

from pypdf import PdfReader


def convert(src, out_dir):
    reader = PdfReader(str(src))
    lines = ["# %s" % src.stem, "",
             "Converted from `inputs/%s` by `tools/pdf_to_md.py` (pypdf). "
             "Text is unedited extraction; check layout and form fields against the "
             "original PDF." % src.name, ""]
    empty = []
    for i, page in enumerate(reader.pages, 1):
        text = (page.extract_text() or "").strip()
        lines.append("## Page %d" % i)
        lines.append("")
        if text:
            lines.append(text)
        else:
            empty.append(i)
            lines.append("_[no extractable text on this page]_")
        lines.append("")
    # Form fields: an I-360 carries its answers here, not in the page text.
    fields = reader.get_fields() or {}
    filled = [(k, v.get("/V")) for k, v in fields.items() if v.get("/V") not in (None, "", "/Off")]
    if filled:
        lines += ["## Filled form fields", "",
                  "| Field | Value |", "| --- | --- |"]
        for k, v in filled:
            lines.append("| %s | %s |" % (str(k).replace("|", "/"), str(v).replace("|", "/")))
        lines.append("")
    dest = out_dir / (src.stem + ".md")
    dest.write_text("\n".join(lines), encoding="utf-8")
    return len(reader.pages), empty, len(filled), dest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdfs", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for p in a.pdfs:
        n, empty, nf, dest = convert(Path(p), out)
        note = (" | no text on pages %s" % empty) if empty else ""
        ff = (" | %d filled form fields" % nf) if nf else ""
        print("%-48s %3d pages%s%s" % (Path(p).name, n, note, ff))


if __name__ == "__main__":
    sys.exit(main())
