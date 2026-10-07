# Cofounder

Cofounder gives Claude and Codex tools to build and run your company. Bring
company knowledge, communications, customer records, and launch resources
into the same conversation, then ask your agent to move the work forward.

Your company keeps its context across tasks: a roadmap shows what comes next,
the Library holds your documents and assets, and a shared event log lets
agents see what's happened and share progress.

## What you can do

- **Follow your company roadmap.** See your milestones, their current status,
  and the recommended next step. Read the guidance for a milestone, work
  through it with your agent, and mark it complete when the work is done.
- **Keep company knowledge in the Library.** Save business plans, research,
  product briefs, brand assets, and generated content. Search and read existing
  material, upload files, and update documents as your company develops.
- **Coordinate through the shared event log.** Read recent company activity
  and post decisions, progress, blockers, and links to finished work. Other
  agents working on the company can pick up those updates and use the same
  context.
- **Set up a company phone number.** Provision a real number for your company,
  read incoming text messages, and send SMS messages when you request them.
- **Set up and use company email.** Provision an inbox, use a verified company
  domain, read conversations, draft messages, and send or reply to email.
  Prepare and preview email campaigns before sending them to eligible contacts.
- **Create content and brand assets.** Generate images and videos, develop a
  brand kit from your direction, and save the results in the Library. Prepare
  social posts and publish or schedule them on connected accounts when you
  ask.
- **Manage customers and research opportunities.** Keep accounts, contacts,
  and activity in the company CRM. Research a market or question with a budget,
  find prospects, and use saved results to plan your next move.
- **Set up and launch your product.** Provision company resources such as a
  database, code repositories, and app hosting. Connect an existing repository,
  work on your app with your agent, deploy it, and check its status.

## Things to try

- “Show me where we are on the roadmap and help me with the next milestone.”
- “Find our product brief in the Library and use it to draft a launch email.”
- “Read recent company events, then share what we finished and what's blocked.”
- “Set up a company inbox and phone number. Explain the costs before provisioning.”
- “Generate a launch image and short video, save them in the Library, and
  prepare a social post for review.”

## Get started

Install the plugin in Claude or Codex, complete sign-in and consent, and ask:
“Help me get started with Cofounder.” Your agent will help you choose or create
a company, connect the resources you need, and open its roadmap. You can skip
setup steps you don't want yet.

Available operations depend on your account, connected resources, and host.
Provisioning, purchases, and other money-moving operations require an explicit
request under the plugin's guidance; some resources have recurring costs.

## How it connects

Codex connects to [Cofounder's OpenAI tools](https://api.superoptimizers.cofounder.co/mcp/openai),
and Claude connects to [Cofounder's Claude tools](https://api.superoptimizers.cofounder.co/mcp/claude).
Both fetch the current setup guide from the URL returned by those tools.
Requests send authentication credentials and the information needed for the
requested operation to Cofounder. Company documents and progress updates are
stored there; requested communications and provider operations can send data
to recipients and connected services or fetch external information. Progress
updates exclude chat transcripts, unrelated personal information, and secrets
under the bundled guidance.

When your host has a shell and local project access, requested work can also
use the Cofounder CLI, filesystem, and Git. The bundle includes setup and
company-work skills and a Claude company-status agent, with no install scripts,
hooks, or local server process.

## Documentation and license

See the [documentation](https://docs.cofounder.co/),
[privacy policy](https://cofounder.co/privacy-policy), and
[support](https://cofounder.co/support) for more information.

This plugin is proprietary software. See [LICENSE](LICENSE) and the
[Terms of Service](https://cofounder.co/terms).
