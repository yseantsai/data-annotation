# Prompt: collect the assets for one evaluation task

Paste everything below the rule into the assistant that has access to the
evaluation platform (browser) and to this workspace on disk. Replace the three
placeholders first. Copy a fresh version for every task.

---

You are collecting the files for one agent-evaluation task so that a separate
reviewer can evaluate it. You are not evaluating anything and you are not
running the task. Your only job is to fetch, record and file, exactly as
instructed, and to report what you could not get.

Placeholders:

- Task page: {TASK_URL}
- Workspace root: {WORKSPACE} (for example /Users/ritaguest/projects/data-annotation/agent-evaluation)
- Task folder name: {TASK_FOLDER} (pattern NNN-short-slug, for example 003-lease-review)

## Target layout

Create this and nothing else. Do not add subfolders.

```text
{WORKSPACE}/tasks/{TASK_FOLDER}/
  README.md                 copy of {WORKSPACE}/templates/task.md, header filled in
  prompt.md                 copy of {WORKSPACE}/templates/prompt.md, with the task prompt pasted verbatim
  reference-solution.md     the reference solution, verbatim, on its own
  inputs/                   the input zip as downloaded, plus its unpacked files
  outputs/gemini-native/    (created empty if that run has not happened yet)
  outputs/antigravity/      (created empty if that run has not happened yet)
  evaluation/               (created empty)
```

## What to collect, in order

1. **Task prompt.** Copy the prompt text exactly as shown on the task page,
   character for character, including headings, blank lines, lists and any
   file names. Do not reformat, correct, summarise or translate it. Paste it
   into the prompt section of `prompt.md`. Below it, in the section the
   template provides, list the input file names and note the zip name.
2. **Reference solution.** The task page usually shows a reference or sample
   solution below the input files, sometimes under a heading such as
   "Reference solution", "Expected answer" or "Golden response". Copy it
   verbatim into `reference-solution.md`. It must never be pasted into
   `prompt.md` or into any harness. If there is none, write
   `No reference solution shown on the task page on <date>.` in that file.
3. **Input files.** Download the input archive into `inputs/` under its
   original name and unpack it there, keeping the original file names. Remove
   only `__MACOSX` folders and `.DS_Store` files. Do not open the files in an
   editor that could save them.
4. **Task metadata.** Fill the header of `README.md`:
   - Category, as the page states it
   - Required harness order (which harness is Stage 1 and which is Stage 3),
     quoted from the "How this task works" text
   - Instruction source or version, if the page names one
   - Expected time, if the page states one
   - Any rating form details visible without submitting: dimension names, the
     rating scale words, the preference options, the confidence options
5. **Harness outputs, only if a run has already happened.** For each harness
   that has run, put into `outputs/<harness>/`:
   - the final chat message, saved as `result.md`, verbatim, including any
     Markdown the model produced
   - the output download (zip) under its original name, unpacked beside it
     if it contains deliverable files
   - for Gemini Native, the run transcript or output JSON if the platform
     offers one
   - for Antigravity, the model-picker screenshot the instructions require,
     saved as `model-picker.png`
   Do not rename, reformat or "clean up" any of these. Do not create the
   folder's contents from memory; if the output is not retrievable, leave
   the folder empty and say so in the report.

## Rules

- Verbatim means verbatim. If a page element cannot be copied exactly (for
  example a rendered table), copy what you can and flag the element in the
  report rather than reconstructing it.
- Never paste the reference solution anywhere except `reference-solution.md`.
- Never run the task, start a harness, or submit anything on the platform.
- Never delete or overwrite a file already in the task folder. If a file
  exists, stop and report.
- Use `templates/task.md` and `templates/prompt.md` as given; fill
  placeholders, do not restructure them.

## Report back

Finish with this report, nothing else:

```text
Task folder: tasks/{TASK_FOLDER}
Collected:
  prompt.md               yes / no   (word count)
  reference-solution.md   yes / none shown / could not copy
  inputs/                 <zip name>, <N> files unpacked: <names>
  outputs/gemini-native/  <files> or "no run yet"
  outputs/antigravity/    <files> or "no run yet"
  README.md header        filled fields: <list>
Harness order on the page: Stage 1 <harness>, Stage 3 <harness>
Could not get: <each item, with the reason>
Anything I changed from the instructions above: none / <what and why>
```
