---
name: uae-einvoicing-readiness
description: Use when a UAE business (or its accountant) asks whether and when it must comply with UAE e-invoicing (Peppol, PINT AE, accredited service provider), what its deadline is, or wants its invoice data, ERP export or sample invoices checked for missing e-invoicing fields and a readiness plan. Not for issuing, transmitting or submitting invoices.
version: 0.1.0
knowledge_reviewed: 2026-10-26
review_threshold_days: 60
reviewer: pending
license: MIT
author: Thinking Forward (thinkingforward.ai)
requires_mcp: [mcp-dubai]
optional_mcp: [bga-uae-updates, uae-law-mcp]
---

# UAE E-invoicing Readiness

Tell a business **whether, when and how** UAE e-invoicing is likely to apply to it, find gaps in its invoice data, and produce a practical readiness plan. The skill prepares; an FTA-accredited service provider (ASP) transmits.

## When to use

- "Do we need e-invoicing in the UAE and from when?"
- "What is PINT AE / the 5-corner model / an ASP?"
- "Here is an export of our invoices — what's missing for e-invoicing?"
- "Give us a readiness plan for e-invoicing."

## Inputs — ask only for what is missing

See [references/inputs.md](references/inputs.md).

1. Annual revenue band (AED): `<50m` or `≥50m` — the main driver of the deadline
2. Customer types: B2B / B2G / B2C (share, roughly)
3. VAT registration status (registered / group / not registered)
4. Invoicing system (ERP / accounting software / manual / multiple)
5. Monthly invoice volume (range)
6. Optional: a **sample export** (CSV/XLSX) or 1–3 sample invoices — **with personal data removed**

## Steps

### 1. Check for the latest rules first (this domain changes fast)
- `mcp-dubai.get_knowledge_status()` → `tax_compliance` domain. Threshold for this skill: **60 days**; warn if exceeded.
- If `bga-uae-updates` is connected: list the most recent FTA / Ministry of Finance publications on e-invoicing and read the newest. If anything contradicts [references/timeline.md](references/timeline.md), **the newer official publication wins** — say so in the output.
- `mcp-dubai.einvoicing_timeline` → capture phases and dates with `knowledge_date`.

### 2. Scope and deadline
Using revenue band, customer types and the timeline:
- Determine the **applicable phase and dates** (ASP appointment date and go-live date) — label "per {source, date}; verify".
- B2C: explain the current position for B2C as stated by the source (do not assume).
- B2G: note the separate government timeline if the business invoices government entities.
- Days remaining to each date from today.

### 3. Model explained in plain words (short)
Peppol, decentralised "5-corner" model: supplier → supplier's ASP → buyer's ASP → buyer, with tax data reported to the FTA. Structured XML/JSON in PINT AE format; **PDF or scanned invoices will not qualify** as e-invoices. One paragraph, no more.

### 4. Data gap check (if the user provided an export or samples)
- Map the user's columns to the field groups in [references/field-checklist.md](references/field-checklist.md).
- Produce a table: field group · required for · present? · example value (masked) · fix.
- Flag common blockers: missing buyer TRN for B2B, no Peppol participant identifier, free-text VAT rates instead of category codes, mixed currencies without exchange rate, missing invoice type for credit notes, totals that don't reconcile (recompute in code).
- **Do not** claim the file is "compliant". Say "no gaps found in the checked field groups".

### 5. Legal basis
If `uae-law-mcp` is connected: search the VAT law and its e-invoicing amendments/decisions; cite and `check_currency`. Otherwise mark "to verify" and point to the FTA.

### 6. Readiness plan
Use [references/output-template.md](references/output-template.md). The plan has owners and dates counted back from the deadline:
1. Appoint ASP (shortlist criteria: Peppol certification, FTA accreditation, ERP connectors, volume pricing, Arabic support)
2. Master data cleanup (customer TRNs, Peppol IDs, VAT categories)
3. ERP mapping and test invoices with the ASP
4. Process changes (credit notes, corrections, rejections)
5. Archiving and audit trail
6. Go-live and monitoring

## Hard rules — the agent does NOT

- issue, sign, transmit or submit invoices, or connect to any ASP or FTA system
- certify compliance
- keep customer personal data — ask the user to remove names of individuals, addresses, phone numbers and emails from samples
- recommend a specific ASP as "the best" — give criteria, not endorsements

## Fallbacks

- No `bga-uae-updates` → state that the latest publications could not be checked; rely on `mcp-dubai` with its date.
- No `mcp-dubai` → use [references/timeline.md](references/timeline.md) with its checked-on date and a strong "verify" warning.

## Escalation

Registered tax agent for VAT treatment questions; the chosen ASP for technical conformance; the FTA for official guidance.

## Sources

See [references/timeline.md](references/timeline.md) and [references/sources.md](references/sources.md).
