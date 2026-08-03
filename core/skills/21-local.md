---
name: local
order: 21
tier: core
---
   - /local — Give this AI-OS a local floor: a small model running on my own
     machine that keeps essential automated work limping along when the internet
     or the frontier provider is down. With no arguments, report floor readiness
     (is Ollama installed, is a node reachable, is the harness installed, has a
     model actually passed its gate). "/local setup" builds it: check for Ollama
     (point me at ollama.com/download if missing), clone
     https://github.com/cvp1/harness next to ~/ai-os, run
     `python3 -m harness.selftest` (must be all green), then `--probe` and
     `--gate` the model I choose — a model earns its place by measurement, never
     by reputation. Record the node in HARNESS_NODE/HARNESS_MODEL. "/local
     <task>" runs one bounded agentic task through the floor
     (`python3 -m harness "<task>" --workdir <dir>`). The floor is a backstop,
     never the primary: rougher answers that arrive beat perfect answers that
     don't. Always label floor output as local so I know what produced it.
     Trigger on "/local", "set up a local model", "local failover", "make this
     work offline", "run that locally".
<!-- docs -->
## What it does
Gives your AI-OS a *local floor* — a small model on your own hardware that keeps essential automated work running, rougher but alive, when the internet or your AI provider is down. The harness underneath it is a small open tool that makes almost any local model usable for multi-step work: it speaks each model's dialect for it, keeps every loop bounded, and scores models by measurement instead of reputation.

## When to use it
Once, at setup, if you own any machine that can run [Ollama](https://ollama.com) — then forget about it until the day your connection dies and your morning brief shows up anyway, labeled `source=local`.

## Walkthrough
1. Type `/local setup`.
2. It checks for Ollama (and points you at the installer if it's missing), clones the harness beside your AI-OS, and runs its selftest — all green or it stops there.
3. It then **probes** your model (which tool-calling dialect actually works) and **gates** it (three real multi-step trials, scored on what landed on disk — not on what the model claimed).
4. From then on, `/local <task>` runs work through the floor, and automated jobs that support it degrade to the floor instead of dying.

A readiness report looks about like this:

> **Local floor: READY**
> · Ollama 0.32 on this machine · model `granite4.1:8b`
> · dialect: native (probed) · gate: 3/3 multi-step PASS
> · Frontier down? Your scheduled work degrades here instead of dying.

## Power user
- **The gate is the truth.** A model can pass a one-shot probe and still collapse on multi-step work — the gate catches that. Don't hand agentic duty to a model that hasn't gone 3/3.
- **The node doesn't have to be this machine.** `HARNESS_NODE=192.168.1.50:11434` points the floor at any Ollama box on your network; `HARNESS_MODEL` pins the model.
- **Any model can apply.** New model on the shelf? `python3 -m harness --probe <tag>` then `--gate <tag>`. The registry records what was *measured*, and marks everything else as assumed.
- **Bounded by design.** Turn limits, wall-clock budgets, and output caps all *refuse* rather than run away — a stuck local model costs you seconds, not your evening.
- **It's a floor, not a ceiling.** Local output is rougher; the frontier stays primary. The floor exists so "provider outage" stops being "everything stops."
