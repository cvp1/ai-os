#!/usr/bin/env python3
"""Generate ai-os/index.html from the core/ source fragments.

index.html is a BUILD ARTIFACT — edit core/, never index.html. The build is
deterministic and idempotent: no source change -> byte-identical output (which is
what keeps the 3-copy ai_os_sync_check.sh meaningful).

Usage:
  build_installer.py            # write index.html from core/ (warns on coverage drift)
  build_installer.py --check    # exit 1 if index.html is stale OR a command is
                                # missing from a human-facing list (CI guard)

After a real build, propagate to the docsite/vault copies with:
  ../ai-os-pm/.. no -> tools/ai_os_sync_check.sh --sync   (run from ai-os-pm/tools)
Canonical source of truth for the prompt text is core/; for the served copies it
remains the public-repo index.html (see ai_os_sync_check.sh).

Stdlib only, /usr/bin/python3.
"""
import re, sys, glob, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent      # .../ai-os
CORE = ROOT / "core"
OUT = ROOT / "index.html"
GUIDE_OUT = ROOT / "guide.html"   # the Field Guide — per-command layered docs (D25)
JOIN = "\n\n"   # the exact separator that flanks/separates skill blocks

# The docs delimiter separates a skill fragment's PROMPT body (injected verbatim into
# the setup prompt) from its GUIDE doc block (rendered into guide.html only). It
# consumes the single newline before the marker, so a fragment's prompt body stays
# byte-identical whether or not a docs block is appended.
DOC_DELIM = re.compile(r"\n<!-- docs -->\n")

def read(p):
    return (CORE / p).read_text()

def read_version():
    m = re.search(r'^version:\s*"?([^"\n]+?)"?\s*(?:#.*)?$', read("meta.yml"), re.M)
    if not m:
        sys.exit("FATAL: meta.yml has no version")
    return m.group(1).strip()

def _after_frontmatter(text):
    """Everything after the leading '---\\n...\\n---\\n' frontmatter."""
    m = re.match(r"---\n.*?\n---\n", text, re.S)
    if not m:
        sys.exit("FATAL: skill fragment missing frontmatter")
    return text[m.end():]

def skill_body(text):
    """The PROMPT body — frontmatter stripped, and any trailing docs block removed so
    guide-only content never leaks into the pasted setup prompt."""
    return DOC_DELIM.split(_after_frontmatter(text), maxsplit=1)[0]

def skill_docs(text):
    """The GUIDE doc block (light markdown after the <!-- docs --> delimiter), or None
    if this skill has no doc block authored yet."""
    parts = DOC_DELIM.split(_after_frontmatter(text), maxsplit=1)
    return parts[1] if len(parts) == 2 else None

def skill_order(text):
    m = re.search(r"^order:\s*(\d+)\s*$", text, re.M)
    return int(m.group(1)) if m else 9999

def skill_commands():
    """Command names (without the slash) declared by core/skills/*.md frontmatter."""
    cmds = []
    for p in sorted(glob.glob(str(CORE / "skills/*.md"))):
        t = pathlib.Path(p).read_text()
        m = re.search(r"^name:\s*(\S+)\s*$", t, re.M)
        if not m:
            sys.exit("FATAL: %s has no name: in frontmatter" % pathlib.Path(p).name)
        cmds.append(m.group(1).strip())
    return cmds

def _section(html, sec_id):
    """Inner markup of <section id="sec_id"> ... </section>, or '' if absent."""
    m = re.search(r'<section id="%s".*?</section>' % re.escape(sec_id), html, re.S)
    return m.group(0) if m else ""

def check_command_coverage():
    """Every core/skills command must be named in BOTH human-facing surfaces — the
    README command table and the landing #commands section — not just in the pasted
    prompt (which the build always fills). This is the tripwire for the drift where a
    new skill ships in the prompt but is missing from the lists a person actually
    reads. Limits (by design, kept a simple tripwire): it does not police the reverse
    (a listed command with no skill), nor distinguish a dedicated row from an
    in-prose cross-reference. Returns a list of problem strings ([] = clean)."""
    problems = []
    readme = (ROOT / "README.md").read_text()
    commands_sec = _section(read("shell.html"), "commands")
    if not commands_sec:
        problems.append('shell.html has no <section id="commands"> to check')
    for name in skill_commands():
        n = re.escape(name)
        # A command counts as "listed" on the landing page if it appears either as a
        # contiguous /name (in a description or the "Try saying" column) OR in the grid's
        # command cell, where the slash is its own span: <span class="slash">/</span>name.
        # (The cell form couples this check to that template — fine; if the markup ever
        # changes the guard fails loudly and gets updated.)
        plain = re.compile(r"/%s(?![\w-])" % n)
        cell = re.compile(r'/</span>%s(?![\w-])' % n)
        if not plain.search(readme):
            problems.append("/%s missing from the README command list" % name)
        if commands_sec and not (plain.search(commands_sec) or cell.search(commands_sec)):
            problems.append("/%s missing from the landing #commands section" % name)
    return problems

def render():
    before = read("sections/before-skills.txt")
    after = read("sections/after-skills.txt")
    career = read("second-act/career.txt")
    scheduler = read("second-act/scheduler.txt")
    projects = read("second-act/projects.txt")
    learning = read("second-act/learning.txt")

    frags = [pathlib.Path(p).read_text() for p in glob.glob(str(CORE / "skills/*.md"))]
    frags.sort(key=skill_order)
    bodies = [skill_body(f) for f in frags]

    prompt = before + JOIN + JOIN.join(bodies) + JOIN + after

    shell = read("shell.html")
    if (shell.count("{{PROMPT}}") != 1 or shell.count("{{PROMPT2}}") != 1
            or shell.count("{{PROMPT3}}") != 1 or shell.count("{{PROMPT4}}") != 1
            or shell.count("{{PROMPT5}}") != 1):
        sys.exit("FATAL: shell.html must contain exactly one each of "
                 "{{PROMPT}}, {{PROMPT2}}, {{PROMPT3}}, {{PROMPT4}}, {{PROMPT5}}")
    html = (shell.replace("{{PROMPT}}", prompt, 1)
                 .replace("{{PROMPT2}}", career, 1)
                 .replace("{{PROMPT3}}", scheduler, 1)
                 .replace("{{PROMPT4}}", projects, 1)
                 .replace("{{PROMPT5}}", learning, 1))
    html = html.replace("{{VERSION}}", read_version())   # global: stamps all build markers
    if "{{VERSION}}" in html:
        sys.exit("FATAL: unsubstituted {{VERSION}} remains")
    return html

# ---- Field Guide (guide.html) rendering ---------------------------------------
# A deliberately small markdown subset — enough for the doc-block template
# (## headings · paragraphs · - and 1. lists · > sample blockquotes · `code`,
# **bold**, *italic*). Kept minimal on purpose: the source of truth is the plain
# doc block in each core/skills/*.md, and a tiny deterministic renderer keeps the
# build honest (no dependency, no surprises). Extend only alongside the template.

def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def _inline(s):
    s = _esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\s)([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
    return s

_BLOCK_START = re.compile(r"^(- |\d+\. |> |## )")

def _gather_item(lines, i, marker_re):
    """Consume one list item starting at line i (its marker already matched);
    fold continuation lines (indented, non-blank, not a new block) into it.
    Returns (item_text, next_i)."""
    item = re.sub(marker_re, "", lines[i].strip(), count=1)
    i += 1
    while i < len(lines) and lines[i].strip() and not _BLOCK_START.match(lines[i].strip()):
        item += " " + lines[i].strip()
        i += 1
    return item, i

def _md_to_html(md):
    lines = md.rstrip("\n").split("\n")
    out, para, i, n = [], [], 0, len(lines)
    def flush():
        if para:
            out.append("<p>" + _inline(" ".join(para)) + "</p>")
            para.clear()
    while i < n:
        s = lines[i].strip()
        if s == "":
            flush(); i += 1; continue
        if s.startswith("## "):
            flush(); out.append('<h3 class="doc-h">' + _inline(s[3:]) + "</h3>"); i += 1; continue
        if s.startswith("> "):
            flush(); buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(_inline(lines[i].strip()[1:].lstrip())); i += 1
            out.append('<blockquote class="sample">' + "<br>".join(buf) + "</blockquote>"); continue
        if re.match(r"^- ", s):
            flush(); items = []
            while i < n and re.match(r"^- ", lines[i].strip()):
                item, i = _gather_item(lines, i, r"^- "); items.append("<li>" + _inline(item) + "</li>")
            out.append("<ul>" + "".join(items) + "</ul>"); continue
        if re.match(r"^\d+\. ", s):
            flush(); items = []
            while i < n and re.match(r"^\d+\. ", lines[i].strip()):
                item, i = _gather_item(lines, i, r"^\d+\. "); items.append("<li>" + _inline(item) + "</li>")
            out.append("<ol>" + "".join(items) + "</ol>"); continue
        para.append(s); i += 1
    flush()
    return "\n".join(out)

def render_guide():
    shell = read("guide-shell.html")
    frags = [pathlib.Path(p).read_text() for p in glob.glob(str(CORE / "skills/*.md"))]
    frags.sort(key=skill_order)
    sections, index_links = [], []
    for f in frags:
        docs = skill_docs(f)
        if not docs:
            continue                      # only authored commands appear (hero-first, D25)
        name = re.search(r"^name:\s*(\S+)\s*$", f, re.M).group(1).strip()
        index_links.append('<a href="#%s"><span class="slash">/</span>%s</a>' % (name, name))
        sections.append(
            '<section id="%s" class="cmd-doc"><div class="wrap">\n'
            '<h2 class="cmd-name"><span class="slash">/</span>%s</h2>\n%s\n'
            '</div></section>' % (name, name, _md_to_html(docs)))
    if not sections:
        sys.exit("FATAL: no skill has a <!-- docs --> block; guide.html would be empty")
    for ph in ("{{GUIDE_INDEX}}", "{{GUIDE_SECTIONS}}"):
        if shell.count(ph) != 1:
            sys.exit("FATAL: guide-shell.html must contain exactly one %s" % ph)
    html = (shell.replace("{{GUIDE_INDEX}}", " · ".join(index_links), 1)
                 .replace("{{GUIDE_SECTIONS}}", "\n\n".join(sections), 1)
                 .replace("{{VERSION}}", read_version()))
    if "{{VERSION}}" in html or "{{GUIDE" in html:
        sys.exit("FATAL: unsubstituted placeholder remains in guide.html")
    return html

def main():
    html = render()
    guide = render_guide()
    coverage = check_command_coverage()
    if "--check" in sys.argv[1:]:
        problems = list(coverage)
        if (OUT.read_text() if OUT.exists() else None) != html:
            problems.append("index.html is stale vs a fresh build of core/ "
                            "(run build_installer.py to regenerate)")
        if (GUIDE_OUT.read_text() if GUIDE_OUT.exists() else None) != guide:
            problems.append("guide.html is stale vs a fresh build of core/ "
                            "(run build_installer.py to regenerate)")
        if problems:
            for p in problems:
                print("FAIL:", p, file=sys.stderr)
            return 1
        print("OK: index.html + guide.html up to date with core/; all %d commands "
              "listed in README + landing" % len(skill_commands()))
        return 0
    if coverage:
        print("WARNING — command-coverage drift (fix before publishing):",
              file=sys.stderr)
        for p in coverage:
            print("  -", p, file=sys.stderr)
    OUT.write_text(html)
    print("wrote", OUT, "(%d bytes)" % len(html))
    GUIDE_OUT.write_text(guide)
    print("wrote", GUIDE_OUT, "(%d bytes)" % len(guide))
    return 0

if __name__ == "__main__":
    sys.exit(main())
