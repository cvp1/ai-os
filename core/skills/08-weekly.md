---
name: weekly
order: 8
tier: core
---
   - /weekly — Generate my recurring status / progress update from project notes +
     recent activity, in my voice and format. Draft only; I send it.
<!-- docs -->
## What it does
Your recurring weekly review, pre-built — what shipped, the decisions, what slipped or is blocked, and the shape of next week — plus a ready-to-edit status update to send.

## When to use it
End of the week — Friday, or whenever you do your review. Instead of reconstructing the week from memory, you start from a draft that's already assembled. Draft only; you send it.

## Walkthrough
1. Type `/weekly`.
2. It reads your project notes and the week's activity and assembles the review: **Shipped**, **Decisions**, **Slipped / blocked**, **Next week**.
3. It also drafts your recurring status update in your voice and format, ready to edit and send.

A weekly review looks about like this:

> **Weekly review · week of 30 Jun**
> **Shipped** · Field Guide pilot live · Compare table repositioned · Connector-auth refresh
> **Decisions** · Grew AI-OS to a second public page (the guide)
> **Slipped / blocked** · Long-tail command docs (11 remaining) · Privacy page (legal)
> **Next week** · Author remaining command pages · Recruit the novice test

## Power user
- **`/weekly` vs `/status`.** `/weekly` is the whole-week rollup for your standing review; `/status` is a single project on demand. Because `/weekly` bundles a status draft, many people run only `/weekly` on Fridays.
- **It reflects what you captured.** The review is as complete as your week's notes — jot decisions and progress as they happen (or with `/improve`) and Friday's draft writes itself.
- **Automate it.** Pair `/weekly` with a scheduled task (see the scheduler "second act" on the setup page) to have Friday's review waiting — mind the reliability and cost caveats there; a machine that's asleep silently skips the run.
- **Keep your format.** Correct the first one's shape and tone, then run `/improve`, and it matches your recurring format from then on.