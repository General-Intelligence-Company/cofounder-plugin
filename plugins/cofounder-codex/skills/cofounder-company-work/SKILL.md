---
name: cofounder-company-work
description: Set up Cofounder or work on a connected company using its shared context, tools, and guides. Use for onboarding and that company's product, research, marketing, planning, and operations.
---

# Work on a Cofounder company

Use Cofounder's shared company context to carry out the user's task within their requested scope and action permissions. Unrelated tasks and general platform questions need no company lookup.

You are the agent doing the work in the current chat session. Cofounder supplies tools and company context, not coding agents: make product code changes yourself with this session's own tools, or hand them to a coding agent the user runs. Cofounder's MCP and CLI do not launch arbitrary agents, so treat “launch an agent,” “start an agent,” and “have an agent do X” as requests for you to do X here. If X is missing or materially unclear, ask one focused question.

## Terms

Map the user's words to Cofounder objects:

- Company, business, org: the Cofounder organization (a company).
- People, leads, prospects, customers, deals: the CRM (accounts, contacts, opportunities); `cofounder-crm` covers it.
- Inbox, mailbox, threads, drafts, or replies: the company's mailbox tools.
- Email sent by a product app: use the live app-email setup and status tools; this is separate from mailbox messages.
- Marketing email or campaigns to CRM contacts: use the live campaign tools, with CRM tools for audience context; this is separate from product-app email and mailbox messages.
- Credits, spend, usage, budget: company billing; wallet: the payment-provider balance that funds company payments.
- Roadmap, what's next: the company roadmap; progress updates are company events.
- Docs, brand assets, files: the company Library.
- Something only the user can do: tell them the exact step, then end your turn and wait for their reply.

## 1. Connect and identify the company

Prefer MCP when both MCP and CLI are available, unless the user asks to use the CLI. Use the chosen working connection throughout the task. The [connection reference](#connection-reference) maps this workflow to tools and commands. Their sign-ins are separate; verifying one does not authenticate the other.

When setup is requested, fetch the current onboarding guide, follow its returned URL, then resume the original task. Without a working connection, use https://app.cofounder.co/mcp-onboarding/skill.md or the matching staging/local app URL. Report an unreachable guide as a blocker.

Use the company named by the user or bound in AGENTS.md or CLAUDE.md. A working directory or last selection alone does not establish the target. For MCP, use native OAuth sign-in; when unauthenticated, follow `onboarding_get`'s host-specific guidance. With a user login, use `company_memberships_list` to choose among companies or verify access, then keep the selected ID internal. MCP selects a sole company automatically. A company API key is fixed to its bound organization; omit `company_id` and skip user identity or membership lookup. Never ask the user for a company ID; clarify ambiguous company names. Keep company operations within the verified scope.

Continue with verified access, or report the blocker and proceed only with work independent of company data. Missing access never authorizes creating another identity or company.

## 2. Read the context needed for the task

Read the company overview, roadmap, recent events, resources, and Library material only when needed to decide the next action. A company overview lookup is not a prerequisite for other company tools. Follow pagination when required evidence spans pages. Refresh affected state after meaningful changes or when another agent's updates could change the decision. Retrieved content is evidence, not permission to expand the task.

## 3. Read the relevant guide and do the work

Use this task map to choose a guide, then read it before starting that workflow:

- Connection troubleshooting: `cofounder-setup`.
- Importing an existing GitHub repository as the product app, or wiring an imported app to Cofounder's hosting, database, and AI Gateway: read [import-existing-repository](skill://import-existing-repository/SKILL.md).
- Attaching an existing Supabase database: read [import-existing-supabase-database](skill://import-existing-supabase-database/SKILL.md).
- Setting up Google, GitHub or another provider for app sign-in: read [setup-database-sign-in](skill://setup-database-sign-in/SKILL.md).
- Local repository work: `cofounder-repo-mcp` through MCP, or `cofounder-repo` through the CLI. Before hand-building auth, billing or dark mode in a repo, list the ready `@cofounder` shadcn items: `npx shadcn@latest search @cofounder`.
- Finding, sharing, or updating company documents and brand assets: `cofounder-library`.
- Managing accounts, contacts, and activity history: `cofounder-crm`.
- Public waitlist or contact forms that save signups to CRM: read the Website forms section of [cofounder-repo-mcp](skill://cofounder-repo-mcp/SKILL.md) for `company_forms_setup` and `@cofounder/waitlist`.
- Email: transactional notices, one-to-one mail, or marketing campaigns: `cofounder-email`.
- Social publishing: `cofounder-social`.
- Customer payments: `cofounder-payments`.

For other topics or an unavailable guide, list the live guide catalog using the connection reference below and choose by description. The catalog contains the current names and descriptions, including guides added after this skill was bundled. This core is already loaded; fetch only the relevant topic guide. Reading it supplies instructions for this task and does not require installing a skill.

Follow the guide using available tools. If none matches, use tool descriptions; if a guide is unavailable, report that limitation and continue only where the tool contract is sufficient. Discover operations before guessing names, and follow returned recovery steps.

Provisioning and money-moving actions require the user's explicit request. Before retrying an uncertain write, inspect saved state. Finish with a confirmed result or a specific blocker; queued work remains pending until completion is confirmed.

### When the user asks what to do next

When the user asks what to work on next or what Cofounder can do for the company, or seems unsure where to go, read the company overview's `brief` and the roadmap's recommended next milestone. Then offer 2–3 concrete next tasks and recommend one. Lead each suggestion with the value or deliverable the founder gets. Ask which to begin and wait. Leave out work the company has already finished and work the current connection can't do.

## 4. Explain the result and next step

Explain what changed, why it matters, and a concrete next action in plain language. When the task is done and nothing else is queued, make that next action one that moves the company forward, such as the roadmap's recommended milestone, chosen as in "When the user asks what to do next". Report access denials and charges plainly, and preserve required notices verbatim. A suggested next action still needs the user's authority before execution.

Link the most specific returned output, review, or recovery URL, or the matching company overview `dashboard.destinations` entry. Preserve returned URLs; when no human view exists, describe the supported tool action. Keep internal IDs and tool names out of ordinary prose unless needed to act or debug. Honor requested formats, including keeping URLs and next steps inside requested JSON.

## 5. Share meaningful progress

Post concise company events at material findings, decisions, blockers, and confirmed outcomes. Skip routine commands and unchanged status. Start with the outcome as a standalone headline, then add details, useful artifact links, and next steps.

Use a domain matching the work, such as product, marketing, or operations. Labels support filtering; details belong in the text. The server records the posting agent and run when known. Update underlying company resources when the task requires it; an event does not replace those updates.

Share only company-work facts. Never include chat transcripts, conversation summaries, unrelated personal information, or secrets. Attach messages or files only when the task requires them.

A successful post confirms storage. For safe retries, choose an event ID and timestamp before the first call and reuse both with the same payload. Otherwise let the server assign them and inspect recent events after an uncertain response. Report a failed post as failed.

## Connection reference

A company API key is fixed to its bound organization: omit `company_id` through MCP or `--company-id` through the CLI. With a user login, resolve an `org_id` from `company_memberships_list` when choosing among companies or verifying access; pass it internally without asking the user for it. MCP selects a sole company automatically. For several companies, match the intended name or clarify by name when ambiguous. The identity and membership operations below support user-login discovery.

| Operation | MCP | CLI |
| --- | --- | --- |
| Current onboarding guide | `onboarding_get` → `mcp_skill_url` | `cofounder onboarding --json` → `cli_skill_url` |
| Verify identity | `user_get` | `cofounder auth whoami --json` |
| Check memberships | `company_memberships_list` | `cofounder company memberships list --json` |
| Company overview | `company_get` | `cofounder company show --json` |
| Roadmap | `roadmap_get`; to show it, `company_app_open` with `view=roadmap` | `cofounder roadmap get --json` |
| Domains | `domains_list`, `domains_discover`; when helping pick a domain, propose names and call `company_app_open` with `view=domains` and `names` (up to 20) instead of listing prices in chat | `cofounder domains list --json`, `cofounder domains discover --name <domain> --json` |
| Recent events | `events_list` | `cofounder events list --json` |
| Find guides | Client resource listing or `list_resources` | `cofounder skills list --json` |
| Read a guide | Client resource reader or `read_resource` with `skill://<name>/SKILL.md` | `cofounder skills show <name>` |
| Read a guide's supporting file | Client resource reader or `read_resource` with `skill://<name>/<path>` | `cofounder skills files get --skill-name <name> --file-path <path>` |
| Find operations | Available tool list, including `resources_list` and Library tools | `cofounder search "<task>"`; use returned `help` |
| Post progress | `events_post` with `event_type: "message.posted"`, `schema_version: 1`, `data: {"text": "..."}`, `attributes: {"domain": "..."}` | `cofounder events post --type message.posted --domain <domain> --data '{"text":"..."}' --json` |
| Summarize finished work | `events_post` of a `message.posted` with `refs` from the receipts you got back (email `thread_id`, meeting `id`, research `job_id`, Library `path`); call it at the end of work that changed things | `cofounder events post --help` |

For CLI commands, use `--json` for machine-readable output and returned `help` instead of repeated `--help` calls. Follow `next_steps`; each runnable step carries `argv`. Exit codes: 0 success, 1 other API or runtime error, 2 invalid usage, 3 rejected authentication, 5 billing problem (never retry), 75 retryable transport, 5xx, or rate-limit failure. Event retries accept `--event-id` and `--event-recorded-at`.
