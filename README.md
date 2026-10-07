<p align="center">
  <img src="plugins/cofounder/assets/directory-icon.png" alt="Cofounder sunflower" width="96" height="96">
</p>

<h1 align="center">Cofounder Plugin</h1>

<p align="center">
  <a href="https://cofounder.co">cofounder.co</a>
</p>

Cofounder gives your AI agent a foundation for building and running a company:
shared company knowledge, a roadmap, and tools for research, customer
relationships, email, social publishing, brand creation, and infrastructure.

Install from this repository to bring Cofounder into **Codex**, **Claude Code**,
or the **Claude app and Cowork**. The plugin bundles a connection to Cofounder's
hosted tools and skills for getting started and working on your company.
[Explore what you can do](plugins/cofounder/README.md).

## Install in a desktop app

This repository is public. You can download the plugin without a GitHub account
or repository access request. Using company tools requires Cofounder sign-in
and consent.

### Codex desktop app

**Ask Codex to install it:** paste this into a local Codex chat with shell
access and a current Codex CLI available:

```text
Install the Cofounder plugin from
https://github.com/General-Intelligence-Company/cofounder-plugin
in my local Codex setup.

Run these supported commands:
codex plugin marketplace add General-Intelligence-Company/cofounder-plugin
codex plugin add cofounder@cofounder
codex plugin list --json

Verify that cofounder@cofounder is installed and enabled. If sign-in or
consent is needed, tell me how to complete it. Tell me when to start a
new chat to use the plugin.
```

Codex can perform the installation through its shell tools. Complete any
approval, sign-in, or consent prompts your setup presents. If the CLI is
unavailable or shell access is restricted, use the UI steps below.

**Install through the UI:**

1. Open **Plugins** in the Codex desktop app.
2. Choose **Add > Add a marketplace**.
3. In **Source**, enter:

   ```text
   General-Intelligence-Company/cofounder-plugin
   ```

4. Leave **Git ref** and **Sparse paths** empty, then select **Add marketplace**.
5. Select the **Cofounder** marketplace, open **Cofounder**, and choose
   **Install**.
6. Complete the Cofounder connection prompts, including sign-in and consent.
   Start a new chat to use the plugin.

### Claude desktop app and Cowork

**Ask Claude Code to install it:** paste this into a local Claude Code session
(including the desktop app's **Code** tab) with shell access and a current
Claude Code CLI available:

```text
Install the Cofounder plugin from
https://github.com/General-Intelligence-Company/cofounder-plugin
in my local Claude Code setup.

Run these supported commands:
claude plugin marketplace add General-Intelligence-Company/cofounder-plugin
claude plugin install cofounder@cofounder --scope user
claude plugin list --json

Verify that cofounder@cofounder is installed and enabled. If sign-in or
consent is needed, tell me how to complete it through /mcp. Tell me
whether to reload plugins or start a new session to use the plugin.
```

This installs into Claude Code on your machine. For Claude **Chat** or
**Cowork**, use the UI steps below to add the plugin to your Claude account;
a Claude Code CLI installation doesn't sync back to that account.

**Install through the UI:**

1. Open **Customize > Plugins** in Claude. For Cowork, open the **Cowork** tab
   first, then **Customize**.
2. Choose **Add > Add marketplace > Add from a repository**.
3. Enter this repository URL and select **Sync**:

   ```text
   https://github.com/General-Intelligence-Company/cofounder-plugin
   ```

4. Open **Cofounder** in the added marketplace and select **Add** or **Install**.
5. Open the plugin's **Connectors** tab and connect Cofounder, completing
   sign-in and consent. Start a new conversation or Cowork task.

Use the repository's main URL above, without `/tree/main`, a subfolder, or a
`.git` suffix. Your organization may control which marketplaces you can add.

Plugins installed in the Claude app are saved to your account. They also sync
to Claude Code when you sign in with the same Claude account on a version that
supports account plugin sync (v2.1.273 or later).

[Claude app installation documentation](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

## Get started

After connecting, ask:

> Help me get started with Cofounder.

Your agent can help you choose or create a company and find the next step on
its roadmap. Then try:

- "Show me our company roadmap and help me with the next milestone."
- "Find our product brief in the Library and draft a launch email from it."
- "Read recent company events and summarize what's finished and what's blocked."

The plugin connects to Cofounder's production service. You don't need to clone
this repository, run a local server, or copy MCP configuration by hand.

## Keep the desktop plugin updated

**Codex:** open the plugin settings, find the **Cofounder** marketplace, and
choose **Upgrade marketplace**. Check Cofounder in the plugin directory and
start a new chat afterward.

**Claude app and Cowork:** use **Check for updates** on the marketplace. You can
also enable **Sync automatically** for this GitHub marketplace. Start a new
Cowork task to load updated components.

## Troubleshooting

- **Plugin missing:** adding a marketplace makes its plugins discoverable;
  you still need to install Cofounder. The install identifier is
  `cofounder@cofounder`: plugin name first, marketplace name second.
- **Command missing:** update your Codex or Claude Code client if it doesn't
  recognize the [CLI commands below](#install-from-the-command-line-for-agents).
- **Tools unavailable:** confirm the plugin is enabled and Cofounder is
  connected. In Claude Code, use `/mcp`; in the Claude app, use the plugin's
  **Connectors** tab. Complete any outstanding sign-in or consent prompts.
- **Marketplace blocked:** check your organization's plugin policy. A company
  administrator may need to allow this source.

## Source and releases

This repository is generated from the `production` plugin source in
[Superoptimizers](https://github.com/General-Intelligence-Company/superoptimizers).
It contains catalogs for both hosts and a shared bundle under
[`plugins/cofounder/`](plugins/cofounder/). Both marketplace names and the
plugin name are `cofounder`.

Versions and plugin content are authored in Superoptimizers. Release
provenance is recorded in [`publication.json`](publication.json).
Publication also regenerates this README from
[`scripts/export_cofounder_plugin_repository.py`](https://github.com/General-Intelligence-Company/superoptimizers/blob/main/scripts/export_cofounder_plugin_repository.py),
so lasting README changes must be made in that source template.

## Documentation and support

See [Cofounder documentation](https://docs.cofounder.co/),
[support](https://cofounder.co/support), and the
[privacy policy](https://cofounder.co/privacy-policy).
This plugin is proprietary software; see [LICENSE](LICENSE) and the
[Terms of Service](https://cofounder.co/terms).

## Install from the command line (for agents)

An agent with shell access can run the commands below to install Cofounder
into Codex or Claude Code on this machine. Use the commands for the host you're
configuring. These are terminal commands, so they also work from a setup
script or another agent's shell tool.

Both the plugin and marketplace are named `cofounder`; the install identifier
is `cofounder@cofounder`. Register the marketplace, install the plugin, then
check the installed-plugin list.

### Codex CLI

```sh
codex plugin marketplace add General-Intelligence-Company/cofounder-plugin
codex plugin add cofounder@cofounder
codex plugin list
```

Confirm Cofounder appears in the installed list. Start a new Codex chat and
complete the Cofounder connection prompts. `/plugins` opens the plugin browser
in an interactive Codex CLI session.

[Codex plugin commands](https://learn.chatgpt.com/docs/developer-commands#codex-plugin)
and [marketplace sources](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli).

### Claude Code CLI

```sh
claude plugin marketplace add General-Intelligence-Company/cofounder-plugin
claude plugin install cofounder@cofounder --scope user
claude plugin list
```

Confirm Cofounder appears in the installed list. Start Claude Code, run `/mcp`,
select Cofounder's server, and complete its browser sign-in flow. User scope
makes the plugin available across projects on this machine. This installation
doesn't add the plugin to your Claude app account.

In an interactive Claude Code session, the equivalent installation flow is:

```text
/plugin marketplace add General-Intelligence-Company/cofounder-plugin
/plugin install cofounder@cofounder
```

Choose **Install for you** in the plugin details. Follow the install summary if
it asks you to reload plugins.

[Claude Code plugin commands](https://code.claude.com/docs/en/plugins/install)
and [MCP authentication](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers).

### Connection and activation

Installing the bundle and authorizing access to a company are separate steps.
If sign-in or consent is required, hand the connection flow to the account
owner. Start a fresh chat or session after installation so the host loads the
new skills and tools.

### Update from the command line

For Codex, refresh the marketplace and install its current plugin version:

```sh
codex plugin marketplace upgrade cofounder
codex plugin add cofounder@cofounder
```

For Claude Code, refresh the listing and update the installed plugin:

```sh
claude plugin marketplace update cofounder
claude plugin update cofounder@cofounder
```

Start a new session afterward. In Claude Code, `/reload-plugins` can apply the
update to an open session. Auto-update is off by default for third-party
marketplaces; enable it through **/plugin > Marketplaces > cofounder > Enable
auto-update** if desired.
