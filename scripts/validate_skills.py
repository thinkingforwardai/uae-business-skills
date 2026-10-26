#!/usr/bin/env python3
"""Validate SKILL.md files: front-matter fields, required sections, linked references."""
import datetime as dt
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED_FIELDS = [
    "name", "description", "version", "knowledge_reviewed",
    "review_threshold_days", "reviewer", "license", "requires_mcp",
]
REQUIRED_SECTIONS = [
    "## When to use", "## Inputs", "## Steps", "## Hard rules",
    "## Fallbacks", "## Escalation", "## Sources",
]


def parse_front_matter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.split("#", 1)[0].strip()
    return fields


def check(path: pathlib.Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    fm = parse_front_matter(text)
    if not fm:
        return [f"{path}: missing front-matter"]
    for field in REQUIRED_FIELDS:
        if not fm.get(field):
            errors.append(f"{path}: missing front-matter field '{field}'")
    if fm.get("name") and fm["name"] != path.parent.name:
        errors.append(f"{path}: name '{fm['name']}' must match folder '{path.parent.name}'")
    if len(fm.get("description", "")) > 1024:
        errors.append(f"{path}: description longer than 1024 characters")
    try:
        reviewed = dt.date.fromisoformat(fm.get("knowledge_reviewed", ""))
        threshold = int(fm.get("review_threshold_days", "0"))
        age = (dt.date.today() - reviewed).days
        if threshold and age > threshold:
            errors.append(f"{path}: knowledge_reviewed is {age} days old (threshold {threshold})")
    except ValueError:
        errors.append(f"{path}: knowledge_reviewed must be YYYY-MM-DD")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"{path}: missing section '{section}'")
    for link in re.findall(r"\]\((references/[^)]+)\)", text):
        if not (path.parent / link).exists():
            errors.append(f"{path}: broken link {link}")
    return errors


def main() -> int:
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        print("No skills found")
        return 1
    errors = [e for s in skills for e in check(s)]
    for e in errors:
        print(f"ERROR {e}")
    print(f"Checked {len(skills)} skills, {len(errors)} problem(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
