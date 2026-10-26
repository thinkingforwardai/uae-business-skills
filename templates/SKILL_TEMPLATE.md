---
name: uae-<topic>-<job>
description: Use when <who> asks <what>, wants <outcome>. Mention the key phrases users type. Say what it is NOT for.
version: 0.1.0
knowledge_reviewed: YYYY-MM-DD
review_threshold_days: 100   # 60 for fast-changing tax rules, 190 medium, 365 stable
reviewer: pending            # name / firm of the licensed professional who reviewed the content
license: MIT
author: Thinking Forward (thinkingforward.ai)
requires_mcp: [mcp-dubai]
optional_mcp: [uae-law-mcp]
---

# <Skill title>

One paragraph: what the skill produces and the one sentence that limits it ("preliminary, not a decision").

## When to use
- 3–5 example user requests

## Inputs — ask only for what is missing
Numbered list. Collect in one message. Link to `references/inputs.md`.
State privacy limits: what the agent must never ask for.

## Steps
### 1. Freshness check
`get_knowledge_status()` and upstream status; warn if past threshold.
### 2…n. Workflow
Each step names the exact MCP tool calls and what to capture from them.
### Last. Output
Link to `references/output-template.md`.

## Output rules
Length, tables, sources and dates, citations, "what must be confirmed", hand-off.

## Hard rules — the agent does NOT
- submit, sign, pay, log in, enter passwords/OTPs, tick declarations
- collect identity numbers or documents
- present output as an official decision
- claim affiliation with any authority

## Fallbacks
What to do when each MCP server is unavailable.

## Escalation
Which licensed professional or authority confirms what.

## Sources
Link to `references/sources.md` (every fact: URL + checked-on date).
