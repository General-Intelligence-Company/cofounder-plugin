---
name: generate-image
description: "Generate one image with Cofounder media tools and follow its job to the finished file, when the founder asks for an image, logo, or graphic. Drives the Cofounder MCP tools `media_generate`, `media_get`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# Generate an Image

Generate an image with `media_generate`.

Prompt: the prompt the founder gave

Call `media_generate` with kind="image", the prompt above, and size if
given (e.g. "1024x1024"). Supply an idempotency_key for this request; reuse
the same key only to retry identical arguments, which returns the same job.
Each job produces exactly one output. To make variants, submit separate jobs
with distinct keys. Pass from (a Library file id or an http(s) URL) to edit
an existing image, or use references for identity/style images. Follow the
response's next_steps for whether and when to call `media_get` with job_id.
Report the output's Library file id and URL — not the raw payload.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
