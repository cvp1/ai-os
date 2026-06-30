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