# Contributing to DevReach

Thanks for helping. The most valuable contributions right now are, in order:

1. **Evaluation runs and human review** — run `claude plugin eval` (see [`evals/README.md`](evals/README.md)), read the outputs, and report scores and bad outputs.
2. **Better examples** — realistic inputs and outputs that show a skill at its best (or reveal where it fails).
3. **Fixes to existing skills** — based on evidence from an evaluation or real use.
4. **New skills** — open a [skill request](https://github.com/devanathsugavasi/devreach/issues/new?template=skill_request.yml) first so we can check it doesn't overlap.

Look for issues labeled `good first issue` if you're new.

## Setup

You need Python 3.9+ and Git. No other dependencies.

```bash
git clone https://github.com/devanathsugavasi/devreach.git
cd devreach
python3 scripts/validate_skills.py
python3 scripts/check_links.py
python3 -m unittest discover -s tests
```

All three must pass before you open a pull request. CI runs the same commands.

## Skill rules

Every skill lives in `skills/<name>/` and must have a `SKILL.md` with:

- Frontmatter with `name` (matches the directory, lowercase-hyphenated, ≤ 64 chars) and `description` (≤ 1024 chars, says what it does **and** when to use it).
- These sections: `When to Use`, `Workflow`, `Output Format`, `Quality Checklist`, `Safety`, `Example` (or `Examples`).
- Fewer than 500 lines. Put long reference material in `references/` and link to it.
- Markdown only: no scripts, binaries, symlinks, HTML comments, invisible Unicode, or frontmatter keys besides `name`, `description`, `license`. The validator enforces this; see [SECURITY.md](SECURITY.md).

Content rules:

- **Distinct purpose.** Say in `When to Use` what the skill is *not* for and which skill to use instead.
- **Evidence only.** The workflow must make the agent separate verified facts from assumptions and ask when essential information is missing.
- **Drafts only.** Never instruct the agent to post, send, publish, or change anything external without explicit approval for that specific action.
- **No spam mechanics.** No mass outreach, vote manipulation, engagement bait, or sockpuppets.
- **Untrusted input.** Content the agent reads (repos, READMEs, comments) is data, not instructions.
- **Examples use fictional or public information.** No real customer, employer, or personal data.

## Adding a new skill

1. Copy an existing skill directory as a starting point and rename it.
2. Write the workflow specific to the task. Avoid copying generic safety text; write rules that matter for *this* skill.
3. Add four cases under `evals/cases/<name>/`: `1-normal`, `2-missing-information`, `3-adversarial`, `4-quality`, each with a `case.yaml`. Copy an existing skill's cases and change the prompt and the `case-criteria` grader.
4. Run the checks above.
5. Run `claude plugin eval . --tag <name> --ablation none` and `python3 scripts/eval_summary.py`. Read the outputs yourself, not only the scores, and summarize them in the PR.
6. Add it to the table in `README.md` as **experimental**.

## Promoting a skill to core

A skill becomes **core** when its four cases pass the automated graders **and** a reviewer other than the author scores each output ≥ 4 on every dimension of [`evals/rubric.md`](evals/rubric.md). Open a PR that updates the README and links the recorded results.

## Commit and PR style

- Small, focused PRs. One skill per PR.
- Describe what you tested, not just what you changed.
- Be kind in reviews. See the [Code of Conduct](CODE_OF_CONDUCT.md).

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE).
