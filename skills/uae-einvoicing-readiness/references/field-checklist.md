# Invoice data — field groups to check

This is a **practical data-readiness checklist**, not the official PINT AE specification. Field-level requirements, codes and cardinalities must be taken from the official PINT AE specification and confirmed with your ASP.

| # | Field group | Typical fields | B2B | B2G | Common gap |
|---|---|---|---|---|---|
| 1 | Invoice identity | invoice number, issue date, invoice type (invoice / credit note / debit note), currency | ● | ● | credit notes issued as negative invoices |
| 2 | Supplier | legal name, TRN, address, **Peppol participant ID** | ● | ● | no Peppol ID yet |
| 3 | Buyer | legal name, **buyer TRN**, address, Peppol participant ID | ● | ● | missing or malformed buyer TRN |
| 4 | References | purchase order, contract, original invoice (for credit notes), delivery reference | ◐ | ● | no link from credit note to original invoice |
| 5 | Lines | description, quantity, unit, unit price, line net amount, item identifiers | ● | ● | free-text units; prices incl. VAT in some lines |
| 6 | VAT | VAT category code per line, rate, taxable amount, VAT amount, exemption reason | ● | ● | rates typed as text ("5%"), no category codes |
| 7 | Totals | sum of line nets, allowances/charges, tax total, payable amount | ● | ● | totals don't reconcile with lines (rounding) |
| 8 | Payment | due date, payment terms, bank details (for the supplier, not individuals) | ◐ | ● | terms in free text |
| 9 | Foreign currency | currency code, exchange rate, VAT amount in AED | ◐ | ◐ | VAT not shown in AED |
| 10 | Process | rejection handling, corrections, archiving period | ● | ● | no process owner |

● usually needed · ◐ when applicable

## How the agent checks a sample export
1. Load the file in code (never estimate by eye).
2. Map columns to groups 1–9; list unmapped columns.
3. For each group: present / partially present / missing.
4. Recompute totals per invoice; report mismatches with counts.
5. Validate formats: TRN length and digits (15), ISO currency codes, dates.
6. Mask values in the report (e.g. `TRN 1002****4003`).
