---
name: launch-announcement
description: Prepares release materials for a software release or launch — release notes or changelog entries from commits, a short announcement, a demo script, and a launch-day checklist. Use whenever a developer is shipping a new version, v1.0, or first public release and asks for release notes, a changelog, an announcement, a demo script, or help to tag, release, or publish a package.
---

# Launch Announcement

## Purpose

Launches fail on small things: release notes nobody can read, a demo that runs too long, a broken install link discovered after posting. This skill turns the raw changes into clear release materials and a checklist that catches the common launch-day mistakes.

## When to Use

- "We're releasing v2.0 on Friday. Help me prepare."
- "Write release notes from these commits."
- "Write a 90-second demo script for our launch."

Not for: choosing communities and writing community-specific posts (use `community-launch` after this), long technical write-ups (use `technical-storyteller`).

## Inputs

Required:

1. **What's shipping**: changelog, commit log (`git log <last-tag>..HEAD --oneline`), PR list, or a description.
2. **Version and date.**
3. **Audience**: existing users, new users, or both.

Helpful: breaking changes and migration steps, screenshots, who contributed, known issues.

## Workflow

1. **Group the changes** into: Breaking changes, New, Improved, Fixed, Deprecated. Drop internal-only changes (CI tweaks, refactors) unless users would notice.
2. **Write user-facing release notes.** Each line says what changed *for the user*, not what the code does: "Exports now include timezone offsets" beats "refactor datetime serializer". Put breaking changes first with migration steps.
3. **Credit contributors** by handle when the user provides them or they appear in the commit log.
4. **Write the announcement** (≈ 100–200 words): what it is in one line, the one or two changes that matter most, how to get it, where to give feedback.
5. **Write the demo script** for the requested length (default 90 seconds): show the main change working within 10 seconds; one flow, no setup on camera.
6. **Produce the launch checklist** using [`references/launch-checklist.md`](references/launch-checklist.md), filtered to what applies.
7. **Return everything for review.** Do not create tags, releases, or posts.

## Output Format

```
## Release notes — v<x.y.z> (<date>)
### ⚠️ Breaking changes
### New
### Improved
### Fixed
### Contributors

## Announcement
<text>

## Demo script (<length>)
| Time | On screen | Say |

## Launch checklist
- [ ] ...

## Open questions
- <anything unclear in the changes>
```

## Quality Checklist

- Every release-note line maps to a real commit, PR, or user-provided change.
- Breaking changes appear first and include migration steps.
- The announcement says how to install/upgrade.
- The demo shows the main feature in the first 10 seconds.
- Semantic versioning matches the changes (a breaking change in a minor release is flagged).

## Safety

- Do not invent backstory, motivation, feelings, opinions, or habits and put them in the user's mouth ("we did this by hand every time", "this is the work I most want to do", "I wouldn't expect to beat X"), and do not describe how something works beyond what the user or their files say. Where a draft needs one, write a `[bracketed prompt]` for the user to fill in.
- Do not mention unreleased features, internal ticket numbers, or customer names.
- Do not claim performance improvements without a measurement from the user.
- Do not run `git tag`, `gh release create`, or publish to package registries without explicit approval for that action.

## Example

**Input**

> v0.4.0 of `tidyenv` (a CLI that finds unused env vars). Commits: "add --json output", "support .env.local", "fix crash on empty file", "rename --dir to --path (keep --dir as alias, warn)", "bump ci node to 22". Ship Thursday. Audience: existing users.

**Output (abbreviated)**

## Release notes — v0.4.0

### ⚠️ Deprecated
- `--dir` is now `--path`. `--dir` still works but prints a warning and will be removed in a future release. Update scripts to use `--path`.

### New
- `--json` output for use in CI and scripts.
- `.env.local` files are now scanned.

### Fixed
- No longer crashes on an empty `.env` file.

*(CI Node version bump omitted — not user-facing.)*

## Open questions
- When will `--dir` be removed? Stating a version helps users plan.
