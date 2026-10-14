# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Bluesky and Mastodon norms in the `community-launch` community guide (#11, thanks @Enard52).

## [0.1.1] - 2026-10-14

### Security

- `open-source-growth` no longer runs a reviewed repository's install or quick-start commands on its own. It reads them first and runs them only after the user approves the exact commands, ideally in an isolated environment. Installing an untrusted repository can execute its code.
- The validator now rejects non-Markdown files, symlinks, HTML comments, invisible/bidi Unicode, and frontmatter keys other than `name`, `description`, `license` (for example `allowed-tools`) in `skills/`.
- The eval fixture's prompt-injection payload is now harmless (it no longer contains a real `gh api` command).
- GitHub Actions are pinned to commit SHAs with `persist-credentials: false`; added Dependabot for Actions and CODEOWNERS.
- Repository settings: private vulnerability reporting, Dependabot alerts and security updates, and a ruleset protecting `main`.

### Added

- `AGENTS.md` / `CLAUDE.md` warning agents that `evals/` contains deliberate test injections and fake secrets.
- SECURITY.md threat model and instructions for pinning a release tag.

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
