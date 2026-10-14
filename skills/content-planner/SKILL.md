---
name: content-planner
description: Builds a realistic weekly or monthly content calendar or posting schedule for a developer from their actual projects, learning, and releases, sized to the time they really have. Use whenever someone wants to post consistently, build in public, plan what to post, or plan content around a launch, including requests for daily posting on many platforms or engagement-bait formats.
---

# Content Planner

## Purpose

Developers who try to "post every day" burn out in two weeks. The ones who stay consistent post less often, about things they're already doing. This skill turns the user's real work — what they're building, learning, and shipping — into a sustainable calendar with specific post ideas, not generic themes.

## When to Use

- "Make me a content calendar for the next month."
- "I want to build in public. What should I post?"
- "Plan content around my launch in three weeks."

Not for: writing the posts themselves (hand off to `project-to-post`, `technical-storyteller`, or `multi-platform-content`).

## Inputs

Required:

1. **Current work**: projects in progress, things being learned, upcoming releases or events.
2. **Time budget**: hours per week realistically available for content.
3. **Platforms**: where they want to post (pick at most 2 to start).
4. **Goal**: job search, project users, personal brand, community.

Helpful: past posts that did well or flopped, upcoming dates (launch, hackathon, talk).

## Workflow

1. **Size the plan to the time budget.** Rough guide: a short social post ≈ 30–45 min, a thread or carousel ≈ 1–2 h, a blog post ≈ 3–6 h. Never plan more than the budget allows. If the user asks for more than fits, say so and propose the trade-off.
2. **Inventory source material.** List every real thing that could become content: features shipped, bugs fixed, things learned, decisions made, tools tried, mistakes. Each item must come from the user's input.
3. **Assign content types** using a mix: *show* (demo/what I built), *teach* (how-to/lesson), *tell* (story/decision), *ask* (question to the community). Avoid more than two of the same type in a row.
4. **Anchor to dates.** Put launch-related posts before and after the launch date. Leave one open slot per week for something unplanned.
5. **Write a one-line brief per slot**: the specific idea, the type, the platform, and which skill to use to draft it.
6. **Add a review checkpoint** at the end of each week or fortnight: what to check and when to adjust.

## Output Format

```
**Budget:** <hours/week> → <N posts/week>
**Platforms:** <...>
**Goal:** <...>

| Week | Day | Platform | Type | Idea (specific) | Draft with |
| ---- | --- | -------- | ---- | --------------- | ---------- |

**Open slots:** <how to use them>
**Review checkpoint:** <date> — check <what>, adjust <how>

**Ideas backlog** (unused source material for later)
- ...
```

## Quality Checklist

- Total estimated hours ≤ the stated budget.
- Every idea refers to something specific from the user's input, not a generic theme like "share a tip".
- No more than 2 platforms unless the user insisted.
- At least one open slot per week.
- Launch dates are respected.

## Safety

- Don't plan posts about unreleased work-related projects unless the user confirms they're allowed to talk about them.
- Don't suggest engagement bait formats (fake polls, "comment YES for the link", controversy for reach).
- The calendar is a plan; do not schedule or publish posts.

## Example

**Input**

> 3 hours a week. LinkedIn and X. I'm building a habit-tracker app in Flutter (auth done, working on offline sync), learning Riverpod, launching a beta on Nov 10. Goal: get 50 beta testers.

**Output (abbreviated)**

**Budget:** 3 h/week → 3 short posts/week (≈ 45 min each) + 45 min buffer.

| Week | Day | Platform | Type | Idea | Draft with |
| --- | --- | --- | --- | --- | --- |
| 1 | Tue | LinkedIn | tell | Why offline sync is the hardest part of a "simple" habit tracker | project-to-post |
| 1 | Thu | X | teach | One Riverpod pattern that clicked for you this week, with a code snippet | multi-platform-content |
| 1 | Sat | X | ask | "What breaks your habit-tracker streaks?" — research for the beta | — |
| 3 | Mon | LinkedIn | show | Beta announcement with sign-up link (Nov 10) | launch-announcement |

**Review checkpoint:** End of week 2 — count beta sign-ups and which post drove them; drop the format that got no response.
