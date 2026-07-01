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
     /backup. (5) CURRENCY — check whether my AI-OS itself has fallen behind the
     current product. If I can reach the internet, use the WebFetch tool (NOT a shell
     curl/wget, which my safety rules block) to read the current installer build from
     https://raw.githubusercontent.com/cvp1/ai-os/main/core/meta.yml and the current
     command roster from https://api.github.com/repos/cvp1/ai-os/contents/core/skills
     (one NN-name.md per command; the command name is that file's name without its
     leading number and .md). Compare against MINE: read my build from
     ~/ai-os/.aios-version if it exists, else from the "AI-OS installer build:" line in
     my CLAUDE.md; if neither exists, treat my build as UNKNOWN (an old install
     predating the stamp) and assume I'm behind. Report two things — (a) BUILD: my build
     vs. the current one (if they differ, I'm behind); (b) MISSING COMMANDS: any command
     in the current roster I don't have a skill for under ~/.claude/skills/. If I'm
     behind or missing commands, DON'T change anything yourself — tell me to re-run the
     setup prompt, which will detect my existing install and switch to UPGRADE MODE:
     it adds only the missing skills and brings memory conventions current, and leaves
     my memories, notes, CLAUDE.md, and customized skills UNTOUCHED. If I can't reach the
     internet (or the fetch is unavailable here), say "couldn't check currency — offline"
     and move on; NEVER let this stop the rest of the check, and NEVER guess a version
     you couldn't read. Then, for the deeper SYSTEM layer — install health, connector CONFIG
     validity, version currency, search/ripgrep, CLAUDE.md size — tell me to run Claude
     Code's own built-in /doctor (if it's available here); don't reinvent that plumbing,
     just point at it. Finish with a short green / needs-attention summary naming the
     one or two things worth doing next. Build it as a Claude Code skill, strictly
     READ-ONLY (inspect and report only). Pairs with /backup: /doctor tells me my
     safety net is current. Trigger on "/doctor", "is my AI-OS healthy / okay", "health
     check", "check my system / check my connectors", "am I up to date",
     "any AI-OS updates", "is my AI-OS current".

<!-- docs -->
## What it does
A read-only checkup for your system — are your connectors still signed in, your memory and commands healthy, your last backup recent, and is your AI-OS itself up to date? It reports what needs attention and points you at the fix; it changes nothing.

## When to use it
Any time something feels off — a command "does nothing", mail looks stale — or as a periodic once-over. It's strictly inspect-and-report: it never changes, deletes, or sends anything.

## Walkthrough
1. Type `/doctor`.
2. It checks the five things the platform's own checker can't see: **Connectors** (via `/mcp` — the thing most likely to be quietly broken), **Memory** (exists, rough size, note count, whether a `/memory-prune` is worth it), **Toolkit** (which skills are registered under `~/.claude/skills/`), **Protection** (the age of your most recent `/backup`), and **Currency** (whether your installer build and command roster have fallen behind the current AI-OS — if so, it points you at re-running setup, which upgrades in place).
3. It finishes with a short green / needs-attention summary naming the one or two things worth doing next — and points you to Claude Code's own built-in `/doctor` for the deeper system layer (install, versions, config).

A checkup looks about like this:

> **/doctor** · AI-OS health
> ✓ Connectors — Google signed in · Memory — 84 notes (~180 KB), healthy
> ⚠ Toolkit — 16 of 17 skills registered (/expenses needs a fresh session)
> ⚠ Protection — last backup 9 days ago → run /backup
> ⚠ Currency — build 2026.05.12a is behind current 2026.06.30m; missing /restore → re-run setup (it upgrades in place, adds only what's new)
> For install/version checks, run Claude Code's built-in /doctor.

## Power user
- **Connectors are the usual culprit.** A signed-out connector is the most common quiet failure; `/doctor` reads live auth via `/mcp` and points you to re-authorize.
- **"My command does nothing."** Usually the skill isn't registered yet — `/doctor` shows the count; start a fresh session to register newly-built ones.
- **It complements native `/doctor`, doesn't replace it.** AI-OS `/doctor` covers AI-OS-specific state; Claude Code's built-in `/doctor` covers install/config/versions. Run both.
- **Currency routes, it never upgrades.** `/doctor` only *tells* you your build or command roster is behind and points you at re-running the setup prompt — which detects your install and switches to upgrade mode, adding only what's missing and leaving your memories, notes, and customized skills untouched. `/doctor` itself changes nothing, and if you're offline it just skips the currency check.
- **Strictly read-only.** It inspects and reports — pair it with `/backup` (it tells you your safety net is current) and `/memory-prune` (it tells you when one's due).
