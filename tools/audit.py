"""Run a lightweight static audit of the PyDSA project.

Run from anywhere:
    python3 tools/audit.py

This audit checks the repository structure, generated program data, the learning content
lesson coverage (including intentional aliases), HTML script references,
JavaScript syntax, and Python lesson generation. It does not replace a real
browser smoke test.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
JS = ASSETS / "js"
SOURCE = ROOT / "tools" / "source_programs"

REQUIRED_HTML = [
    "index.html", "programs.html", "python.html", "lesson.html",
    "dsa.html", "interview.html", "404.html",
]
LESSON_FILES = [
    "program-lessons.js",
    "program-lessons-stack.js",
    "program-lessons-advanced-stack.js",
    "program-lessons-linked.js",
    "program-lessons-dp.js",
    "program-lessons-bit.js",
    "program-lessons-patterns.js",
]
ALIASES = {
    "arrays-strings-2-05": "searching-sorting-01",
    "recursion-math-10": "recursion-math-01",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def node_load_data() -> dict:
    script = r"""
const fs = require('fs');
const vm = require('vm');
const path = process.argv[1];
const files = process.argv.slice(2);
const context = { window: {} };
vm.createContext(context);
for (const file of files) vm.runInContext(fs.readFileSync(file, 'utf8'), context, {filename:file});
process.stdout.write(JSON.stringify({
  programs: context.window.PYDSA_PROGRAMS,
  groups: context.window.PYDSA_GROUPS,
  lessons: context.window.PYDSA_PROGRAM_LESSONS || {}
}));
"""
    files = [JS / "data.js"] + [JS / f for f in LESSON_FILES]
    result = subprocess.run(
        ["node", "-e", script, str(ROOT), *map(str, files)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        fail(f"could not load generated/lesson JavaScript: {result.stderr.strip()}")
    return json.loads(result.stdout)


def check_structure() -> None:
    for name in REQUIRED_HTML:
        if not (ROOT / name).is_file():
            fail(f"missing HTML entry point: {name}")
    for name in ["data.js", "content.js", "app.js", "sections.js", "lesson.js"]:
        if not (JS / name).is_file():
            fail(f"missing core JavaScript file: {name}")
    for name in LESSON_FILES:
        if not (JS / name).is_file():
            fail(f"missing program lesson registry: {name}")


def check_html_script_refs() -> None:
    missing = []
    pattern = re.compile(r'<script\b[^>]*\bsrc=["\']([^"\']+)["\']', re.I)
    for html in ROOT.glob("*.html"):
        for ref in pattern.findall(html.read_text(encoding="utf-8")):
            if "://" in ref or ref.startswith("/"):
                continue
            target = (html.parent / ref).resolve()
            if not target.is_file():
                missing.append(f"{html.name} -> {ref}")
    if missing:
        fail("missing HTML script references: " + ", ".join(missing))


def check_js_syntax() -> None:
    failures = []
    for path in sorted(JS.glob("*.js")):
        result = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)
        if result.returncode:
            failures.append(f"{path.relative_to(ROOT)}: {result.stderr.strip()}")
    if failures:
        fail("JavaScript syntax errors:\n" + "\n".join(failures))


def main() -> None:
    check_structure()
    check_html_script_refs()
    check_js_syntax()

    payload = node_load_data()
    programs = payload["programs"]
    groups = payload["groups"]
    lessons = payload["lessons"]

    if len(programs) != 91:
        fail(f"expected 91 programs, found {len(programs)}")
    if len(groups) != 10:
        fail(f"expected 10 groups, found {len(groups)}")

    missing_code = [p["id"] for p in programs if not p.get("code")]
    if missing_code:
        fail("programs with missing code: " + ", ".join(missing_code))

    ids = [p["id"] for p in programs]
    if len(ids) != len(set(ids)):
        fail("duplicate program IDs detected")

    missing_lessons = []
    alias_mismatches = []
    for pid in ids:
        if pid in ALIASES:
            if ALIASES[pid] not in lessons:
                alias_mismatches.append(f"{pid} -> missing canonical {ALIASES[pid]}")
        elif pid not in lessons:
            missing_lessons.append(pid)
    if missing_lessons:
        fail("programs without a canonical lesson or alias: " + ", ".join(missing_lessons))
    if alias_mismatches:
        fail("broken aliases: " + ", ".join(alias_mismatches))

    group_counts = {}
    for p in programs:
        group_counts[p["group"]] = group_counts.get(p["group"], 0) + 1
    if len(group_counts) != 10:
        fail(f"expected 10 populated groups, found {len(group_counts)}")

    print("PASS: project structure")
    print("PASS: HTML script references")
    print(f"PASS: JavaScript syntax ({len(list(JS.glob('*.js')))} files)")
    print(f"PASS: {len(programs)} programs, {len(groups)} groups")
    print("PASS: missing code: []")
    print(f"PASS: {len(lessons)} canonical lessons + {len(ALIASES)} intentional aliases")
    print("PASS: every program has a lesson or intentional alias")
    print("NOTE: browser interaction/console smoke testing still requires a real browser")


if __name__ == "__main__":
    main()
