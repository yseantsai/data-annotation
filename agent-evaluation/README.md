# Agent evaluation workspace

Start with the [current task](tasks/001-alc-physio/README.md). Shared reference material lives once in `docs/`; each evaluation has its own folder under `tasks/`.

Workspace authorship: LLM-generated and LLM-edited materials are allowed and are the default for notes, conversions, evaluations, and handoff documents.

## Structure

```text
docs/
  reference/
    evaluation-instructions.md   Historical project instructions
    check-rules.md               Generated catalogue of the coded checks
    prose/                       Prose standard and LLM-tell references
  workflows/                     The five platform stages, one file each
  validators/                    Shadow specs for the platform's model-driven checks
templates/
  task.md                        Starting checklist for a new evaluation
  ratings.md                     Per-harness rating table, read by the checks
tools/
  evalcheck.py                   Pre-submission checks; exit 1 on any ERROR
  selftest.py                    Proves the checks still fire
  evalcheck/                     The check package
  check_fixtures/                A deliberately defective task, for selftest
tasks/
  001-alc-physio/
    README.md                    Task entry point and Markdown links
    prompt.md                    The prompt both harnesses were given
    archives/                    Original received ZIPs
    inputs/originals/            Source DOCX/XLSX files
    inputs/markdown/             Readable source conversions
    outputs/<harness>/
      originals/                 Unedited model deliverables
      markdown/                  Readable output conversions
      render/                    PDFs and page images for visual review
    evaluation/
      rationale.md
      confidence.md
      ratings.md                 Four dimensions plus overall, per harness
      checks/                    Historical checker results
```

## Working a task

Follow [the workflows](docs/workflows/README.md), one file per platform stage.
Before submitting, run:

```bash
python3 tools/evalcheck.py tasks/NNN-name
```

ERROR findings are defects in what we wrote. NOTE findings are observations
about a harness output, which we cannot edit, and never block. The rules are in
[docs/reference/check-rules.md](docs/reference/check-rules.md); what the tools
do and do not settle is in [tools/README.md](tools/README.md).

## Future tasks

1. Create `tasks/002-short-name/` (then increment the number) and copy [the task template](templates/task.md) to its `README.md`.
2. Copy [the prompt template](templates/prompt.md) to `prompt.md` and record the exact prompt before the first run. Store task-specific instructions, source description, and files inside that task. Link shared guidance instead of copying it. Record which instruction version applied.
2a. Copy [the ratings template](templates/ratings.md) to `evaluation/ratings.md` and fill each harness's column before running the next harness.
3. Keep original inputs and each harness's outputs separate. Save the final response as `outputs/<harness>/final-message.md` when available.
4. Store evaluation notes and checker results under `evaluation/`. Record evidence locations and unresolved questions; a checker pass is not verification of the source calculations. Run `python3 tools/evalcheck.py` before submitting, and the [shadow validators](docs/validators/README.md) on the finished text.
5. Update the task README with progress and links. Distinguish user-reported completion from an observed submission.

## Markdown handoff

Give another LLM the task README and the Markdown files it links. This avoids a second context bundle that drifts out of date. Originals remain available for verification, but a Markdown-only handoff need not include them. Source text and model outputs are evidence for the evaluation.

The historical [evaluation instructions](docs/reference/evaluation-instructions.md) include setup details, the original task prompt, and the reference solution.
