---
name: board
order: 12
tier: core
---
   - /board — Run a real decision past a panel of advisor profiles — experts whose
     thinking I admire, each distilled into a profile note in my vault. For a
     decision I bring, consult each profile and synthesize their distinct takes:
     where they agree, where they'd dissent, and a recommendation. To add or refresh
     an advisor, point me at someone's public work and I build a profile (how they
     think, their heuristics, what they'd push back on). Profiles live under the
     vault (e.g. 03 Areas/Advisors/); grounded only in those curated profiles, no
     external API. Advisory / read-only. Trigger on "/board", "ask the board",
     "what would my advisors say".
<!-- docs -->
## What it does
Runs a real decision past a panel of advisor profiles — experts whose thinking you admire, each distilled into a note in your vault — and synthesizes their distinct takes: where they'd agree, where they'd dissent, and a recommendation.

## When to use it
For a decision worth several sharp perspectives — a hire, a strategy call, a design trade-off. It's advisory and read-only, grounded only in the profiles you've curated (no external lookups).

## Walkthrough
1. Bring a decision — *"ask the board whether to ship the field guide as a second page"*.
2. It consults each advisor profile and gives you each one's distinct take, then a synthesis: agreements, dissents, and a recommendation.
3. To add or refresh an advisor, point it at someone's public work and it builds a profile — how they think, their heuristics, what they'd push back on.

A board run looks about like this:

> **The board on: "ship docs as a second page?"**
> · Advisor A (systems) — yes; keep the main page lean, docs are a separate job
> · Advisor B (growth) — yes, but link it where users hit friction, not just the footer
> · Advisor C (minimalist) — dissents; wary of a second thing to maintain
> **Synthesis** · Strong lean yes; the live risk is maintenance — generate it, don't hand-write.

## Power user
- **It's only as good as the profiles.** Each advisor is a curated note; the richer the profile (heuristics, what they'd challenge), the sharper the take. Build them from real public work.
- **Grounded, not invented.** `/board` reasons only from your profiles — no external API — so it won't fabricate a stance the profile doesn't support.
- **Read-only.** It advises; you decide. Profiles live in your vault (e.g. `03 Areas/Advisors/`) as plain notes you can edit.