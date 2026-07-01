---
name: workflow-visualizer
order: 14
tier: core
---
   - /workflow-visualizer — Turn a system or process I describe into one
     self-contained interactive HTML diagram (clickable nodes, hover detail, ~20
     nodes max) I can open in a browser — an architecture, an approval flow, how a
     project's pieces connect. Save the single HTML file under the vault
     (04 Resources/Diagrams/) and give me the path. Trigger on
     "/workflow-visualizer", "diagram this", "map out this system".
<!-- docs -->
## What it does
Turns a system or process you describe into one self-contained interactive HTML diagram — clickable nodes, hover detail — that you can open in a browser.

## When to use it
When a wall of text would be clearer as a picture: an architecture, an approval flow, how a project's pieces connect. Good for sharing, or for thinking something through visually.

## Walkthrough
1. Describe the thing — *"diagram our release process"* or *"map out how these services connect"*.
2. It builds one self-contained interactive HTML file (up to ~20 nodes, with clickable nodes and hover detail).
3. It saves the file in your vault (`04 Resources/Diagrams/`) and gives you the path to open.

A run looks about like this:

> **Release process → diagram**
> 7 nodes: PR → CI → review → staging → QA → deploy → monitor
> Saved: 04 Resources/Diagrams/release-process.html — open it in your browser.

## Power user
- **Keep it to one system.** It's tuned for ~20 nodes — a focused flow reads far better than an everything-map. Split a big system into a few diagrams.
- **Self-contained by design.** The output is a single HTML file with no dependencies — email it or drop it anywhere.
- **It's a file you own.** Saved in your vault; edit the description and regenerate to iterate.