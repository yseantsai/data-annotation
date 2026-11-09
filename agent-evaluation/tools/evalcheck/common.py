"""Text readers and sentence splitting.

The docx reader is zipfile and regex, so the checks run on the system
interpreter with no third-party package: paragraph text is the document XML
with the tags stripped, one paragraph per line. The sentence splitter is shared
by every check that reads sentences.
"""
import re
import zipfile
from pathlib import Path

_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+")
_SENTENCE_END_CAP_RE = re.compile(r"(?<=[.!?])\s+(?=[\"“'(]?[A-Z])")


def split_sentences(text, capital=False):
    """Sentences of `text`, split after . ! ? and whitespace; with `capital`, only where the
    next character (after an optional opening quote or paren) is a capital, which keeps
    '2.10 and' and '5,365.50 and' whole."""
    return (_SENTENCE_END_CAP_RE if capital else _SENTENCE_END_RE).split(text)


def docx_text(path):
    """Paragraph text of a .docx, one paragraph per line."""
    with zipfile.ZipFile(path) as z:
        if "word/document.xml" not in z.namelist():
            return ""
        xml = z.read("word/document.xml").decode("utf-8", "ignore")
    xml = re.sub(r"</w:p>", "\n", xml)
    return re.sub(r"<[^>]+>", "", xml)


def docx_emdash_stats(path):
    """A6: em-dash count and word count of a docx's paragraph text."""
    with zipfile.ZipFile(path) as z:
        if "word/document.xml" not in z.namelist():
            return None
        xml = z.read("word/document.xml").decode("utf-8", "ignore")
    text = " ".join(m.group(1) for m in re.finditer(r"<w:t[^>]*>([^<]*)</w:t>", xml))
    text = text.replace("&#8212;", "—").replace("&mdash;", "—")
    return text.count("—"), len(text.split())


_MD_FENCE_RE = re.compile(r"^```")
_MD_HEADING_RE = re.compile(r"^#{1,6}\s+")


def read_text(path):
    """Text of a .md, .txt or .docx, as the checks want to read it."""
    path = Path(path)
    if path.suffix.lower() == ".docx":
        return docx_text(path)
    return path.read_text(encoding="utf-8", errors="ignore")


def prose_only(text):
    """`text` with markdown tables, fenced code and heading markers removed.

    The prose checks judge sentences a reader reads. A pipe table is data, and
    A20 would read every row as a run-on, so any line holding a pipe is skipped.
    """
    out, in_fence = [], False
    for line in text.split("\n"):
        if _MD_FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence or "|" in line:
            continue
        out.append(_MD_HEADING_RE.sub("", line))
    return "\n".join(out)


def word_count(text):
    return len(text.split())


def markdown_headings(text):
    """ATX headings of a markdown file, as text without the # markers."""
    out = []
    for line in text.split("\n"):
        s = line.strip()
        if _MD_HEADING_RE.match(s):
            out.append(_MD_HEADING_RE.sub("", s).strip())
    return out
