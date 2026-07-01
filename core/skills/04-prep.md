---
name: prep
order: 4
tier: core
---
   - /prep — Prep me for a specific meeting (client call, team sync, 1:1): pull the
     invite, related mail/threads, the relevant project + people notes, last
     decisions and open items, and produce an agenda + talking points + likely
     questions.
<!-- docs -->
## What it does
Everything you need for one specific meeting, gathered onto a single page — the invite, the relevant mail thread, your project and people notes, the last decisions and open items — plus a ready-made agenda, talking points, and the questions you're likely to get.

## When to use it
Right before a meeting you want to walk into sharp: a client call, a team sync, a 1:1. It's read-only — it pulls together what already exists and drafts an agenda; it sends and changes nothing.

## Walkthrough
1. Type `/prep` and name the meeting — *"/prep my 2pm with the design team"* or *"prep me for the Acme call"*.
2. It finds the calendar invite, pulls the related mail thread, and reads your project and people notes — last decisions, open items, who's attending.
3. It hands you a one-page pack — **Context**, **Attendees**, **Agenda**, **Talking points**, **Likely questions** — that you can edit, or ask it to turn into a follow-up afterward.

A prep looks about like this:

> **Acme quarterly review · Thu 14:00 · 3 attendees**
> **Context** · Renewal is up in 6 weeks; last call they raised onboarding friction
> **Attendees** · Dana (their VP), Chen (their PM), you
> **Agenda** · 1) Onboarding fixes shipped · 2) Q3 roadmap · 3) Renewal terms
> **Talking points** · Support tickets down 40% since the March fix · SSO ships next sprint
> **Likely questions** · "What's the SLA on the migration?" · "Can we add three seats mid-term?"

## Power user
- **Be specific about which meeting.** If two invites could match, name the time or the person — *"/prep the 2pm, not the 4pm"*. The more precise the pointer, the tighter the pack.
- **It's only as sharp as your notes.** `/prep` reads your project and people notes; the more current those are, the better it briefs you. `/status` and your vault feed it.
- **Chain it after `/brief` or `/triage`.** Both surface meetings — say *"prep me for that one"* and `/prep` takes over.
- **Ask for the follow-up.** After the meeting, *"draft the recap from the prep"* turns the same context into a follow-up email — drafted locally, sent only on your OK.
- **Missing context?** Tell it what it overlooked and run `/improve` so it looks in the right place next time.