# Connecting the MCP servers

The skills call tools from independent MCP servers. None of them is official; check each project's license and terms, and the terms of the underlying data publishers, before commercial use.

## 1. MCP-Dubai — required by all skills

- Package: `mcp-dubai` (PyPI), Python 3.11+, stdio. 120 tools; 112 need no credentials.
- Claude Code:
  ```bash
  claude mcp add dubai -- uvx mcp-dubai
  ```
- Optional environment variables:
  - `MCP_DUBAI_PULSE_CLIENT_ID`, `MCP_DUBAI_PULSE_CLIENT_SECRET` — OAuth credentials for the 6 Dubai government dataset tools (DLD, RTA) via data.dubai.
  - `MCP_DUBAI_WAQI_TOKEN` — air-quality tools.
- Health check: call `about()` and `get_upstream_status()`.
- Project: https://pypi.org/project/mcp-dubai/

## 2. UAE Law MCP (Ansvar Systems) — recommended

- Package: `@ansvar/uae-law-mcp` (npm), stdio.
  ```bash
  claude mcp add uae-law -- npx -y @ansvar/uae-law-mcp
  ```
- Federal law, DIFC and ADGM; tools include `search_legislation`, `get_provision`, `check_currency`, `validate_citation`, `format_citation`.
- Project: https://github.com/Ansvar-Systems/UAE-law-mcp

## 3. Open Emirates (uaemcp) — recommended for Golden Visa

- Self-host (free, unmetered):
  ```bash
  claude mcp add open-emirates -- bunx --bun uaemcp@latest
  ```
- Hosted endpoint requires an `X-API-Key` (`https://uae-open-data.zadstack.com/mcp`).
- Project: https://github.com/zadstack/uaemcp

## 4. dld-mcp — optional, property context

- ```bash
  claude mcp add dld -- uvx dld-mcp
  # or remote, no install:
  claude mcp add --transport http dld https://offerbrief.com/mcp
  ```
- Data via OfferBrief; limit 300 queries per IP per day. For commercial products, arrange your own data access.
- Project: https://glama.ai/mcp/servers/level09/dld-mcp

## 5. BGA UAE Business Updates — optional, latest regulatory publications

- ```bash
  claude mcp add --transport http bga https://mcp.bga.ae/mcp
  ```
- Read-only, no keys, fair use.
- Project: https://bga.ae/mcp-en/

## Name mapping

Skills refer to servers by these names. If you register them under different names, the agent will still find the tools by their tool names.

| Name used in skills | Server |
|---|---|
| `mcp-dubai` | MCP-Dubai |
| `uae-law-mcp` | UAE Law MCP |
| `open-emirates` | Open Emirates / uaemcp |
| `dld-mcp` | dld-mcp |
| `bga-uae-updates` | BGA UAE Business Updates |

## Smoke test

```text
Run about() on MCP-Dubai, search UAE legislation for "corporate tax",
and list Golden Residency routes from Open Emirates. Report which servers responded.
```
