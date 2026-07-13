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
     curl/wget, which my safety rules block) to read the current installer build AND its
     outcomes: notes (one-line, cost-phrased summaries of what a change does for me, each
     keyed by build + command + scope) from
     https://raw.githubusercontent.com/cvp1/ai-os/main/core/meta.yml, and the current
     command roster from https://api.github.com/repos/cvp1/ai-os/contents/core/skills
     (one NN-name.md per command; the command name is that file's name without its
     leading number and .md). Compare against MINE: read my build from
     ~/ai-os/.aios-version if it exists, else from the "AI-OS installer build:" line in
     my CLAUDE.md; if neither exists, treat my build as UNKNOWN (an old install
     predating the stamp) and assume I'm behind. Report three things — (a) BUILD: my build
     vs. the current one (if they differ, I'm behind); (b) MISSING COMMANDS: any command
     in the current roster I don't have a skill for under ~/.claude/skills/; (c) WHAT'S NEW
     FOR YOU: for each outcomes note whose build is newer than mine, render its one plain
     sentence so I see what being behind actually COSTS me ("the build you're missing means
     /brief can now …") — but ONLY if that note applies to me: show scope: core notes to
     everyone, and show a scope: optin note ONLY if I actually have that command under
     ~/.claude/skills/ (a note about a command I never installed is not for me — skip it).
     If no newer note applies to me, render NOTHING here — do NOT invent an "all caught up!"
     line (the closing summary already covers a clean bill). NEVER state a capability that
     isn't spelled out in an outcomes note; only ever echo a note verbatim. If I'm
     behind or missing commands, DON'T change anything yourself — if I already have /update
     installed, tell me to say /update and it will fetch, verify, and hand off to upgrade
     mode for me; if update is itself one of my missing commands (I'm crossing this
     threshold for the first time), tell me to re-run the setup prompt manually this one
     time — after that, future updates are one command. Either path detects my existing
     install and switches to UPGRADE MODE: it adds only the missing skills and brings
     memory conventions current, and leaves
     my memories, notes, CLAUDE.md, and customized skills UNTOUCHED. If I can't reach the
     internet (or the fetch is unavailable here), say "couldn't check currency — offline"
     and move on; NEVER let this stop the rest of the check, and NEVER guess a version
     you couldn't read. (6) STANDING WORK — if I've put any of my managers on a schedule (a
     between-session "check-in" that drafts something while I'm away), confirm it's actually
     still running. Read ~/ai-os/.aios-heartbeat.jsonl if it exists (one JSON line per run:
     ts, job, status, every, note). For each distinct job take its LATEST record, and FLAG it
     if either (a) its status is "error", or (b) the time since its ts exceeds its own expected
     cadence `every` by more than about half again (so a "7d" job is stale past ~10 days) —
     which means a scheduled run may be failing SILENTLY (a sleeping laptop skips runs, a
     deleted routine stops them, an errored run leaves no draft), and that is worse than no
     automation because I THINK it's still happening. For a flagged job say plainly: "your
     <job> standing work hasn't run since <date> (expected every <every>) — open your Scheduled
     sessions or re-check that routine." For a healthy job, one green line: when it last ran and
     whether a draft is waiting. If the file is missing or empty, render NOTHING here (I simply
     have no standing work registered — do not invent a line). Strictly READ-ONLY: never re-run
     a job, never re-authorize, never restart a routine — detect, report, and point me at the
     fix. If a counter file ~/ai-os/.aios-usage.jsonl exists, append one aggregate
     "heartbeat_stale" event per flagged job — counts only, no content. Then, for the deeper SYSTEM layer — install health, connector CONFIG
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
2. It checks the six things the platform's own checker can't see: **Connectors** (via `/mcp` — the thing most likely to be quietly broken), **Memory** (exists, rough size, note count, whether a `/memory-prune` is worth it), **Toolkit** (which skills are registered under `~/.claude/skills/`), **Protection** (the age of your most recent `/backup`), **Currency** (whether your installer build and command roster have fallen behind the current AI-OS — if so, it points you at re-running setup, which upgrades in place), and **Standing work** (if you've scheduled a manager to draft between sessions, whether it's actually still running — a silently-skipped run is worse than none).
3. It finishes with a short green / needs-attention summary naming the one or two things worth doing next — and points you to Claude Code's own built-in `/doctor` for the deeper system layer (install, versions, config).

A checkup looks about like this:

> **/doctor** · AI-OS health
> ✓ Connectors — Google signed in · Memory — 84 notes (~180 KB), healthy
> ⚠ Toolkit — 16 of 17 skills registered (/expenses needs a fresh session)
> ⚠ Protection — last backup 9 days ago → run /backup
> ⚠ Currency — build 2026.05.12a is behind current 2026.06.30m; missing /restore, /update → re-run setup once to catch up (it upgrades in place, adds only what's new) — after that, /update does this for you
> &nbsp;&nbsp;What's new for you — the newer build's /brief now drafts your morning digest before you're even at your desk
> ⚠ Standing work — your /projects check-in hasn't run since Jul 1 (expected weekly) → check its routine (a sleeping laptop skips runs)
> For install/version checks, run Claude Code's built-in /doctor.

## Power user
- **Connectors are the usual culprit.** A signed-out connector is the most common quiet failure; `/doctor` reads live auth via `/mcp` and points you to re-authorize.
- **"My command does nothing."** Usually the skill isn't registered yet — `/doctor` shows the count; start a fresh session to register newly-built ones.
- **It complements native `/doctor`, doesn't replace it.** AI-OS `/doctor` covers AI-OS-specific state; Claude Code's built-in `/doctor` covers install/config/versions. Run both.
- **Currency routes, it never upgrades.** `/doctor` only *tells* you your build or command roster is behind; if you have `/update`, say it and it fetches, verifies, and hands off to the same upgrade mode automatically — if you don't have `/update` yet, re-paste the setup prompt manually once (upgrade mode detects your install, adds only what's missing, leaves your memories, notes, and customized skills untouched). `/doctor` itself changes nothing, and if you're offline it just skips the currency check.
- **Strictly read-only.** It inspects and reports — pair it with `/backup` (it tells you your safety net is current) and `/memory-prune` (it tells you when one's due).
- **Standing work can fail silently — this catches it.** If you've scheduled a manager to draft between sessions (the "Run it without you" setup), `/doctor` reads a small heartbeat file and tells you if a scheduled run has quietly stopped — a sleeping laptop, a deleted routine, an errored run. It only reports and points you at the fix; it never re-runs or restarts anything.
