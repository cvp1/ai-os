---
name: doctor
order: 17
tier: core
---
   - /doctor — A quick READ-ONLY "is my AI-OS healthy?" check I can run any time: it
     inspects and reports, and must NEVER change, delete, or send anything. Cover the
     AI-OS-specific state that the platform's own checker can't see: (1) CONNECTORS —
     run /mcp and report which mail/calendar connector is signed in vs. needs a fresh
     sign-in; this is the thing most likely to be quietly broken, and /mcp shows the
     live auth, so if one needs sign-in point me to re-authorize it. (2) MEMORY —
     confirm ~/ai-os/memory/ exists, report its rough size and how many notes it holds,
     and flag if it's grown big enough that a /memory-prune is worth running. (3)
     TOOLKIT — count and list the skills installed under ~/.claude/skills/ so I can see
     my commands are all registered (if one I expect is missing, that's why it "does
     nothing" — start a fresh session to register newly-built ones). (4) PROTECTION —
     if ~/ai-os/backups/ exists, report the age of my most recent /backup so a stale or
     missing backup is visible; if there's no backup yet, say so and suggest running
     /backup. Then, for the deeper SYSTEM layer — install health, connector CONFIG
     validity, version currency, search/ripgrep, CLAUDE.md size — tell me to run Claude
     Code's own built-in /doctor (if it's available here); don't reinvent that plumbing,
     just point at it. Finish with a short green / needs-attention summary naming the
     one or two things worth doing next. Build it as a Claude Code skill, strictly
     READ-ONLY (inspect and report only). Pairs with /backup: /doctor tells me my
     safety net is current. Trigger on "/doctor", "is my AI-OS healthy / okay", "health
     check", "check my system / check my connectors".

<!-- docs -->
## What it does
A read-only checkup for your system — are your connectors still signed in, your memory and commands healthy, your last backup recent? It reports what needs attention and points you at the fix; it changes nothing.

## When to use it
Any time something feels off — a command "does nothing", mail looks stale — or as a periodic once-over. It's strictly inspect-and-report: it never changes, deletes, or sends anything.

## Walkthrough
1. Type `/doctor`.
2. It checks the four things the platform's own checker can't see: **Connectors** (via `/mcp` — the thing most likely to be quietly broken), **Memory** (exists, rough size, note count, whether a `/memory-prune` is worth it), **Toolkit** (which skills are registered under `~/.claude/skills/`), and **Protection** (the age of your most recent `/backup`).
3. It finishes with a short green / needs-attention summary naming the one or two things worth doing next — and points you to Claude Code's own built-in `/doctor` for the deeper system layer (install, versions, config).

A checkup looks about like this:

> **/doctor** · AI-OS health
> ✓ Connectors — Google signed in · Memory — 84 notes (~180 KB), healthy
> ⚠ Toolkit — 16 of 17 skills registered (/expenses needs a fresh session)
> ⚠ Protection — last backup 9 days ago → run /backup
> For install/version checks, run Claude Code's built-in /doctor.

## Power user
- **Connectors are the usual culprit.** A signed-out connector is the most common quiet failure; `/doctor` reads live auth via `/mcp` and points you to re-authorize.
- **"My command does nothing."** Usually the skill isn't registered yet — `/doctor` shows the count; start a fresh session to register newly-built ones.
- **It complements native `/doctor`, doesn't replace it.** AI-OS `/doctor` covers AI-OS-specific state; Claude Code's built-in `/doctor` covers install/config/versions. Run both.
- **Strictly read-only.** It inspects and reports — pair it with `/backup` (it tells you your safety net is current) and `/memory-prune` (it tells you when one's due).
