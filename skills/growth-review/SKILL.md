---
name: growth-review
description: Analyzes a project's or creator's supplied metrics and feedback — GitHub stars, traffic, clones, installs, post analytics, issues, comments — to explain what is and isn't working and recommend 1–3 small experiments. Use for a weekly or post-launch review when a developer wants to decide what to do next based on data rather than guesses.
---

# Growth Review

## Purpose

Developers check star counts and post likes but rarely connect them to decisions. This skill reads the numbers and feedback the user provides, separates signal from noise (small numbers are noisy), and turns the review into a short list of experiments with a clear way to tell whether each one worked.

## When to Use

- "Here are my GitHub traffic stats for the last two weeks. What's working?"
- "My launch got 300 stars and no issues. What does that mean?"
- "Do a weekly review of my LinkedIn posts."

Not for: defining the audience from scratch (use `audience-research`).

## Inputs

Required:

1. **Metrics with time periods**: e.g. GitHub Insights → Traffic (views, unique visitors, clones, referrers, popular content), stars over time, package downloads, post impressions/reactions/comments, sign-ups.
2. **What happened in the period**: posts published, launches, releases, changes.
3. **The goal**: users, contributors, job leads, sign-ups.

Helpful: qualitative feedback (comments, issues, DMs), previous review results.

## Workflow

1. **Check the data.** List each metric, its period, and whether it's enough to conclude anything. With very small counts (e.g. under ~30 events), say that differences are likely noise.
2. **Line up events against metrics.** Which posts, releases, or referrers line up with changes? Say "coincides with", not "caused", unless there's direct evidence (e.g. referrer data).
3. **Find the funnel leak.** For repos: referrer → page views → README read → clone/install → issue/contribution. For posts: impressions → engagement → profile/link clicks → goal. Identify the step with the largest drop where the user has evidence.
4. **Read the qualitative feedback** and group it into themes. One detailed issue can outweigh a hundred stars.
5. **Recommend 1–3 experiments.** Each: hypothesis, change to make, metric to watch, how long to run it, what result would count as success. Prefer changes that are cheap and reversible.
6. **Note what to stop doing** if the data clearly shows something isn't working.

## Output Format

```
**Data quality**
| Metric | Period | Value | Enough to conclude? |

**What the data shows**
- <finding> — <evidence> — <confidence: high / medium / low>

**Biggest leak:** <funnel step> — <evidence>

**Feedback themes**
- <theme> (<n> mentions) — "<anonymized quote>"

**Experiments**
| # | Hypothesis | Change | Metric | Duration | Success looks like |

**Stop doing:** <...>
```

## Quality Checklist

- No causal claims without direct evidence.
- Small-sample findings are labeled low confidence.
- Each experiment has one metric and a success threshold set before running it.
- At most 3 experiments.
- Recommendations connect to the user's stated goal, not vanity metrics.

## Safety

- Do not invent or estimate missing metrics. Ask for them or note they're missing.
- Do not recommend buying stars, followers, or engagement, or using automation to inflate numbers.
- Anonymize feedback quotes.

## Example

**Input**

> Repo, last 14 days: 2,140 views, 1,310 unique visitors, 95 clones (41 unique), stars 12 → 188. Referrers: news.ycombinator.com 1,050 views, reddit.com 410, github.com 300. Launched Show HN on day 3. 2 issues opened, both "install fails on Windows". Goal: active users.

**Output (abbreviated)**

**What the data shows**
- The HN launch drove most traffic (1,050 of 2,140 views) — high confidence (referrer data).
- Only 41 unique cloners out of 1,310 unique visitors (~3%) — medium confidence; clones also include CI and bots.
- Both issues report Windows install failure — small sample, but 100% of reported problems.

**Biggest leak:** Visitor → successful install. Windows failures may be silently losing users who don't file issues.

**Experiments**
| # | Hypothesis | Change | Metric | Duration | Success |
| --- | --- | --- | --- | --- | --- |
| 1 | Windows users fail to install and leave | Fix Windows install, add a Windows CI job, note it in README | Install-related issues; unique clones | 2 weeks | No new Windows install issues; unique clones/visitor ratio ≥ current |

**Stop doing:** Nothing yet — only one launch event to learn from.
