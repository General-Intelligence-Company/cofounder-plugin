---
name: import-context
description: "Add a URL or local text to the company Library and verify it is searchable, when the founder shares a link, repo, document, or notes for Cofounder to remember. Drives the Cofounder MCP tools `library_search`, `library_text_write`, `library_urls_ingest`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# Import Company Context

Ingest company context from: the source the founder gave

1. If the source the founder gave is a URL (repo, doc, article), call `library_urls_ingest`
   with it.
2. If it is local text you already have in hand, call `library_text_write`
   with a `<department>/...` path instead of ingesting a URL for it.
3. Verify the import landed: call `library_search` with a query that
   should hit the new content and confirm it appears in the results.

Report what was written/ingested (path or URL, size) and the verification
query result — not the full document text.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
