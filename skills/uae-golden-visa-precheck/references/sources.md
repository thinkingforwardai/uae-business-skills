# Sources — uae-golden-visa-precheck

Checked on 2026-10-26. Thresholds and criteria change — always take current values from the tools and verify with the authority.

## MCP servers
- Open Emirates (uaemcp, MIT) — `uae_golden_residency` (14 official Golden Residency routes with provenance), `uae_discover`, `uae_query`.
  https://github.com/zadstack/uaemcp
- MCP-Dubai (v0.4.0, MIT) — `list_visa_types`, `visa_details`, `visa_recommend`, `golden_visa_check`, `portal_guide`, `get_knowledge_status`.
  https://pypi.org/project/mcp-dubai/
- dld-mcp (MIT) — `query_dld` (DLD sales transactions and Ejari contracts via OfferBrief; 300 queries/IP/day).
  https://glama.ai/mcp/servers/level09/dld-mcp
- UAE Law MCP (Ansvar Systems) — legislation search and in-force checks.
  https://playbooks.com/mcp/ansvar-systems/uae-law-mcp

## Authorities (for the user to verify)
- Federal Authority for Identity, Citizenship, Customs and Port Security (ICP) — https://icp.gov.ae
- General Directorate of Identity and Foreigners Affairs Dubai (GDRFA) — https://gdrfad.gov.ae
- UAE government portal, Golden Visa page — https://u.ae

## Notes for maintainers
- Do not hard-code thresholds in SKILL.md. Keep them in tool data or in this file with a source URL and date.
- Commonly cited example (verify before use): property route with a minimum property value of AED 2 million. Source to confirm on u.ae / ICP.
