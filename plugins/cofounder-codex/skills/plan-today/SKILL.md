---
name: plan-today
description: "Pick the few things worth the founder's time today, when they ask what to work on, prioritize, or do next. Drives the Cofounder MCP tools `company_get`, `company_memberships_list`, `customer_support_tickets_list`, `email_threads_list`, `playbooks_pending_approvals_list`, `playbooks_reviews_list`, `roadmap_get`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# What Should I Work On Today

Help the founder decide what to work on today.

With a company API key the company is fixed: omit company_id. Otherwise, if the founder has several companies, call `company_memberships_list`, match the company they named, and pass its org_id as company_id on every call. Ask by company name, never by ID, when the match is unclear.

1. Call `playbooks_pending_approvals_list` and `playbooks_reviews_list`; anything waiting on the founder comes first.
2. Call `roadmap_get` for the recommended next milestone and its blockers.
3. Call `company_get` and read its brief and gaps.
4. Call `customer_support_tickets_list` with needs_human_attention=true. Skip the call if setup is missing; do not set it up unasked.
5. Call `email_threads_list` for unanswered mail (omit resource to use the company default mailbox). Skip the call if setup is missing; do not set it up unasked.

Recommend at most three actions in order, each with one line on why now. For an action Cofounder can run, name the playbook and offer to start it.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
