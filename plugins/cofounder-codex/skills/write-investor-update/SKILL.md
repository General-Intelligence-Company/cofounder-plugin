---
name: write-investor-update
description: "Draft an investor update from the company's own data, when the founder asks for an investor, board, or monthly update. Drives the Cofounder MCP tools `analytics_website_traffic_get`, `company_get`, `company_memberships_list`, `crm_opportunities_query`, `crm_summary_get`, `library_text_write`, `playbooks_runs_list`, `roadmap_get`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# Write My Investor Update

Draft an investor update from the company's own data.

With a company API key the company is fixed: omit company_id. Otherwise, if the founder has several companies, call `company_memberships_list`, match the company they named, and pass its org_id as company_id on every call. Ask by company name, never by ID, when the match is unclear.

1. Call `company_get` and `roadmap_get` for progress and milestones.
2. Call `playbooks_runs_list` for what shipped.
3. Call `crm_summary_get` and `crm_opportunities_query` for pipeline.
4. Call `analytics_website_traffic_get` for site traffic.
5. Save the draft with `library_text_write` under `general/`.

Use only numbers these tools returned and mark anything missing as unknown.
Structure: highlights, metrics, challenges, asks. Return the Library path and
the draft for the founder to edit.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
