# AI OS — a personal "operating system" for Claude Code

A one-page walkthrough + copy-paste setup prompt that stands up a personal **AI
operating system** inside [Claude Code](https://claude.com/claude-code): a
persistent **file-based memory**, a structured **notes vault** (PARA), and a
starter set of **skills** (slash-commands) — wired to **Microsoft 365** (Outlook
mail + calendar, Teams, SharePoint).

It interviews you first, then builds everything shaped to your role, and keeps
getting more "you" every time you correct it.

## What you get

- **Persistent memory** — one-fact-per-file notes (`user` / `feedback` / `project`
  / `reference`) with an index that loads every session, interlinked and
  self-maintaining.
- **Notes vault** — an Obsidian-compatible PARA vault, plus an AI-owned
  `Synthesis/` zone that turns raw sources you drop in into maintained, linked
  concept pages (`/ingest`).
- **Skills** — `/brief`, `/triage`, `/prep`, `/status`, `/raid`, `/weekly`,
  `/wiki`, `/improve`, `/ingest`, `/memory-prune`, `/skill-center` — read-only by
  default, nothing sent without your explicit OK.
- **Local-first Microsoft 365** — caches calendar + mail locally and refreshes
  only when stale, so it's instant and won't trip Graph throttling.

## How to use it

1. Open **`index.html`** in a browser (or view the hosted page) and read the
   walkthrough.
2. Install Claude Code and connect the Microsoft 365 connector.
3. Open a Claude Code session in a folder you want as your AI-OS home
   (e.g. `~/ai-os`).
4. Copy the setup prompt from the page and paste it as your first message.
5. Answer the interview — Claude builds the rest and explains what it made.

## Note

This is a **personal-productivity template**, not an official product of any
employer. If you're wiring it to a work account, confirm with your leadership / IT
that Claude Code with the Microsoft 365 connector is approved first.

Built & shared by Craig Vandeputte.
