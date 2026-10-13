# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-10-13

### Added

- Twelve Claude Code skills in four groups: developer branding, content marketing, community and distribution, outreach and growth strategy.
- Four core skills with worked examples: `project-to-post`, `developer-profile`, `community-launch`, `open-source-growth`. The other eight are marked experimental.
- `scripts/validate_skills.py` — standard-library validator for skill structure and frontmatter.
- `scripts/check_links.py` — checks relative Markdown links resolve.
- Unit tests for the validator (`tests/`).
- Manual evaluation rubric and per-skill evaluation cases (`evals/`).
- GitHub Actions workflow running validation and tests.
- Community files, issue templates, and pull request template.
