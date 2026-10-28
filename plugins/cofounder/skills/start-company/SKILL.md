---
name: start-company
description: "Start a new company from an idea or bring an existing company or product onto Cofounder, when the founder says they want to start, launch, or move a company here. Drives the Cofounder MCP tools `company_create`, `onboarding_get`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# Start My Company

Help the founder start their company on Cofounder.

Ask the founder, as a one-line choice, whether they are starting a new company from an idea or bringing an existing company or product; then continue on that path. For an existing one, ask whether there is a repository to attach. When creating the company, pass existing_project to `company_create` with the repository's owner/name. Do not assume the current working directory is that project.

Call `onboarding_get` with {} and follow its state, instruction,
call_next, and rules; call it again after each step, because the state is
recomputed every time. It owns the current sign-in, company selection, setup,
and first-task flow. The guide at mcp_skill_uri (read with `read_resource`, or
fetch mcp_skill_url) is long-form reference only. Keep the founder's requested
company name, goal, and existing project in context.

Report the company_id used and the outcome (for a repository: attached,
skipped, or needs the user's input), not raw payloads.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
