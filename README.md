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

Use it in **ChatGPT, Codex, or Claude**.
[Explore the tools](plugins/cofounder/README.md).

## Install

Follow the steps for your app, then sign in to Cofounder.

### ChatGPT and Codex

1. Open **Plugins** and search for **Cofounder**.
2. Choose **Install** or the plus button, then sign in when prompted.
3. Start a new chat to use the plugin.

**Not listed?** In Codex, add the marketplace below. In a ChatGPT workspace,
ask an admin to import it. This import requires the **ChatGPT desktop app**
to install and use the plugin.

**Using a personal ChatGPT account?** The workspace import steps below don't
apply. If Cofounder isn't in your Plugins directory,
[contact support](https://cofounder.co/support) for help.

<details>
<summary>Add the marketplace to ChatGPT</summary>

A workspace admin completes these steps:

1. Open **Admin > Plugins > Add > Import marketplace**.
2. Set **Source** to `https://github.com/General-Intelligence-Company/cofounder-plugin`.
3. Leave **Path** and **Branch, tag, or commit** empty, then select
   **Import marketplace** and connect GitHub when prompted.
4. Make Cofounder available to workspace members. They can then install it
   from **Plugins** in the ChatGPT desktop app and sign in.

[OpenAI's import guide](https://learn.chatgpt.com/docs/enterprise/plugin-management).

</details>

<details>
<summary>Add the marketplace to local Codex</summary>

1. Open **Plugins > Add > Add a marketplace**.
2. Set **Source** to `General-Intelligence-Company/cofounder-plugin`.
3. Leave **Git ref** and **Sparse paths** empty, then select **Add marketplace**.
4. Open **Cofounder**, choose **Install**, and sign in when prompted.
   Start a new **local** chat to use it.

You can also use the [CLI commands below](#install-from-the-command-line-for-agents).
These configure local Codex; they don't import the plugin into a ChatGPT workspace.

</details>

### Claude desktop app and Cowork

1. Open **Customize > Plugins**. For Cowork, open the **Cowork** tab first.
2. Choose **Add > Add marketplace > Add from a repository**.
3. Enter `https://github.com/General-Intelligence-Company/cofounder-plugin` and select **Sync**.
4. Open **Cofounder** and choose **Add** or **Install**.
5. Open its **Connectors** tab, connect Cofounder, and sign in.
   Start a new conversation or Cowork task.

[Claude's installation guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).
For Claude Code, use the [CLI commands below](#install-from-the-command-line-for-agents).
Installing through the CLI doesn't add the plugin to your Claude app account.

<details>
<summary>Optional: ask your agent to help with installation</summary>

```text
Help me install the Cofounder plugin in this app:
https://github.com/General-Intelligence-Company/cofounder-plugin
Then help me connect my Cofounder account.
```

Your agent may guide you through the steps rather than install it directly.

</details>

## Get started

Once connected, ask:

> Help me get started with Cofounder.

Your agent will help you choose or create a company and find the next step.
Then try: **“Show me our roadmap and help me with the next milestone.”**

## Need help?

[Contact support](https://cofounder.co/support), or check the fixes below.

<details>
<summary>Troubleshooting</summary>

- **Tools aren't available?** Finish signing in, then start a new chat. In
  Codex, open **Plugins > Cofounder > Authenticate**. In Claude Code, use `/mcp`;
  in the Claude app, open the plugin's **Connectors** tab.
- **ChatGPT says “Desktop only”?** Open the ChatGPT desktop app to install and
  use this imported plugin.
- **Codex asks for a cloud environment?** Start a local chat; cloud environments
  don't carry your local plugin sign-in.
- **Windows install error** (`SEC_E_NO_CREDENTIALS`, “access denied,” or missing
  home directory)? Use the Plugins UI or run the CLI commands in your own
  PowerShell window.

</details>

<details>
<summary>Keep the plugin updated</summary>

- **ChatGPT workspace:** an admin opens **Admin > Plugins > Marketplaces**,
  selects Cofounder, and chooses **Sync now**.
- **Codex:** choose **Upgrade marketplace** for Cofounder in plugin settings.
- **Claude app and Cowork:** choose **Check for updates** on the marketplace.

Start a new chat or task after updating.

</details>

<details>
<summary>Command-line installation</summary>

## Install from the command line (for agents)

Run these in your terminal. On Windows, use your own PowerShell window if an
agent's sandbox blocks installation. Update the client if a command is missing.

**Codex**

```sh
codex plugin marketplace add General-Intelligence-Company/cofounder-plugin
codex plugin add cofounder@cofounder
codex plugin list
```

If sign-in didn't finish, run `codex mcp list`, then `codex mcp login` with the
Cofounder server name it shows. Start a new chat afterward.

**Claude Code**

```sh
claude plugin marketplace add General-Intelligence-Company/cofounder-plugin
claude plugin install cofounder@cofounder --scope user
claude plugin list
```

Run `/mcp` in Claude Code to sign in, then start a new session.

[Codex commands](https://learn.chatgpt.com/docs/developer-commands#codex-plugin) ·
[Claude Code commands](https://code.claude.com/docs/en/plugins/install).

</details>

<details>
<summary>Source and releases</summary>

Plugin files come from the production source in
[Superoptimizers](https://github.com/General-Intelligence-Company/superoptimizers).
Both marketplace names and the plugin name are `cofounder`.
Release provenance is recorded in [`publication.json`](publication.json).

Publication also regenerates this README from
[`scripts/export_cofounder_plugin_repository.py`](https://github.com/General-Intelligence-Company/superoptimizers/blob/main/scripts/export_cofounder_plugin_repository.py).
Make lasting README changes in that source template.

</details>

[Documentation](https://docs.cofounder.co/) ·
[Privacy](https://cofounder.co/privacy-policy) ·
[Terms](https://cofounder.co/terms).
This plugin is proprietary software; see [LICENSE](LICENSE).
