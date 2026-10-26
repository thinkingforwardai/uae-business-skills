---
name: uae-golden-visa-precheck
description: Use when someone asks whether they might qualify for a UAE Golden Visa (long-term Golden Residency) — as a property investor, business owner or investor, skilled professional, entrepreneur, outstanding talent, researcher or student — and wants a preliminary match to official routes, a gap list and a document checklist. Not an eligibility decision and not for submitting applications.
version: 0.1.0
knowledge_reviewed: 2026-10-26
review_threshold_days: 100
reviewer: pending
license: MIT
author: Thinking Forward (thinkingforward.ai)
requires_mcp: [mcp-dubai]
optional_mcp: [open-emirates, dld-mcp, uae-law-mcp]
---

# UAE Golden Visa Pre-check

Match a person's situation to UAE Golden Residency routes, show what is missing, and prepare them for an official application or a licensed adviser. **Never state that someone "qualifies" — state "appears to match route X, subject to verification".**

## When to use

- "Can I get a Golden Visa if I buy property in Dubai?"
- "I earn AED X as a software engineer — am I eligible for the 10-year visa?"
- "Which Golden Visa route fits a startup founder?"
- "What documents do I need for a Golden Visa?"

## Inputs — ask only for what is missing

See [references/inputs.md](references/inputs.md). Collect in one message:

1. Which route the person is considering (or "not sure")
2. Current status: inside UAE on a residence visa / outside UAE / visit
3. For property: emirate, area, property type, price range, completed or off-plan, mortgage yes/no, sole or joint ownership
4. For professionals: occupation category, education level, monthly salary range (AED)
5. For investors/business owners: type of investment and amount range
6. For entrepreneurs, talents, researchers, students: the qualifying achievement in one sentence
7. Family members to sponsor (counts only)

**Never** ask for passport, Emirates ID or document numbers, or exact salary slips.

## Steps

### 1. Freshness and sources
- `mcp-dubai.get_knowledge_status()` → check `visas` domain age (high volatility, 100 days). Warn if exceeded.
- If `open-emirates` is connected: call `uae_golden_residency` to get the **current list of official routes** with their publishers and fetch dates. This is the primary route list. Otherwise use `mcp-dubai.list_visa_types` and note the source.

### 2. Route matching
- For each plausible route, call `mcp-dubai.golden_visa_check` with the user's facts and `mcp-dubai.visa_details` for the route.
- Build a table: route · key criteria · user's value · match (`appears to match` / `gap` / `unknown`) · what is missing.
- If two taxonomies disagree (Open Emirates routes vs MCP-Dubai visa types), show both and mark the item "to verify".

### 3. Property route — value check (only if property is involved)
- If `dld-mcp` is connected: `query_dld(area=<area>, type="sales", property_type=<type>, metric="stats")` for the last 12 months. Report median and range as **market context**, not as a valuation.
- Explain which value typically counts (purchase price / title deed value / DLD valuation) as "to verify with the authority", and what usually affects off-plan and mortgaged properties (paid amount, bank letters) — preliminary only.
- Never imply that a market median proves the user's property value.

### 4. Legal basis
If `uae-law-mcp` is connected: `search_legislation("entry and residence of foreigners golden residence")`, cite the relevant provisions with `format_citation`, run `check_currency`. Otherwise mark "legal basis to verify".

### 5. Family and practicalities
- Family sponsorship: list which family members the route typically allows to sponsor, as preliminary.
- Steps: list the typical sequence (eligibility / nomination where applicable → application through the competent authority's channel → medical test → Emirates ID biometrics) and note that the channel differs by emirate and route. Use `mcp-dubai.portal_guide` for which portals are relevant — **describe, never operate them**.
- Costs: use tool data only; if absent, say "fees vary — check the authority's fee schedule".

### 6. Output
Use [references/output-template.md](references/output-template.md).

## Output rules

- Lead with a one-sentence verdict phrased as **"appears to match / does not appear to match / unclear"**.
- One table of routes with match status and gaps.
- Document checklist grouped by route.
- "What only the authority can confirm" — always present.
- Every criterion has a source and a date; legal statements have citations or "to verify".

## Hard rules — the agent does NOT

- tell anyone they are eligible or approved
- submit, pay, upload, book medical tests or biometrics, or log in to any portal
- collect or store passport, Emirates ID, visa file numbers, salary slips or bank statements
- value a specific property (market statistics are context only)
- give advice on circumventing requirements

## Fallbacks

- No `open-emirates` → use `mcp-dubai` routes, flag "single source".
- No `dld-mcp` → skip market context for property.
- No `mcp-dubai` → general explanation only, every criterion marked "unverified", recommend checking the official immigration authority portal.

## Escalation

Recommend verification with the competent immigration authority (ICP federally, GDRFA for Dubai) and, for complex cases (joint ownership, off-plan, company-owned property, previous rejections), a licensed adviser.

## Sources

See [references/sources.md](references/sources.md).
