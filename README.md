<div align="center">

# 🧭 AI OS for Claude Code

**Turn [Claude Code](https://claude.com/claude-code) into a chief-of-staff that remembers your work, knows your calendar, and gets sharper every time you correct it.**

A persistent memory · a structured notes vault · a toolkit of slash-commands — wired to your **Microsoft 365 or Google Workspace**, and built around *you* in about five minutes.

### [▶︎ Open the walkthrough →](https://cvp1.github.io/ai-os/)

</div>

---

## What this is

A single self-contained page (`index.html`) with an embedded, copy-paste **setup prompt**. You paste it into a fresh Claude Code session; it **interviews you** about your role, then builds a personal "AI operating system" shaped to how you actually work — and explains each piece in plain language as it goes.

No code. No config files to edit. If you can use email and a calendar, you can use this.

## Why you'd want it

- **It keeps your memory true.** Claude Code remembers across sessions — this keeps that memory honest: it re-checks what's gone stale, removes duplicates, resolves contradictions, and links related facts, so what it knows about your projects and people stays trustworthy instead of drifting.
- **It's wired to your real work.** Commands read from your live mail & calendar — Microsoft 365 or Google Workspace — not a generic chatbot guess.
- **It's in your hands.** Read-only by default — it drafts and proposes; nothing is sent, posted, or accepted without your explicit OK, every time.
- **It gets more "you."** Correct it once, run `/improve`, and the lesson sticks.

## Quickstart — about 5 minutes

| # | Step |
|---|------|
| 1 | Install **Claude Code** and sign in. *(Claude Code runs on a paid Claude plan — Pro is ~$20/mo. This template is free; the runtime that powers it isn't.)* |
| 2 | Connect your mail & calendar — the **Microsoft 365** *or* **Google (Gmail + Calendar)** connector (the prompt can walk you through it). |
| 3 | Open a Claude Code session in a folder you want as your home — e.g. `~/ai-os`. |
| 4 | Open the [walkthrough](https://cvp1.github.io/ai-os/), copy the setup prompt, and paste it as your first message. |
| 5 | Answer the interview. Claude builds everything and tells you what to try first. |

## What gets built

**🧠 A maintained memory** — a clean one-fact-per-file structure (`user` / `feedback` / `project` / `reference`) over Claude Code's built-in memory, that actively keeps itself healthy: re-verifies stale facts, de-dupes, resolves contradictions, and grows the sources you drop in into interlinked concept notes — legible, trustworthy, and yours to edit.

**📚 Notes vault** — an Obsidian-compatible PARA vault, plus an AI-owned `Synthesis/` zone that turns raw sources you drop in into maintained, linked concept pages.

**🛠️ A starter toolkit of commands:**

| Command | What it does |
|---------|--------------|
| `/brief` | Your morning brief — meetings, what's waiting on you, priorities, deadlines. |
| `/triage` | One pass over inbox + calendar → Needs Reply / FYI / Noise, conflicts flagged. |
| `/prep` | Preps you for one meeting — invite, thread, notes, decisions, likely questions. |
| `/status` | Drafts a status update — what progressed, what's blocked, decisions needed, next steps. |
| `/weekly` | Pre-builds your weekly review and a ready-to-edit status update. |
| `/wiki` | Precedent search over your own notes, answered with citations. |
| `/ingest` | Turns raw notes you drop in into maintained, linked concept pages. |
| `/improve` | The learning loop — captures your corrections into durable memory. |
| `/memory-prune` | Keeps memory healthy — verifies, de-dupes, proposes cleanups (never auto-deletes). |
| `/skill-center` | Build, edit, and audit your own commands as your needs grow. |
| `/board` | Run a decision past a panel of advisor profiles — distinct takes, dissents, a recommendation. |
| `/teach` | A stateful tutor — keeps a syllabus and your progress across sessions. |
| `/workflow-visualizer` | Turns a system you describe into one interactive HTML diagram. |

**⚡ Local-first by design** — caches your calendar and mail locally and refreshes only what changed (Graph delta / Gmail history), so it's instant to use and won't trip rate limits.

## Your control & privacy

- **Read-only by default.** It drafts and shows you; you approve before anything goes outward. Approving one action is never standing approval for the next.
- **Your data stays local.** Cached on your own machine; confidential material is treated as never-leaves-without-your-say.
- **Yours to shape.** The starter commands are a foundation — `/skill-center` adds and refines more as you go.

## The principles behind it

A few rules shape every command — the same ones, whatever you wire it to:

- **Propose, don't act.** It drafts and recommends; you approve. The safe, reversible direction can be automatic — anything outward-facing or hard to undo waits for your OK.
- **Earn trust, don't assume it.** It leads with what it's unsure of, checks the real source instead of a cached "looks fine," and tells you when something's stale.
- **Signal over noise.** It surfaces what changed and what needs you, and stays quiet when nothing does.
- **Remember, then improve.** Your context persists and compounds; a correction you make once becomes a durable rule, not a lesson you repeat.
- **Local-first, yours to shape.** Your data stays on your machine, secrets stay out of the conversation, and every piece is a small tool you can read, edit, or replace.

## A note before you connect a work account

This is a **personal-productivity template**, not an official product of any employer. If you're wiring it to a work mailbox, confirm with your leadership / IT that Claude Code with the Microsoft 365 or Google Workspace connector is approved for your account first.

---

<div align="center">
<sub>Built &amp; shared by Craig Vandeputte · adapt it freely.</sub>
</div>
