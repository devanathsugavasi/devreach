# Before and After

> Illustrative examples based on the fictional project in [`sample-project.md`](sample-project.md). "After" versions are the kind of output the skills aim for; your results will vary.

## LinkedIn post (`project-to-post`)

**Before** — what people usually write:

> 🚀 Thrilled to announce my new open-source project quietlog! 🚀 It's a game-changing Python library that leverages cutting-edge techniques to keep your logs secure. Check it out and give it a star! ⭐ #Python #Security #OpenSource #AI #Tech #Coding

**After:**

> A Stripe key once ended up in our team's log service because of one `logger.info(request.url)`.
>
> That's why I built quietlog — a small Python library that removes secrets from log messages before they're written. It wraps the standard `logging` module, so existing code doesn't change.
>
> The hard part wasn't detecting secrets; it was *not* detecting things that look like secrets. My first regex version flagged every UUID and commit hash. What fixed it was combining an entropy check with context: a high-entropy string next to a key name like `token=` is far more likely to be real.
>
> It currently recognizes 14 patterns and adds about 4 µs per log call in my benchmark.
>
> I'm looking for teams willing to try it in a real service and tell me what it misses. If your logs have ever leaked something, I'd especially like to hear what it was (without the secret 🙂).

Why it's better: specific hook, a real story, one technical insight, numbers from the author's own facts, a specific ask, no hype.

## GitHub profile line (`developer-profile`)

**Before:** "Passionate developer | Python | Security enthusiast | Open to opportunities"

**After:** "Backend Python developer · I build tools that make logs safer · Author of quietlog (secret redaction for Python logging)"

## Community post title (`community-launch`)

**Before (same title everywhere):** "Check out my new library quietlog!"

**After:**
- *Show HN:* "Show HN: Quietlog – Strip secrets from Python log messages before they're written"
- *r/Python:* "I wrote a logging filter that redacts API keys — how do you handle false positives on UUIDs?"
