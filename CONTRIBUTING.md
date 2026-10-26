# Contributing

Thank you for helping make these skills accurate and useful.

## Most valuable contributions

1. **Corrections from practitioners** — PROs, setup providers, tax agents, lawyers. If something is wrong or outdated, open an issue with the correct information and a source (official page, law article, circular).
2. **Freshness updates** — fees, timelines and rules change. Updates must include a source and the date you checked it.
3. **New skills** that follow [`templates/SKILL_TEMPLATE.md`](templates/SKILL_TEMPLATE.md).
4. **Arabic translations** reviewed by a native speaker.

## Rules for every change

- Every factual claim (number, deadline, fee, threshold, eligibility rule) needs a **source URL** and a **checked-on date**.
- Update `knowledge_reviewed` in the skill front-matter when you change facts.
- No personal data, no screenshots with personal data, no credentials.
- No official logos, emblems or branding of authorities.
- Do not add steps where the agent submits, signs, pays, or enters passwords/OTPs. A human does those.
- Keep `SKILL.md` focused on the workflow; put long reference material in `references/`.

## Before opening a pull request

```bash
python3 scripts/validate_skills.py
```

The validator checks front-matter fields and required sections.

## Reviewers

Content reviewers are listed in each skill's front-matter (`reviewer`). If you are a licensed professional in the UAE and want to review a skill, open an issue titled `Reviewer: <skill name>`.
