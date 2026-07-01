---
name: triage
order: 2
tier: core
---
   - /triage — One pass over my inbox + calendar. Classify mail into Needs Reply /
     FYI / Noise, surface calendar conflicts and free blocks, and ONLY on explicit
     request draft replies, flag, or propose calendar changes. Read-only by default;
     respects my "never without approval" rules.
<!-- docs -->
## What it does
One pass over your inbox and calendar that sorts the noise for you — mail bucketed into Needs Reply / FYI / Noise, plus your calendar conflicts and free blocks — so you start from a triaged list instead of a full inbox.

## When to use it
Monday morning, or any time the inbox has gotten ahead of you. Like `/brief` it's read-only by default: it reads and sorts, and only drafts a reply, flags a message, or proposes a calendar change when you explicitly ask — and never sends or moves anything without your OK.

## Walkthrough
1. Type `/triage` (or say *"/triage my inbox"*).
2. It reads your inbox and calendar from the fast local cache and returns three mail buckets — **Needs Reply**, **FYI**, and **Noise** — plus a calendar read: conflicts and your free blocks.
3. Act on any line: *"draft replies to the Needs Reply ones"* (it drafts locally, never sends), *"flag the second one"*, or *"find me an hour for the Acme call"* — each waits for your approval.

A triage looks about like this:

> **Needs Reply (3)** · Finance — Q3 budget sign-off (2 days) · Sam — roadmap review, wants a time · Legal — vendor SOW redlines
> **FYI (5)** · Two newsletters, release notes, an all-hands recap, a calendar invite
> **Noise (11)** · Promotions and automated notifications — safe to skip
> **Calendar** · Conflict: 14:00 1:1 overlaps the design sync · Free: 09:00–10:00, after 15:30

## Power user
- **Ask for the actions explicitly.** Triage never sends, flags, or moves anything on its own — say *"draft the replies"* or *"propose a new time for the conflict"* and it drafts or proposes for your approval (the same propose-only discipline as everywhere else).
- **Pair it with `/brief`.** `/brief` gives you the day; `/triage` clears the inbox behind it. A common rhythm is `/brief` first thing, then `/triage` to work the pile down.
- **Hand off to `/prep`.** When triage surfaces a meeting you're not ready for, say *"prep me for that one"* and it hands the details to `/prep`.
- **Teach it your buckets.** If it keeps mis-sorting a sender — a VIP landing in Noise, say — correct it and run `/improve` so the rule sticks. Triage gets more "you" over time.
- **Stale inbox?** If mail looks out of date, your connector may have signed out — run `/doctor`, or re-authorize in your connector settings.