# Output template — uae-einvoicing-readiness

```markdown
# UAE e-invoicing readiness — preliminary assessment
*Prepared {date} · rules checked against {sources + dates} · unofficial, not advice*

{warning if latest publications could not be checked or knowledge is older than 60 days}

## Bottom line
Based on revenue {band} and {customer mix}, e-invoicing is expected to apply to you from **{go-live date}**, with an ASP to be appointed by **{date}** ({days} days from today). Verify against the latest FTA publication.

## What changes for you
- Invoices to businesses (and government) must be structured e-invoices exchanged through an accredited provider; PDFs stop counting.
- …

## Data readiness (from your sample of {n} invoices)
| Field group | Status | Issues found | Fix |
|---|---|---|---|
Totals check: {n} invoices recomputed, {k} mismatches.

## Readiness plan
| # | Workstream | Owner | Start | Done by |
|---|---|---|---|---|
| 1 | Appoint ASP | Finance | | {ASP date} |
| 2 | Master data cleanup | Finance + Sales ops | | |
| 3 | ERP mapping and test invoices | IT + ASP | | |
| 4 | Process changes | Finance | | |
| 5 | Archiving and audit trail | Finance + IT | | |
| 6 | Go-live and monitoring | All | | {go-live} |

## Questions to ask ASP candidates
- FTA accreditation and Peppol certification status
- Connector for {system}
- Pricing at {volume}
- Rejection and correction workflow
- Data residency and archiving

## What must be confirmed
- With your tax agent: …
- With your ASP: …

---
Sources: … · Not tax advice. Verify with the FTA, a registered tax agent and your ASP.
```
