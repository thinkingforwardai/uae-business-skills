---
name: uae-company-setup-advisor
description: Use when someone wants to set up or relocate a company in the UAE and needs to choose between mainland, free zone and offshore, compare free zones, estimate setup cost, timeline, visa allocation, banking and Corporate Tax impact, or get a document checklist before talking to a setup provider. Not for submitting applications.
version: 0.1.0
knowledge_reviewed: 2026-10-26
review_threshold_days: 100
reviewer: pending
license: MIT
author: Thinking Forward (thinkingforward.ai)
requires_mcp: [mcp-dubai]
optional_mcp: [uae-law-mcp, open-emirates]
---

# UAE Company Setup Advisor

Help a founder or business choose a UAE company structure and prepare for a conversation with a licensed setup provider. Output is a **preliminary comparison**, never a licensing decision.

## When to use

- "Should I set up in mainland Dubai or a free zone?"
- "Which free zone is best for a software / trading / consulting company?"
- "How much does it cost and how long does it take to open a company in the UAE?"
- "What do I need to prepare to open a UAE company and bank account?"

## Inputs — ask only for what is missing

Collect these in one short message, not one by one. See [references/inputs.md](references/inputs.md) for allowed values.

1. Business activity (plain words is fine)
2. Where the clients are (UAE market / outside UAE / both) and whether you sell to UAE government entities
3. Number of shareholders and their nationality group (UAE/GCC vs other) — **no names, no ID numbers**
4. Number of residence visas needed now and in 12 months
5. Need for physical office or warehouse
6. Preferred emirate (or "no preference")
7. Budget range for year one (AED)
8. Expected annual revenue range (AED) — needed for Corporate Tax and VAT thresholds

If the user does not know a value, proceed with a stated assumption.

## Steps

### 1. Freshness check
Call `mcp-dubai.get_knowledge_status()`. For domains `setup_advisor`, `free_zones`, `visas`, `banking`, `tax_compliance`, `founder_essentials`: if age since `full_review_date` exceeds the domain's threshold (high volatility 100 days, medium 190, stable 365), add a visible warning in the output. Call `mcp-dubai.get_upstream_status()` once and note any blocked sources.

### 2. Jurisdiction type
Call `mcp-dubai.setup_advisor` with the activity, client location, visa count, office need and budget. Capture the recommended option (mainland / free zone / offshore) **and the reasons**. Apply these checks before accepting the recommendation:
- Selling directly to the UAE onshore market or to government → mainland is usually required or a distributor/branch arrangement is needed. State it as "usually", and flag for verification.
- Offshore entities cannot hold UAE residence visas or operate onshore → exclude offshore if visas > 0.

### 3. Free zone shortlist (if free zone is in play)
Call `mcp-dubai.list_free_zones`, then `mcp-dubai.compare_free_zones` for the 3 best fits on activity, emirate preference, visa quota, office options and cost. Use `mcp-dubai.free_zone_details` for each finalist. Mention `mcp-dubai.list_offshore` only if offshore remains relevant.

### 4. Corporate Tax and VAT impact
- Call `mcp-dubai.corporate_tax_estimate` with the expected profit or revenue range.
- For free zone options call `mcp-dubai.qfzp_check` and explain in one paragraph what Qualifying Free Zone Person status depends on (qualifying income, substance, audited accounts, de minimis rules) — as preliminary.
- Call `mcp-dubai.vat_filing_calendar` and state whether VAT registration is likely mandatory, voluntary or not required for the revenue range.
- Call `mcp-dubai.einvoicing_timeline` and add one line on when e-invoicing may apply.
- If `uae-law-mcp` is connected: `search_legislation("Corporate Tax Federal Decree-Law 47 of 2022")`, then `get_provision` for the rate/threshold article and `check_currency`. Cite it.

### 5. Visas, bank, timeline, cost
- `mcp-dubai.visa_recommend` for investor/partner/employee visas matching the plan; `mcp-dubai.golden_visa_check` only if the user mentions investment above typical setup level.
- `mcp-dubai.bank_recommendation` for the activity and shareholder profile; `mcp-dubai.dul_eligibility` if the setup is in Dubai.
- `mcp-dubai.setup_timeline_estimate` and `mcp-dubai.pro_services_estimate` for each finalist.
- `mcp-dubai.attestation_guide` if shareholders are corporate or documents come from abroad.
- `mcp-dubai.common_founder_mistakes` — pick the 3 most relevant to this case.

### 6. Compliance obligations from day one
Call `mcp-dubai.ubo_filing_guide`, `mcp-dubai.aml_requirements` (only if the activity is a designated non-financial business), `mcp-dubai.esr_status`, `mcp-dubai.emiratisation_requirements` (mainland with staff), `mcp-dubai.pdpl_compliance` (if handling personal data of customers). Summarise as a short list.

### 7. Write the output
Use [references/output-template.md](references/output-template.md). Keep it under ~900 words unless the user asks for more.

## Output rules

- Compare **at most 3 options** side by side in one table: type, authority, year-one cost range, timeline, visa capacity, office requirement, Corporate Tax position, main trade-off.
- Every cost and timeline is a **range with a source and a date** from the tool result (`knowledge_date` / `verify_at`).
- Every legal statement has a citation or is marked "to verify".
- End with **"What a licensed setup provider must confirm"** (3–6 bullets) and a **hand-off brief** the user can send to a provider.
- Currency: AED; add the user's home currency only if asked (`mcp-dubai.currency_convert`).

## Hard rules — the agent does NOT

- submit applications, reserve trade names, sign, pay, or log in to any portal
- ask for or store passport numbers, Emirates ID numbers, addresses of individuals, passwords or OTPs
- present a recommendation as a licensing, tax or immigration decision
- claim to be affiliated with any authority or free zone

## Fallbacks

- `mcp-dubai` unavailable → say so, give only a high-level comparison from general knowledge, mark every figure "unverified", and recommend re-running when the server is available.
- `uae-law-mcp` unavailable → skip citations, mark legal statements "to verify".

## Escalation

Always recommend a licensed business setup provider / PRO for licence application, a registered tax agent for Corporate Tax and VAT position, and a lawyer for shareholder agreements or regulated activities (financial services, healthcare, education, media). Regulated activities: flag early that additional approvals are likely.

## Sources

See [references/sources.md](references/sources.md).
