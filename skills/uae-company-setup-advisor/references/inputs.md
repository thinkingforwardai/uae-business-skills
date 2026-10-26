# Inputs — uae-company-setup-advisor

| Input | Allowed values / format | Default if unknown | Why it matters |
|---|---|---|---|
| `activity` | free text; map to the closest activity group (IT/software, consulting, trading general, e-commerce, media, F&B, manufacturing, logistics, real estate services, financial services, healthcare, education) | ask once, then "general consulting" | drives jurisdiction, licence type, regulated-activity flags |
| `client_location` | `uae_onshore` · `outside_uae` · `both` · `uae_government` | `both` | onshore and government sales often require mainland |
| `shareholders_count` | integer | 1 | cost, visas, documents |
| `shareholder_type` | `individual` · `corporate` · `mixed` | `individual` | corporate shareholders need attested corporate documents |
| `shareholder_group` | `uae_gcc` · `other` · `mixed` | `other` | ownership rules for some mainland activities; Corporate Tax nuances |
| `visas_now`, `visas_12m` | integers | 1, 1 | visa quota → office size → cost |
| `office_need` | `none` · `flexi_desk` · `office` · `warehouse` · `retail` | `flexi_desk` | cost and eligibility of cheapest packages |
| `emirate_pref` | `DXB` · `AUH` · `SHJ` · `AJM` · `RAK` · `UAQ` · `FUJ` · `none` | `none` | free zone shortlist |
| `budget_y1_aed` | range, e.g. `20-40k` | `30-60k` | filters options |
| `revenue_aed` | range, e.g. `<375k`, `375k-3m`, `3m-50m`, `>50m` | `375k-3m` | Corporate Tax, VAT, e-invoicing timing |

## Privacy

Never ask for names, passport or Emirates ID numbers, dates of birth, home addresses or bank details. Nationality *group* is enough for this skill.

## One-message intake (suggested wording)

> To compare options I need a few quick details: (1) what the company will do, (2) where your clients are, (3) how many shareholders and whether they are individuals or companies, (4) how many residence visas you need now and in a year, (5) whether you need a physical office, (6) preferred emirate if any, (7) rough year-one budget and (8) expected annual revenue. Skip anything you don't know — I'll assume and say so.
