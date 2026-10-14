# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-10-14

### Added

- Twelve Claude Code skills in four groups: developer branding, content marketing, community and distribution, outreach and growth strategy.
- Four core skills with worked examples: `project-to-post`, `developer-profile`, `community-launch`, `open-source-growth`. The other eight are marked experimental.
- `scripts/validate_skills.py` — standard-library validator for skill structure and frontmatter.
- `scripts/check_links.py` — checks relative Markdown links resolve.
- Unit tests for the validator, link checker, eval case layout, and install script (`tests/`).
- Claude Code plugin and marketplace manifests (`/plugin install devreach --marketplace devanathsugavasi/devreach`).
- `install.sh` to install, list, or remove individual skills.
- 48 behavioral eval cases in `claude plugin eval` format (4 per skill) with LLM-judge, skill-fired, and secret-leak graders, plus a fixture repository for `open-source-growth`.
- `scripts/eval_summary.py` to summarize eval runs; first full run recorded in `evals/RESULTS.md`.
- Human-review rubric (`evals/rubric.md`).
- GitHub Actions workflow running validation and tests.
- Community files, issue templates, and pull request template.
