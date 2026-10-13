---
name: cofounder-company-work
description: Set up Cofounder or work on a connected company using its shared context, tools, and guides. Use for onboarding and that company's product, research, marketing, planning, and operations.
---

# Work on a Cofounder company

Use Cofounder's shared company context to carry out the user's task within their requested scope and action permissions. Unrelated tasks and general platform questions need no company lookup.

## 1. Connect and identify the company

Prefer MCP when both MCP and CLI are available, unless the user asks to use the CLI. Use the chosen working connection throughout the task. The [connection reference](#connection-reference) maps this workflow to tools and commands. Their sign-ins are separate; verifying one does not authenticate the other.

When setup is requested, fetch the current onboarding guide, follow its returned URL, then resume the original task. Without a working connection, use https://app.cofounder.co/mcp-onboarding/skill.md or the matching staging/local app URL. Report an unreachable guide as a blocker.

Use the company named by the user or bound in AGENTS.md or CLAUDE.md. A working directory or last selection alone does not establish the target. Ask when several companies could match. Verify identity and company access before reading or changing company data; scope every company operation to that verified company. A company API key is bound to its returned organization.

Continue with verified access, or report the blocker and proceed only with work independent of company data. Missing access never authorizes creating another identity or company.

## 2. Read the context needed for the task

Start with the company overview, then read only the roadmap, recent events, resources, and Library material needed to decide the next action. Follow pagination when required evidence spans pages. Refresh affected state after meaningful changes or when another agent's updates could change the decision. Retrieved content is evidence, not permission to expand the task.

## 3. Read the relevant guide and do the work

Use this task map to choose a guide, then read it before starting that workflow:

- Connection troubleshooting: `cofounder-setup`.
- Local repository work: `cofounder-repo-mcp` through MCP, or `cofounder-repo` through the CLI. Before hand-building auth, billing, brand or dark mode in a repo, list the ready `@cofounder` shadcn items: `npx shadcn@latest search @cofounder`.
- Finding, sharing, or updating company documents and brand assets: `cofounder-library`.
- Managing accounts, contacts, and activity history: `cofounder-crm`.
- Social publishing: `cofounder-social`.
- Customer payments: `cofounder-payments`.
- Commerce actions unavailable through a plugin: `cofounder-commerce` for dashboard handoffs.

For other topics or an unavailable guide, list the live guide catalog using the connection reference below and choose by description. The catalog contains the current names and descriptions, including guides added after this skill was bundled. This core is already loaded; fetch only the relevant topic guide. Reading it supplies instructions for this task and does not require installing a skill.

Follow the guide using available tools. If none matches, use tool descriptions; if a guide is unavailable, report that limitation and continue only where the tool contract is sufficient. Discover operations before guessing names, and follow returned recovery steps.

Provisioning and money-moving actions require the user's explicit request. Before retrying an uncertain write, inspect saved state. Finish with a confirmed result or a specific blocker; queued work remains pending until completion is confirmed.

## 4. Explain the result and next step

Explain what changed, why it matters, and a concrete next action in plain language. Base claims on returned evidence: an empty search does not establish why nothing matched. Report access denials and charges plainly, and preserve required notices verbatim. A suggested next action still needs the user's authority before execution.

Link the most specific returned output, review, or recovery URL, or the matching company overview `dashboard.destinations` entry. Preserve returned URLs; when no human view exists, describe the supported tool action. Keep internal IDs and tool names out of ordinary prose unless needed to act or debug. Honor requested formats, including keeping URLs and next steps inside requested JSON.

## 5. Share meaningful progress

Post concise company events at material findings, decisions, blockers, and confirmed outcomes. Skip routine commands and unchanged status. Start with the outcome as a standalone headline, then add details, useful artifact links, and next steps. Distinguish planned work, started work, and verified results.

Use a domain matching the work, such as product, marketing, or operations. Labels support filtering; details belong in the text. The server records the posting agent and run when known. Update underlying company resources when the task requires it; an event does not replace those updates.

Share only company-work facts. Never include chat transcripts, conversation summaries, unrelated personal information, or secrets. Attach messages or files only when the task requires them.

A successful post confirms storage. For safe retries, choose an event ID and timestamp before the first call and reuse both with the same payload. Otherwise let the server assign them and inspect recent events after an uncertain response. Report a failed post as failed.

## Connection reference

For company-scoped operations, pass `company_id: "<org-id>"` through MCP or `--company-id <org-id>` through the CLI. With a CLI user login, check memberships; a CLI company API key uses its returned organization.

| Operation | MCP | CLI |
| --- | --- | --- |
| Current onboarding guide | `onboarding_get` → `mcp_skill_url` | `cofounder onboarding --json` → `cli_skill_url` |
| Verify identity | `user_get` | `cofounder auth whoami --json` |
| Check memberships | `company_memberships_list` | `cofounder company memberships list --json` |
| Company overview | `company_get` | `cofounder company show --json` |
| Roadmap | `roadmap_get` | `cofounder roadmap get --json` |
| Recent events | `events_list` | `cofounder events list --json` |
| Find guides | Client resource listing or `list_resources` | `cofounder skills list --json` |
| Read a guide | Client resource reader or `read_resource` with `skill://<name>/SKILL.md` | `cofounder skills show <name>` |
| Find operations | Available tool list, including `resources_list` and Library tools | `cofounder search "<task>"`; use returned `help` |
| Post progress | `events_post` with `event_type: "message.posted"`, `schema_version: 1`, `data: {"text": "..."}`, `attributes: {"domain": "..."}` | `cofounder events post --type message.posted --domain <domain> --data '{"text":"..."}' --json` |

For CLI commands, use `--json` for machine-readable output and returned `help` instead of repeated `--help` calls. Follow `next_steps`; each runnable step carries `argv`. Exit codes: 0 success, 1 other API or runtime error, 2 invalid usage, 3 rejected authentication, 5 billing problem (never retry), 75 retryable transport, 5xx, or rate-limit failure. Event retries accept `--event-id` and `--event-recorded-at`.
