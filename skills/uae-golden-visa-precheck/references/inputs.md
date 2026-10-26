# Inputs — uae-golden-visa-precheck

| Input | Format | Notes |
|---|---|---|
| `route_interest` | `property` · `investor_business` · `skilled_professional` · `entrepreneur` · `talent` · `researcher` · `student` · `humanitarian_frontline` · `not_sure` | `not_sure` → screen all routes with the facts given |
| `current_status` | `uae_resident` · `outside_uae` · `visit_visa` | affects in-country steps |
| `property.emirate` | emirate code | |
| `property.area` | area/community name as the user writes it | normalise for `dld-mcp` (e.g. "JVC" → "Jumeirah Village Circle") |
| `property.type` | `apartment` · `villa` · `townhouse` · `land` · `commercial` | |
| `property.price_range_aed` | range | |
| `property.status` | `completed` · `off_plan` | |
| `property.mortgage` | `yes` · `no` | |
| `property.ownership` | `sole` · `joint` · `company` | joint/company → escalate |
| `professional.occupation_group` | free text → occupation level as used by the tool | |
| `professional.education` | `bachelor_or_higher` · `other` | |
| `professional.salary_range_aed_month` | range | ranges only, no payslips |
| `investment.type_amount` | e.g. "deposit in UAE fund, AED 2–3m" | |
| `achievement` | one sentence | for talent / entrepreneur / researcher / student |
| `family_counts` | spouse: n, children: n, parents: n | counts only |

## Privacy
Counts and ranges only. No names, numbers of documents, dates of birth, or financial statements.
