#!/usr/bin/env python3
"""Render a harness's output documents to PDF and page images, for visual review.

    .venv/bin/python tools/render.py tasks/NNN-name/outputs/<harness>
    .venv/bin/python tools/render.py <file.docx|.xlsx|.pptx|.pdf> --out <dir>

DOCX, XLSX and PPTX go through headless LibreOffice to PDF, which is how task
001's renders were made; a PDF is used as-is. Every PDF page is then drawn to
`page-N.png` with pypdfium2. With a harness folder, sources are read from
the folder given and written to `evaluation/converted/<inputs|harness>/`.

Length, pagination and layout are judged from these renders, never from the
Markdown conversions. A render is LibreOffice's layout, which can differ from
Word's by a line or two at a page break, so a result that sits right at a page
limit is worth opening in Word before it is marked down.
"""
import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pypdfium2 as pdfium

SOFFICE_CANDIDATES = [
    Path.home() / "Applications/LibreOffice.app/Contents/MacOS/soffice",
    Path("/Applications/LibreOffice.app/Contents/MacOS/soffice"),
]
OFFICE_EXT = {".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".odt", ".rtf"}
SCALE = 2.0   # 144 dpi: legible for reading a page, small enough to keep


def soffice():
    for p in SOFFICE_CANDIDATES:
        if p.exists():
            return str(p)
    found = shutil.which("soffice")
    if found:
        return found
    sys.exit("LibreOffice not found; expected ~/Applications/LibreOffice.app")


def to_pdf(src, out_dir):
    """Convert one office file to PDF in out_dir, with a throwaway profile so a
    running LibreOffice or a stale lock cannot block the headless run."""
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run(
            [soffice(), "-env:UserInstallation=file://%s" % profile, "--headless",
             "--convert-to", "pdf", "--outdir", str(out_dir), str(src)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    pdf = out_dir / (src.stem + ".pdf")
    if not pdf.exists():
        raise RuntimeError("LibreOffice produced no PDF for %s" % src.name)
    return pdf


def to_pngs(pdf, out_dir, prefix=""):
    doc = pdfium.PdfDocument(str(pdf))
    paths = []
    for i in range(len(doc)):
        img = doc[i].render(scale=SCALE).to_pil()
        p = out_dir / ("%spage-%d.png" % (prefix, i + 1))
        img.save(p)
        paths.append(p)
    return paths


def render(src, out_dir, prefix=""):
    out_dir.mkdir(parents=True, exist_ok=True)
    if src.suffix.lower() == ".pdf":
        pdf = out_dir / src.name
        if pdf.resolve() != src.resolve():
            shutil.copy2(src, pdf)
    elif src.suffix.lower() in OFFICE_EXT:
        pdf = to_pdf(src, out_dir)
    else:
        return None
    pngs = to_pngs(pdf, out_dir, prefix)
    return pdf, pngs


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
    ap.add_argument("target", help="a harness folder, or a single file")
    ap.add_argument("--out", help="output dir (default: evaluation/converted/...)")
    a = ap.parse_args()
    t = Path(a.target)

    if t.is_dir():
        srcs = sorted(p for p in t.glob("*")
                      if p.suffix.lower() in OFFICE_EXT | {".pdf"})
        out = Path(a.out) if a.out else converted_dir(t)
        if not srcs:
            sys.exit("no office or PDF files in %s" % t)
        # one source: page-N.png, as task 001; several: prefix by file stem
        multi = len(srcs) > 1
        for s in srcs:
            r = render(s, out, prefix=(s.stem + "_") if multi else "")
            print("%-50s -> %s, %d page(s)" % (s.name, r[0].name, len(r[1])))
    else:
        out = Path(a.out) if a.out else t.parent
        r = render(t, out)
        if r is None:
            sys.exit("unsupported file type: %s" % t.suffix)
        print("%-50s -> %s, %d page(s)" % (t.name, r[0].name, len(r[1])))


if __name__ == "__main__":
    main()
