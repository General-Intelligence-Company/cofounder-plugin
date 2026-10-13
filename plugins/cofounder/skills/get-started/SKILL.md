---
name: get-started
description: Load Cofounder's current hosted setup guide when the user chooses Set up for Cofounder or asks to get started or onboard. Not for unrelated work or ongoing company tasks.
---

# Get started with Cofounder

1. Call `onboarding_get` with `{}`.
2. Fetch the returned `mcp_skill_url` and follow its current instructions.
3. If `onboarding_get` is unavailable, Cofounder is not signed in yet. Fetch https://app.cofounder.co/mcp-onboarding/skill.md and follow it.
