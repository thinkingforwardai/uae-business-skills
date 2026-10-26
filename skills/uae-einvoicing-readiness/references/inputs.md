# Inputs — uae-einvoicing-readiness

| Input | Format | Default if unknown |
|---|---|---|
| `revenue_band` | `<50m` · `>=50m` (AED, annual) | ask — it determines the deadline |
| `customer_mix` | % B2B / B2G / B2C | `B2B 100%` |
| `vat_status` | `registered` · `group` · `not_registered` | `registered` |
| `system` | ERP / accounting software name, `manual`, or `multiple` | `unknown` |
| `monthly_volume` | `<500` · `500–5k` · `5k–50k` · `>50k` | `500–5k` |
| `sample` | CSV / XLSX export or 1–3 invoices, personal data removed | optional |

## Privacy
Ask the user to remove names of individual customers, personal addresses, phone numbers and emails before sharing samples. Company names and TRNs of businesses may remain; mask them in the output.
