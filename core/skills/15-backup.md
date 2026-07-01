---
name: backup
order: 15
tier: core
---
   - /backup — Protect this whole AI-OS — my memory, my notes vault, AND my skills
     (they live outside ~/ai-os, so nothing else captures them) — against a lost or
     wiped machine. With no arguments it just works: commit my ~/ai-os to its own git
     history (the cheap, frequent layer), build a timestamped full snapshot under
     backups/, encrypt it, and drop the encrypted copy into the cloud folder that
     syncs off this machine — so I have a working copy, on-disk history, and an
     offsite copy (the 3-2-1 rule) without thinking about it. Expert flags exist
     (--full, --no-encrypt, --to <path>, --dry-run) and a backup.config.yml tunes
     destinations, retention, and what's included. Build it per the BACKUP & RECOVERY
     section below. Trigger on "/backup", "back up my system", "snapshot my AI-OS".
<!-- docs -->
## What it does
Protects your whole AI-OS — memory, notes, *and* your skills — against a lost or wiped machine. One command keeps an on-disk history and tucks an encrypted copy into the cloud folder you already sync (the 3-2-1 rule), no setup required.

## When to use it
Regularly, and before anything risky — a big cleanup, a migration. Your skills live outside `~/ai-os`, so nothing else captures them; this is the one thing that does.

## Walkthrough
1. Type `/backup`. With no arguments it just works.
2. It commits your `~/ai-os` to its own git history (the cheap, frequent layer), builds a timestamped full snapshot under `backups/`, encrypts it, and drops the encrypted copy into your synced cloud folder.
3. You end up with a working copy, on-disk history, and an offsite copy — 3-2-1 — without thinking about it.

A backup looks about like this:

> **Backup complete**
> · Committed ~/ai-os (git) · Snapshot backups/2026-06-30T09-12.tar.gz.enc (encrypted)
> · Copied offsite → your cloud folder
> Memory, notes, and 17 skills all captured.

## Power user
- **Expert flags exist.** `--full`, `--no-encrypt`, `--to <path>`, `--dry-run`; a `backup.config.yml` tunes destinations, retention, and what's included.
- **It captures your skills.** Because commands live outside `~/ai-os`, `/backup` deliberately reaches out to include them — a plain vault sync would miss them.
- **Prove it with `/restore --drill`.** A backup you've never restored is only a hope; the drill verifies it into a throwaway copy without touching your live system.
- **`/doctor` watches its age.** `/doctor` reports how old your most recent backup is, so a stale one is visible.