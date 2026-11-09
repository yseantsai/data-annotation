# Prose review references

Reference material for the prose we type into the platform, and for reading the register of a harness output. These are references, not instructions overriding the workflows.

| File | What it is |
| --- | --- |
| [style-guide-llm-tells.md](style-guide-llm-tells.md) | The platform's own style-guide table of LLM tells, with severities and fixes |
| [reviewer-checklist.md](reviewer-checklist.md) | The reviewer-side "signs of LLM use" scan list |
| [llm-prose-tells.md](llm-prose-tells.md) | The pattern classes behind check A10, and the mapping of every checklist line to a code or a read |
| [prose-standard.md](prose-standard.md) | The grammar side: em dashes, comma rules, and the sentence shapes that get sent back |

Read the style guide, then the checklist, then the catalog and the standard. The mechanical part is `python3 tools/evalcheck.py --codes A6,A10,A20,A21,A32,A33`, with the rules listed in [check-rules.md](../check-rules.md). The rest is a read, specified in [authorship-read.md](../../validators/authorship-read.md).
