---
name: restore
order: 16
tier: core
---
   - /restore — Bring this AI-OS back from a snapshot — after a new laptop, a bad
     edit, or a lost folder. Lists the snapshots it can find (local and the cloud
     folder), defaults to the newest, and lays everything back into place — my memory,
     notes, and skills. It is REVERSIBLE: anything it would overwrite is moved aside
     first, so a restore can itself be undone. Use --dry-run to see exactly what it
     would change, and --drill to prove a backup actually restores (into a throwaway
     copy, never touching my live system) — because a backup I've never restored is
     only a hope. Build it per the BACKUP & RECOVERY section below. Trigger on
     "/restore", "restore my AI-OS", "recover my system".
<!-- docs -->
## What it does
Brings your whole AI-OS back from a snapshot — after a new laptop, a bad edit, or a lost folder. It picks the newest snapshot, lays everything back, and is fully reversible.

## When to use it
When you need your system back — recovery, a fresh machine — or when you want to *prove* your backups actually work (with `--drill`, safely). Anything it would overwrite is moved aside first, so a restore can itself be undone.

## Walkthrough
1. Type `/restore`. It lists the snapshots it can find — local and in your cloud folder — and defaults to the newest.
2. It lays everything back into place: your memory, notes, and skills.
3. Anything it would overwrite is moved aside first, so the restore is reversible. Use `--dry-run` to see exactly what it would change before committing.

A dry run looks about like this:

> **Restore (dry-run)**
> Source: backups/2026-06-30T09-12.tar.gz.enc (newest)
> Would restore: memory/ (84 notes), notes vault, 17 skills
> Existing files → moved to restore-backup/ first — nothing lost.
> Re-run without --dry-run to apply.

## Power user
- **`--drill` proves a backup.** It restores into a throwaway copy, never touching your live system — the honest test that your `/backup` actually works.
- **Always reversible.** Overwrites are set aside first, so a restore you didn't want can be undone.
- **`--dry-run` first.** See the exact change set before you commit — especially on a machine that already has data.
- **Pairs with `/backup`.** Together they're your recovery quadrant; `/doctor` tells you the safety net is current.