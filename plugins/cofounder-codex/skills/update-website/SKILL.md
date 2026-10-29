---
name: update-website
description: "Review the company site, make a change, and deploy it, when the founder wants to launch, edit, or publish their website. Drives the Cofounder MCP tools `code_push_token_create`, `code_repository_get`, `company_memberships_list`, `hosting_deploy`, `hosting_deployments_list`, `hosting_deployments_readiness_get`, `hosting_deploys_get`, `playbooks_get`, `playbooks_list`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# Launch or Update My Website

Help the founder launch or update their website.

With a company API key the company is fixed: omit company_id. Otherwise, if the founder has several companies, call `company_memberships_list`, match the company they named, and pass its org_id as company_id on every call. Ask by company name, never by ID, when the match is unclear.

1. Call `code_repository_get` for the repository, production branch, last deployment, and open pull requests.
2. For a design overhaul, find the website playbook with `playbooks_list` and start it as in `playbooks_get`'s run_entrypoint.
3. For a specific change, edit the repository directly; `code_push_token_create` issues push access.
4. After the change reaches the production branch, call `hosting_deploy` with an idempotency_key, then poll `hosting_deploys_get` until the job succeeds. The job output does not update afterward, so then poll `hosting_deployments_readiness_get` with its deployment_id and source_sha only while overall_state is pending. Report the final overall_state and follow its next_action; use `hosting_deployments_list` to find failures.

Deploying publishes to the public site, so confirm the change with the founder
first. Report the live URL and what changed.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
