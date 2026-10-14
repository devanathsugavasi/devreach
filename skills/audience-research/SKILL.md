---
name: audience-research
description: Defines who a developer project or personal brand is for — audience segments, their real problems, where they gather, and a positioning statement — using only evidence the user supplies. Use whenever a developer asks who their project is for, how to position it, why it gets no traction, how it compares to alternatives, or wants user-interview questions or market statistics.
---

# Audience Research

## Purpose

"It's for developers" is not an audience. Projects get traction when they are clearly for a specific group with a specific problem. This skill helps the user separate what they *know* about their audience from what they *assume*, write a positioning statement from the evidence, and plan the cheapest way to test the assumptions.

## When to Use

- "Who is my project actually for?"
- "My launch got no traction. Am I targeting the wrong people?"
- "Help me position my library against alternatives."
- "Write interview questions for potential users."

Not for: analyzing metrics after launch (use `growth-review`).

## Inputs

Required:

1. **The project or offering**: what it does.
2. **Any evidence about users**: issues, comments, DMs, survey answers, support questions, who starred/forked, conversations. "None yet" is a valid answer.

Helpful: alternatives users currently use, the user's own reason for building it.

## Workflow

1. **Sort evidence** into *observed* (someone said or did it) and *assumed* (the user believes it). Quote observed evidence directly.
2. **Propose 2–4 segments.** For each: who they are (role + situation), the problem in their words, what they use today, why they'd switch, and where they gather online. Mark every field as observed or assumed.
3. **Pick a primary segment** — the one with the strongest observed evidence and the most painful problem — and explain the choice.
4. **Write a positioning statement**: "For <segment> who <problem>, <project> is a <category> that <key benefit>. Unlike <alternative>, it <differentiator>." Note which parts are assumptions.
5. **Plan the cheapest tests** for the riskiest assumptions: 5 user conversations, a question in a community, a landing-page sentence change. For conversations, write 5–8 non-leading interview questions about past behavior, not opinions about the project.
6. **Return the research doc.**

## Output Format

```
**Evidence**
| Source | Quote / observation | Observed or assumed |

**Segments**
| Segment | Problem (their words) | Current alternative | Where they are | Evidence strength |

**Primary segment:** <...> — <why>

**Positioning statement**
<statement>
Assumptions in this statement: <...>

**Riskiest assumptions and tests**
| Assumption | Test | Signal that confirms / disproves |

**Interview questions**
1. ...
```

## Quality Checklist

- Every segment field is marked observed or assumed.
- The primary segment is chosen on evidence, not size.
- Interview questions ask about past behavior ("Tell me about the last time you…"), not hypotheticals ("Would you use…").
- Positioning names a real alternative, including "doing it manually" if that's the truth.

## Safety

- Do not invent survey results, user quotes, or market-size numbers. Present any external statistic only if the user supplied it with a source.
- Do not suggest collecting personal data from users without consent, or scraping profiles.
- Anonymize user quotes (no names or handles) in the output unless the user says they're public.

## Example

**Input**

> Project: `logtrim`, a CLI that strips noise from CI logs so you see the actual failure. Evidence: 3 GitHub issues from people using GitHub Actions with monorepos; one Reddit comment "this would save me 10 minutes per failed build on our Nx repo"; I built it because our Jenkins logs are 20k lines.

**Output (abbreviated)**

**Primary segment:** Developers maintaining CI for JavaScript/TypeScript monorepos on GitHub Actions — 4 of 4 external signals come from this group. Jenkins users are the founder's own case only (assumed).

**Positioning statement**
For developers debugging failed CI runs in large monorepos, logtrim is a CLI that shows only the lines that explain the failure. Unlike scrolling raw logs or searching for "error", it understands common tool output formats and hides the noise.
Assumptions: "understands common tool output formats" — confirm which tools it actually supports.

**Interview questions**
1. Tell me about the last CI failure you debugged. How long did it take to find the cause?
2. What did you do first when you opened the log?
3. What have you tried to make that faster?
