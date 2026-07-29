---
name: weekly
order: 8
tier: core
---
   - /weekly — Generate my recurring status / progress update from project notes +
     recent activity, in my voice and format. Draft only; I send it.
     ONCE PER CALENDAR MONTH (the first /weekly of a new month, or on demand via
     "/weekly sharper"), also render a "SHARPER THIS MONTH" block — a short mirror of
     how you got sharper at MY work, not a recap of what you did. Show ONLY things
     idiosyncratic to me (a rule, a voice habit, a "never" from ~/ai-os/me/HOW-I-WORK.md)
     — NOT generic good-assistant behavior (leading with the conclusion, clean prose,
     honest trade-offs): the base model already does those, so they are not compounding.
     Up to three kinds of moment, each shown ONLY if real AND proven:
       (a) ABSORBED — a correction that became a standing rule in HOW-I-WORK.md THIS
           period (it carries an `added:` date in the window) AND that you have since
           applied at least once in a later session. Capture alone does not count — the
           rule must have done work.
       (b) SYNTHESIZED — a standing rule you PROPOSED from a repeated pattern of mine
           (it carries `origin: synthesized` in HOW-I-WORK.md) that I accepted THIS
           period AND have not since deleted or rewritten. Show it only if it is still
           present and provenanced; a proposal I rejected or later reverted does not
           count.
       (c) FRONTIER — a newly-available capability, quoted VERBATIM from the /aios-doctor
           CURRENCY outcomes notes, that helps a specific thing I actually do (match it
           against my me/WHOAMI.md + recent activity). Never invent a capability; skip it
           if it doesn't map to something real of mine.
     EARN, DON'T NAG: if there is not at least ONE qualifying, proven moment, render
     NOTHING for this block — no "all quiet", no "nothing new", no placeholder. Silence
     is the default. Never render it more than once per calendar month. This is a MIRROR
     I meet because I chose to run /weekly — never a notification, never between-session,
     never a feed. It only READS me/ and memory; it NEVER writes a rule (that stays
     /improve's job, on my explicit OK). If you cannot confidently tell a real divergent
     moment from generic competence, stay SILENT rather than fabricate one. If a counter
     file ~/ai-os/.aios-usage.jsonl exists, append an aggregate event ("mirror_shown",
     and "mirror_engaged" if I act on it) — counts only, never any content.
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
>
> **Sharper this month** (monthly) · You corrected status-update openings 3× → now a
> standing rule, applied to the last two drafts without a fix · /prep now pulls the
> attendee's last email thread — useful for your Monday 1:1s

## Power user
- **"Sharper this month" — the compounding mirror.** Once a month, `/weekly` adds a short mirror of how the system got sharper *at your work* — the corrections it turned into standing rules and has since applied, and (when relevant) a new capability that helps something you actually do. It shows the *change*, not a list of what it knows. It stays completely silent any month it has nothing real to show — it's a mirror, never a nag. Run it on demand any time with `/weekly sharper`.
- **`/weekly` vs `/status-update`.** `/weekly` is the whole-week rollup for your standing review; `/status-update` is a single project on demand. Because `/weekly` bundles a status draft, many people run only `/weekly` on Fridays.
- **It reflects what you captured.** The review is as complete as your week's notes — jot decisions and progress as they happen (or with `/improve`) and Friday's draft writes itself.
- **Automate it.** Pair `/weekly` with a scheduled task (see the [scheduler second act](index.html#autopilot) on the setup page) to have Friday's review waiting — mind the reliability and cost caveats there; a machine that's asleep silently skips the run.
- **Keep your format.** Correct the first one's shape and tone, then run `/improve`, and it matches your recurring format from then on.