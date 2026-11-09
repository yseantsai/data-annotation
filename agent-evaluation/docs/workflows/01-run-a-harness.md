# Stages 1 and 3: run the task in a harness

Run the task once in each harness with the identical prompt and input files.
The task folder's README states which harness goes first; that order is set per
task and is not ours to choose. Run each harness once. If a run fails for a
technical reason, retry it and keep only the finished run.

## Before the first run

- Check the category is inside your professional expertise. If it is not, skip
  the task; there is no penalty, and a rating from outside the field is worth
  less than no rating.
- Antigravity only: all plugins and connectors disabled or removed
  (Customizations, Installed), and the model picker showing the model the
  instructions require. The screenshot of the picker is part of the submission.
- Use the escape hatch only for a platform error or an input folder that will
  not download or open. Not for a task that turns out to be hard.

## Record before you run

In `tasks/NNN-name/prompt.md`, copied from `templates/prompt.md`, before the
run and not after:

- the exact prompt text, as pasted
- the input files given, by name
- which instruction version applied

`evalcheck` E05 fails a task with no prompt file, and fails one still carrying
the template placeholder.

The point of writing it first is that a prompt reconstructed after the fact is
a reconstruction. Two harnesses have to receive the same thing, and the only
proof of that is the text recorded once and pasted twice.

## Save the outputs

```text
tasks/NNN-name/prompt.md        recorded before the first run
tasks/NNN-name/outputs/<harness>/
  result.md         the model's final chat message (any .md name is fine)
  <files>           the model's files, unedited, original names
  <harness>-outputs.zip   the download, if there was one
```

Nothing else goes in that folder. Conversions made for reading and checking
(Markdown, PDF, page images) are written by the tools to
`evaluation/converted/<harness>/`. They drop formatting, so nothing about
layout, pagination or visual presentation is ever decided from them; the page
images there exist for that.

Save the final message. It is part of what a client receives, and Stage 2 asks
you to read it.

## Then stop

Rate this result before running the second harness. Go to
[02-rate-a-result.md](02-rate-a-result.md).
