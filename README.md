# UAE Business Skills

**Open-source Agent Skills for doing business in the United Arab Emirates — company setup, Golden Visa pre-checks and e-invoicing readiness — built on public MCP servers.**

By [Thinking Forward](https://thinkingforward.ai) · MIT License · Unofficial, independent project

> ⚠️ **Not official. Not advice.** These skills are not affiliated with, endorsed by, or connected to the UAE Government or any authority, free zone or platform they mention. They produce *preliminary, informational* output with sources and review dates. Always verify with the competent authority or a licensed professional (PRO, registered tax agent, lawyer). See [DISCLAIMER.md](DISCLAIMER.md).

---

## What's inside

| Skill | What it does | Main MCP servers |
|---|---|---|
| [`uae-company-setup-advisor`](skills/uae-company-setup-advisor/SKILL.md) | Compares mainland, free zone and offshore setup; shortlists free zones; estimates cost, timeline and Corporate Tax impact; outputs a document checklist and a hand-off brief for a licensed setup provider | MCP-Dubai, UAE Law MCP |
| [`uae-golden-visa-precheck`](skills/uae-golden-visa-precheck/SKILL.md) | Matches a person's profile to Golden Residency routes, lists gaps and documents, cites the legal basis | Open Emirates, MCP-Dubai, dld-mcp (property route), UAE Law MCP |
| [`uae-einvoicing-readiness`](skills/uae-einvoicing-readiness/SKILL.md) | Determines if and when a business falls under UAE e-invoicing (Peppol / PINT AE), checks invoice data for gaps, produces a readiness plan | MCP-Dubai, BGA UAE Updates, UAE Law MCP |

Each skill follows the same rules:

- **Every number has a source and a date.**
- **Every legal requirement has a citation** and an "in force" check where a legal MCP is available.
- **Freshness is checked** before answering (knowledge older than its review threshold triggers a warning).
- **The agent never** submits applications, enters passwords or OTPs, ticks declarations, makes payments, or stores identity documents.
- **Escalation is built in**: the output ends with what a licensed professional must confirm.

---

## Install

### Claude Code (plugin marketplace)

```bash
/plugin marketplace add thinkingforwardai/uae-business-skills
/plugin install uae-business-skills@thinkingforward
```

### Any Agent Skills client (skills CLI)

```bash
npx skills add thinkingforwardai/uae-business-skills
```

### Manual

Copy any folder from `skills/` into your client's skills directory (for Claude Code: `~/.claude/skills/` or `.claude/skills/` in your project).

---

## Connect the MCP servers

The skills work best with these public MCP servers connected. All are independent community or commercial projects — check their licenses and terms.

| Server | Install / endpoint | Auth | Used for |
|---|---|---|---|
| **MCP-Dubai** | `uvx mcp-dubai` | none for 112 of 120 tools | setup, free zones, visas, banking, tax, compliance, holidays, Arabic letters |
| **UAE Law MCP** (Ansvar) | `npx -y @ansvar/uae-law-mcp` | none (local) | legislation search, citations, in-force checks |
| **Open Emirates** | `bunx --bun uaemcp@latest` | none (self-host) | Golden Residency routes, official open data with provenance |
| **dld-mcp** | `uvx dld-mcp` or `https://offerbrief.com/mcp` | none, 300 req/IP/day | Dubai property transactions and Ejari rents |
| **BGA UAE Business Updates** | `https://mcp.bga.ae/mcp` | none | latest FTA / MoF / MOHRE publications |

Ready-to-use config: [`examples/mcp.json`](examples/mcp.json). Full guide: [`docs/mcp-setup.md`](docs/mcp-setup.md).

If a server is unavailable, every skill falls back to a reduced mode and tells the user what could not be checked.

---

## Example prompts

```text
I'm a software consultancy from Poland with 2 partners. We want a UAE company,
need 3 visas, clients are mostly in Europe. Mainland or free zone? Budget ~AED 40k.
```

```text
I'm considering buying an apartment in Dubai Marina for about AED 2.2M.
Would that qualify me for a Golden Visa? What else would I need?
```

```text
We're a Dubai distributor with ~AED 80M annual revenue on Zoho Books.
When do we need to comply with e-invoicing and what's missing in our invoice data?
```

More in [`examples/`](examples/).

---

## Repository structure

```
skills/
  uae-company-setup-advisor/   SKILL.md + references/
  uae-golden-visa-precheck/    SKILL.md + references/
  uae-einvoicing-readiness/    SKILL.md + references/
templates/SKILL_TEMPLATE.md    standard for new skills
docs/                          MCP setup, design principles
examples/                      prompts and MCP config
scripts/validate_skills.py     checks front-matter and required sections
```

---

## Roadmap

- `uae-compliance-calendar` — Corporate Tax, VAT, UBO, ESR, AML and Emiratisation deadlines for a company profile
- `dubai-property-investment-brief` — transaction prices, rental yield and surroundings for a specific property
- `uae-gov-letter-ar-en` — formal bilingual letters to authorities
- Arabic-first versions of all skills

Suggestions welcome — open an issue.

---

## Contributing

Corrections from practitioners (PROs, tax agents, lawyers) are the most valuable contribution. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Need this inside your business?

Thinking Forward helps companies in the UAE and the Gulf design and deploy AI agents on top of their own processes and data — from setup providers and accounting firms to teams preparing for e-invoicing.
→ [thinkingforward.ai](https://thinkingforward.ai)

---

## ملخص بالعربية

**مهارات أعمال الإمارات** — مجموعة مفتوحة المصدر من مهارات وكلاء الذكاء الاصطناعي لمساعدة الشركات في الإمارات: المقارنة بين تأسيس الشركات في البر الرئيسي والمناطق الحرة، والتقييم الأولي لأهلية الإقامة الذهبية، والاستعداد لنظام الفوترة الإلكترونية.

هذا مشروع مستقل وغير رسمي، ولا يرتبط بحكومة دولة الإمارات أو أي جهة حكومية. المعلومات المقدمة أولية ولأغراض إعلامية فقط، ولا تُعد استشارة قانونية أو ضريبية أو استشارة في شؤون الهجرة. يُرجى دائماً التحقق من الجهة المختصة أو من مستشار مرخّص.

---

## License

[MIT](LICENSE) © 2026 Thinking Forward. Third-party MCP servers and data sources remain subject to their own licenses and terms.
