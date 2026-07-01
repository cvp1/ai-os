---
name: brief
order: 3
tier: core
---
   - /brief — A morning brief: today's meetings (with prep + who's attending),
     what's waiting on me, top priorities pulled from my project notes, and anything
     due this week. Read-only; concise.
<!-- docs -->
## What it does
Your morning brief — today's meetings and who's in them, what's waiting on you, your top priorities, and what's due this week, all on one screen.

## When to use it
First thing, before your first call — instead of opening five tabs to reconstruct your day. It's also a good midday reset. Because `/brief` is read-only, it's the safest command to run anytime: nothing it does can send, post, or change a thing.

## Walkthrough
1. Type `/brief`.
2. It reads your calendar and inbox from the fast local cache, plus your project notes, and prints four short sections: **Meetings** (with who's attending and a one-line prep), **Waiting on you**, **Priorities**, and **Due this week**.
3. Point at anything in it. Say *"prep me for the 2pm"* and it hands off to `/prep`; say *"draft a reply to the first one"* and it drafts locally — never sends.

A brief looks about like this:

> **Tue 30 Jun**
> **Meetings** · 10:00 Design sync (4 people) — last decision: ship the compare table below the fold · 14:00 1:1 w/ Sam — you owe them the Q3 roadmap
> **Waiting on you** · Reply to Finance re: budget (2 days) · Approve the vendor SOW
> **Priorities** · Website redesign — copy pass · Hiring — close the PM loop
> **Due this week** · Board deck (Thu)

## Power user
- **Scope it.** *"/brief just my meetings"* or *"/brief for tomorrow"* narrows the run to what you need.
- **Sharpen "priorities."** `/brief` pulls them from your project notes — the more you keep those current (with `/status` and your vault), the better it reads your actual day rather than guessing.
- **Automate it.** Pair `/brief` with a scheduled task (see the scheduler "second act" on the setup page) to have a brief waiting each morning — mind the reliability and cost caveats there; a machine that's asleep at 7am silently skips the run.
- **Stale data?** If meetings or mail look out of date, your connector may have signed out. Run `/doctor` to check, or re-authorize in your connector settings — the cache refreshes when something changes, not on a fixed timer.
- **It never writes to memory.** If `/brief` got a priority wrong, tell it, then run `/improve` to make the correction stick for next time.