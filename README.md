# Cofounder plugin marketplace

This repository is generated from the `production` plugin source in
[Superoptimizers](https://github.com/General-Intelligence-Company/superoptimizers).
Do not edit generated plugin files here; make changes in that source repository.

Use the commands below to add this marketplace. If the repository is private,
your GitHub account needs read access and Git must be authenticated. With the
GitHub CLI, run `gh auth login` and `gh auth setup-git` before installation.

## Install in Claude Code

```text
/plugin marketplace add General-Intelligence-Company/cofounder-plugin
/plugin install cofounder@cofounder
```

## Install in Codex

```sh
codex plugin marketplace add General-Intelligence-Company/cofounder-plugin
```

Then select **Cofounder** in the Plugins Directory. To refresh a
marketplace after a release, run `codex plugin marketplace upgrade cofounder`.

## Source and version

Plugin identity: `cofounder`. Versions and shared content are authored in
Superoptimizers. Publication provenance is recorded in `publication.json`.
