---
name: research-topic
description: "Research a market, competitor, or question and save the findings to the Library, when the founder asks for research or a brief. Drives the Cofounder MCP tools `company_memberships_list`, `library_search`, `library_text_write`, `research_jobs_get`, `research_jobs_results_get`, `research_start`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# Research a Topic

Research for the founder: the topic the founder gave

With a company API key the company is fixed: omit company_id. Otherwise, if the founder has several companies, call `company_memberships_list`, match the company they named, and pass its org_id as company_id on every call. Ask by company name, never by ID, when the match is unclear.

1. Call `research_start` with the topic as query, max_cost_usd set to
   a modest amount the founder approves, and an idempotency_key. Research spends company credit; reuse the
   key only to retry identical arguments.
2. Call `research_jobs_get` until the job finishes, then read it with
   `research_jobs_results_get`.
3. Save a short brief with `library_text_write` under `general/`, then verify
   it with `library_search`.

Report the key findings, sources, cost, and the Library path.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
