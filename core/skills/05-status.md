---
name: status
order: 5
tier: core
---
   - /status — Draft a status update from my project notes + recent activity: what
     progressed, what's blocked, decisions needed, next steps. Uses my template and
     my tone (with separate external vs internal versions if I asked for both). Draft
     only.
<!-- docs -->
## What it does
A ready-to-edit status update drafted from your project notes and recent activity — what progressed, what's blocked, decisions needed, and next steps — written in your template and your tone.

## When to use it
Whenever you owe someone an update — a project check-in, a stakeholder note — and don't want to start from a blank page. It drafts only; you review and send.

## Walkthrough
1. Type `/status` and name the project — *"/status for the website redesign"*.
2. It reads that project's notes and recent activity and drafts an update: **Progress**, **Blocked**, **Decisions needed**, **Next steps**.
3. It writes in your tone and format — and if you keep separate external and internal versions, it can draft both. Edit and send; nothing goes out on its own.

A status draft looks about like this:

> **Website redesign — status · week of 30 Jun**
> **Progress** · Compare table moved below the fold; hero copy pass done
> **Blocked** · Waiting on legal sign-off for the new privacy page
> **Decisions needed** · Ship the field guide as a second page? (recommend yes)
> **Next steps** · Author the remaining command pages; QA the mobile nav

## Power user
- **Tune the register.** Ask for *"a polished external version"* or *"a direct internal one"* — or both at once if you write for two audiences.
- **It leans on your notes.** `/status` drafts from what's captured, so the more you note decisions and progress as you go, the less you edit. Run `/recall` first to see what it'll find.
- **`/status` vs `/weekly`.** `/status` is one project on demand; `/weekly` rolls up everything for your recurring review (and includes a status update of its own).
- **Save your template once.** Correct the first draft's shape and tone, then run `/improve` — after that, `/status` matches your format by default.