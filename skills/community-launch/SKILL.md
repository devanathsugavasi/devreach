---
name: community-launch
description: Plans where and how to share a project in developer communities (subreddits, Hacker News, Discord/Slack servers, forums, Product Hunt) and drafts a separate, rule-aware post for each one. Use when a developer is ready to announce a project and wants to reach people who will care without spamming or getting removed.
---

# Community Launch

## Purpose

Developers often paste the same announcement into ten communities and get ignored or banned. Each community has different rules, norms, and reasons people show up. This skill picks a small number of communities where the project genuinely fits, explains what each one expects, and drafts a post written for that audience — for the user to review and post themselves.

## When to Use

- "Where should I post my project?"
- "Write a Show HN post for this."
- "Help me launch this on Reddit without getting removed."
- "Make a launch plan for these three communities."

Not for: the announcement content itself across social platforms (use `launch-announcement` or `multi-platform-content`), or replying to comments after launch (use `community-engagement`).

## Inputs

Required — ask if missing:

1. **The project**: what it does, who it's for, link, license, price (free/paid/open source).
2. **Readiness**: Is there a working demo or install path a stranger can use today?
3. **The user's existing presence**: communities they already participate in. Being an active member matters more than any post.

Helpful: communities the user already has in mind, past launch attempts and how they went, the user's time zone.

## Workflow

1. **Check readiness first.** If a stranger can't try the project in under 5 minutes (no demo, broken install, private repo), say so and list what to fix before launching. Launching too early wastes a one-time chance in most communities.
2. **Shortlist 3–6 communities.** For each, state *why the project fits that audience*. Prefer communities the user already participates in. Use [`references/community-guide.md`](references/community-guide.md) for norms of common venues.
3. **Flag rules to verify.** You cannot see current community rules. For each venue, list what the user must check (self-promotion ratio, flair, allowed days, "Show" format requirements) and tell them to read the rules/sidebar before posting. Never claim a rule is current.
4. **Draft one post per community.** Each draft must differ in title, framing, and length to fit that venue. Lead with the problem and what's interesting, not with "I built". Include what feedback the user wants.
5. **Write the first comment** where the venue expects one (e.g. Show HN context comment, Reddit OP comment with technical details).
6. **Sequence the launch.** Suggest order and spacing (not all on one day), and what the user should be ready to do in the first two hours (answer questions, fix install bugs).
7. **Return for review.** Do not post.

## Output Format

```
**Readiness:** <ready / not ready> — <reasons, and fixes if not ready>

**Shortlist**
| Community | Why it fits | Rules to check before posting |
| --------- | ----------- | ----------------------------- |

**Drafts**
### <Community 1>
Title: ...
Body: ...
First comment (if applicable): ...

### <Community 2>
...

**Launch sequence**
1. <day / time> — <community> — <what to be ready for>

**Do not**
- <venue-specific mistakes to avoid>
```

## Quality Checklist

- No two drafts share the same title or opening line.
- Each draft says who the project is for and what's interesting in the first two lines.
- Every draft asks for a specific kind of feedback.
- No "please upvote", "please star", or vote-manipulation language anywhere.
- Rules are presented as "check this", never as verified facts.
- Number of communities is small enough that the user can respond to every comment.

## Safety

- Never draft posts for communities where the project clearly doesn't fit, even if they are large.
- Never suggest vote rings, asking friends to upvote, sockpuppet accounts, or reposting after removal to evade moderators.
- Never suggest cross-posting the same text to many communities at once.
- If the project collects user data, make sure the draft mentions it honestly.
- The user posts manually. Do not use tools to post, even if available, unless the user explicitly approves each individual post.

## Example

**Input**

> I built `pgdiff-lite`, an MIT-licensed CLI (Go) that compares two Postgres schemas and prints a migration SQL file. Single binary, `brew install` works. I'm active in r/golang (comment there sometimes). Never posted on HN. Want feedback on edge cases it misses.

**Output (abbreviated)**

**Readiness:** Ready — public repo, single-binary install, MIT license.

**Shortlist**
| Community | Why it fits | Rules to check before posting |
| --- | --- | --- |
| Hacker News (Show HN) | Developer tools with a working install are the core of Show HN | Show HN guidelines: must be something people can try; no signup walls |
| r/golang | You're already active; Go CLI tools are on-topic | Self-promotion rules and any required flair |
| r/PostgreSQL | Audience has exactly the problem | Self-promotion rules; some subs require participation history |

**Hacker News**
Title: Show HN: pgdiff-lite – Diff two Postgres schemas into a migration file
First comment: Why I built it (one paragraph), how it works (reads `information_schema` / `pg_catalog`, builds a dependency graph, emits ordered DDL), what it doesn't handle yet, and a direct request: "I'd especially like schemas that break it."

**r/PostgreSQL**
Title: I wrote a small schema-diff CLI and I'm looking for schemas that break it
Body: leads with the edge cases you already know it misses (e.g. partitioned tables, if true), asks for test cases.

**Launch sequence**
1. r/golang first (friendliest audience, you're known there) — fix install issues reported.
2. Show HN 2–3 days later on a weekday morning US time — stay online for 2 hours.
3. r/PostgreSQL after incorporating early feedback.
