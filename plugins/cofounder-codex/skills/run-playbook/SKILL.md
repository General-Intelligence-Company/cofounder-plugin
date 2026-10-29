---
name: run-playbook
description: "Choose a Cofounder playbook and start a run of it, when the founder wants a recurring or multi-step company job done, such as brand voice or outreach. Drives the Cofounder MCP tools `company_memberships_list`, `playbooks_approvals_decide`, `playbooks_get`, `playbooks_list`, `playbooks_pending_approvals_list`, `playbooks_runs_list`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# Run a Playbook

Start a Cofounder playbook run. The founder has not picked one.

With a company API key the company is fixed: omit company_id. Otherwise, if the founder has several companies, call `company_memberships_list`, match the company they named, and pass its org_id as company_id on every call. Ask by company name, never by ID, when the match is unclear.

1. Call `playbooks_list` and match the request to one playbook's goal. With no
   request, offer the two or three most useful for the company's state.
2. Call `playbooks_get` with its playbook_key to read prerequisites,
   schedule, and default budget. Tell the founder the budget in dollars.
3. Once the founder agrees, call the playbook's own run tool, named by the
   run_entrypoint in the `playbooks_list` result. Pass only the settings the
   founder gave.
4. Follow progress with `playbooks_runs_list`, and relay approvals through
   `playbooks_pending_approvals_list`; record a decision with
   `playbooks_approvals_decide` only on the founder's explicit answer.

Report the run's status and what the founder must do next.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
