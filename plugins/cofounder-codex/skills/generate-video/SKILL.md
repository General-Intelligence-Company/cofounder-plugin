---
name: generate-video
description: "Generate one video with Cofounder media tools and follow its job to the finished file, when the founder asks for a video or clip. Drives the Cofounder MCP tools `media_generate`, `media_get`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# Generate a Video

Generate a video with `media_generate`.

Prompt: the prompt the founder gave

Call `media_generate` with kind="video" and the prompt above; set
duration_seconds and ratio (e.g. "16:9") if given. Supply an idempotency_key
for this request; reuse the same key only to retry identical arguments, which
returns the same job. Videos commonly return pending or running. Follow the
response's next_steps for whether and when to call `media_get` with job_id.
Pass from (a Library file id or an http(s) URL) as the image-to-video first
frame, or use references for reference-to-video; do not combine them. Report
the output's Library file id and URL once complete — not the raw payload.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
