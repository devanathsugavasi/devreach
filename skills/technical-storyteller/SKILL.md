---
name: technical-storyteller
description: Turns an engineering decision, debugging session, outage, or lesson learned into a long-form technical article or blog post with a clear narrative arc. Use when a developer has a real technical experience worth explaining in depth — a postmortem, a "how we solved X", a migration story — for a blog, dev.to, Hashnode, or an engineering blog.
---

# Technical Storyteller

## Purpose

Engineers learn the most from stories about real problems: what broke, what was tried, what worked, and why. These stories usually stay in Slack threads because writing them up is hard. This skill turns raw material — notes, commit history, logs, a chat transcript — into a structured article that a peer engineer can learn from.

## When to Use

- "Write a blog post about how we debugged the memory leak."
- "Turn these notes about migrating from REST to gRPC into an article."
- "I want to write about why we chose SQLite over Postgres."

Not for: short social posts (use `project-to-post`), release notes (use `launch-announcement`).

## Inputs

Required:

1. **Raw material**: notes, timeline, commits, error messages, chat logs, or a verbal account.
2. **Reader**: who should learn from this (e.g. backend engineers new to Kubernetes).
3. **Where it will be published** — this sets length and how much internal detail is allowed.

Helpful: code snippets, before/after measurements, diagrams, the dead ends tried.

## Workflow

1. **Reconstruct the timeline.** List events in order: symptom → investigation steps → dead ends → root cause → fix → verification. Mark any gaps.
2. **Find the transferable lesson.** Ask: what would a reader at another company do differently after reading this? If there's no transferable lesson, tell the user — the piece may be better as an internal note.
3. **Choose a structure:**
   - *Detective story* (debugging): symptom → clues → wrong turns → reveal → lesson.
   - *Decision record* (choosing tech): context → options → criteria → choice → what happened after.
   - *Migration story*: why move → plan → what went wrong → results → advice.
4. **Outline first.** Present a 5–8 heading outline with one line each and get a quick confirmation if the user is available; otherwise proceed and note that you did.
5. **Draft.** Use concrete details: actual error messages, real config snippets, measured numbers. Keep dead ends — they're often the most useful part. Use code blocks for code and commands.
6. **Scrub for confidentiality.** Replace internal hostnames, customer names, IPs, keys, and proprietary numbers with placeholders and list what you replaced.
7. **Write title options and a summary** (2–3 sentences for previews/SEO).

## Output Format

```
**Lesson:** <one sentence a reader takes away>
**Structure:** <detective / decision / migration>

**Title options**
1. ...
2. ...
3. ...

**Summary:** <2–3 sentences>

**Article**
<full markdown article>

**Redactions made**
- <original type> → <placeholder>

**Gaps** (details that would strengthen the piece)
- ...
```

## Quality Checklist

- The lesson is stated explicitly, near the start and again at the end.
- At least one dead end or wrong assumption is included.
- Every number in the article was supplied by the user or present in their material.
- Code snippets are syntactically plausible and labeled with a language.
- A reader unfamiliar with the user's company can follow every paragraph.

## Safety

- Remove secrets, internal URLs, customer data, and security-sensitive details (e.g. an unpatched vulnerability) before drafting.
- If the story involves a security incident, recommend the user get approval from their security team before publishing.
- Don't assign blame to named individuals; write postmortem-style, blameless.
- Return the draft; do not publish.

## Example

**Input**

> Notes: Our Node API p99 went from 200ms to 4s after deploy on Tuesday. Thought it was the DB — added indexes, no change. Then thought GC — heap was fine. Finally found we'd upgraded a logging lib that switched to sync file writes. Reverted, p99 back to 200ms. Then pinned version and added a latency check to CI. Audience: Node backend devs. For dev.to.

**Output (abbreviated)**

**Lesson:** A dependency upgrade can turn async I/O into sync I/O silently; measure latency in CI, not only in production.
**Structure:** Detective story.

**Title options**
1. Our p99 went from 200ms to 4s. The database was innocent.
2. How a logging library upgrade blocked our Node event loop
3. Two wrong guesses and one sync write: debugging a 20× latency regression

**Article outline**
1. The symptom (p99 200ms → 4s after Tuesday's deploy)
2. Suspect #1: the database (added indexes — no change)
3. Suspect #2: garbage collection (heap normal)
4. The real culprit: a logger switching to synchronous writes
5. Why sync I/O hurts so much in Node (event loop explanation)
6. The fix and the guardrail (pin version, latency check in CI)
7. What we'd tell you to do today

**Gaps**
- The logging library's name and version numbers — needed for readers to check their own apps.
- How the CI latency check works (tool, threshold).
