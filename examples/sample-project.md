# Sample Project: `quietlog`

> A fictional project for trying DevReach skills. Copy any section below into Claude Code as input. Everything here is made up.

## What it is

`quietlog` is an open-source (MIT) Python library that wraps the standard `logging` module and automatically removes secrets — API keys, bearer tokens, passwords in URLs — from log messages before they're written.

- Install: `pip install quietlog`
- Repo: `github.com/example/quietlog` (fictional)
- Python 3.9+; no dependencies.

## Facts the author can verify

- Built over 6 weeks, nights and weekends, by one developer.
- Detects 14 secret patterns (AWS keys, GitHub tokens, Stripe keys, JWTs, `password=` in URLs, etc.).
- Adds about 4 µs per log call in the author's benchmark on an M2 MacBook (benchmark script in `bench/`).
- 37 GitHub stars, 2 outside issues, 0 outside PRs.
- Started after the author's team accidentally logged a Stripe key to a third-party log service at work. (The author may say this happened; no company name.)

## Hardest problem

Regex patterns for secrets caused false positives on UUIDs and hashes. The author added an entropy check plus a context check (key name near the value) to cut false positives.

## Author's goals

- Find 10 teams who will try it in a real service.
- Get one outside contributor to add a new secret pattern.

## Try it with

| Skill | Prompt |
| --- | --- |
| `project-to-post` | "Write a LinkedIn post about quietlog using examples/sample-project.md. Audience: backend developers." |
| `community-launch` | "Plan where to launch quietlog using examples/sample-project.md." |
| `open-source-growth` | "Draft 3 good first issues for quietlog based on examples/sample-project.md." |
| `outreach-writer` | "Draft a message to the maintainer of a popular Python logging library asking whether they'd link quietlog in their docs." |
