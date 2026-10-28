---
name: catch-up
description: "Summarize where the company stands, what is running, and what needs the founder, when they ask for a status, update, or what happened. Drives the Cofounder MCP tools `company_get`, `company_memberships_list`, `crm_summary_get`, `playbooks_pending_approvals_list`, `playbooks_reviews_list`, `playbooks_runs_list`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# Catch Me Up on My Company

Catch the founder up on their company.

With a company API key the company is fixed: omit company_id. Otherwise, if the founder has several companies, call `company_memberships_list`, match the company they named, and pass its org_id as company_id on every call. Ask by company name, never by ID, when the match is unclear.

1. Call `company_get` for readiness, resources, gaps, and its brief.
2. Call `playbooks_runs_list` for what is running or finished.
3. Call `playbooks_pending_approvals_list` and `playbooks_reviews_list` for decisions waiting on the founder.
4. Call `crm_summary_get` for recent customer and deal activity.

Lead with what needs the founder now, then what is in progress, then what
changed. Report names and outcomes, not raw payloads or IDs.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
