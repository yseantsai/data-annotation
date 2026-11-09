# Stages 2 and 4: rate one result

Rate the result as it is, against the standard of a strong professional in the
field, counting only errors you verified in the files. Not against the other
harness: that comparison is Stage 5.

## Open every file

Download the output files and open each in its own application: Word, Excel,
PowerPoint, a PDF reader. Go through every sheet, slide and page, and read the
final message. Judging from a preview is explicitly not acceptable, and in this
workspace judging from the Markdown conversion is the same mistake wearing a
different hat.

Anything about length, pagination, table layout or visual polish is decided
from the page images in `evaluation/converted/<harness>/`, never from the
Markdown conversion beside them.

## Verify before you fault

The instruction is to count only errors you verified in the files. In practice
that means three different things, and they are worth keeping apart:

- **Verified error.** The output states a figure, you recomputed it from the
  source, and it disagrees. This is a fault, and the rating moves.
- **Unsupported claim.** The output asserts something the files neither
  establish nor contradict, and acts on it. This is a fault of professional
  judgment, and the rating moves, but the finding is "the files do not support
  this", not "this is wrong".
- **Defensible difference.** The output took a route you would not have taken,
  and the files permit it. The rating does not move. Write it down anyway, so
  Stage 5 does not rediscover it as a fault.

`tools/evalcheck.py` E50 will later check that every figure the rationale
quotes exists somewhere in the files. It cannot check that your arithmetic was
right, so do the arithmetic here, and record where it came from.

## The reference solution is a floor

The reference solution description is the minimum standard for a correct,
complete result, not a ceiling and not an answer key. Apply domain expertise
for consequential strengths or errors it does not mention. A result that
matches it exactly is correct and complete; it is not thereby exemplary.

## Record the rating

Fill this harness's column in `evaluation/ratings.md`, copied from
`templates/ratings.md`. Four dimensions on the platform's five-point scale
(Poor, Below par, Acceptable, Good, Excellent), then overall quality 1 to 7.

The form anchors the scale: Excellent means a strong professional would hand
it in as-is on this dimension, Acceptable means it does the job with rough
edges, Poor means it would be sent back. Use the full scale. Each dimension is
rated alone, and the form routes issues: inaccurate content belongs to
Correctness, poor domain choices or framing to Professional Judgment, and
structural or visual quality to Format & Presentation, unless the prompt
explicitly required the feature, in which case it stays under Instruction
Following. For that dimension, judge whether the response completed what was
asked, not whether the content was correct or elegantly presented.

| Dimension | The question |
| --- | --- |
| Instruction Following | Did it deliver what was asked and follow the rules set in the prompt and files? |
| Correctness | Are the facts, figures and citations right and traceable to the files? |
| Professional Judgment | Did it show sound professional judgment, pitched at the right audience? |
| Format & Presentation | Is it well structured, polished and close to client-ready? |
| Overall quality | Taking everything into account, how good is it as a piece of professional work? |

Under **Evidence for each rating**, one line per rating that is not
self-evident, naming the file and the location that decided it. Those lines are
the raw material for the rationale, and writing them now is what stops Stage 5
from becoming an exercise in remembering.

Overall quality of 7 means you would hand it in as-is. If you would edit it
first, it is not a 7, however good the analysis is.

## Prose tells in the output

`python3 tools/evalcheck.py --codes A6,A10,A20,A32,A33` reports NOTE findings
against the harness outputs: em-dash density, generic heading pairs, uniform
bullet runs, the flagged prose shapes. These are observations for Format &
Presentation, with the quote attached so a rating can cite it. They are never
defects to fix, because the output is not ours to edit, and a NOTE never
blocks.

Weigh them, do not count them. A deliverable with two generic headings and
correct figures is better professional work than a well-titled one that is
wrong, and the dimension that carries the most weight is whichever one the
client would notice first.
