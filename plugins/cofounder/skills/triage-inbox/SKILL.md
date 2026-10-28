---
name: triage-inbox
description: "Review recent mail and support tickets and draft replies for approval, when the founder asks about their inbox, email, or customer messages. Drives the Cofounder MCP tools `company_memberships_list`, `customer_support_tickets_list`, `customer_support_tickets_reply`, `email_drafts_create`, `email_drafts_send`, `email_threads_get`, `email_threads_list`, `email_threads_reply`, `resources_list`."
---

<!-- Generated from PROMPT_MENU by backend/scripts/sync_plugin_prompt_skills.py; edit mcp_prompts.py instead. -->

# Triage My Inbox

Triage the founder's inbox and draft replies.

With a company API key the company is fixed: omit company_id. Otherwise, if the founder has several companies, call `company_memberships_list`, match the company they named, and pass its org_id as company_id on every call. Ask by company name, never by ID, when the match is unclear.

1. Call `resources_list`, pick the resource whose primitive is email, and pass its resource_id as resource to `email_threads_list` for recent threads and `email_threads_get` for the ones that need an answer. Pass the same resource to the email tools below.
2. Call `customer_support_tickets_list` for open tickets. Show proposed replies and call `customer_support_tickets_reply` only after the founder approves them.
3. For each thread worth answering, check the email resource's handle. If it ends in @cofounder.company it is a shared trial inbox that cannot save drafts: show the proposed reply in chat and call `email_threads_reply` only after approval. Otherwise call `email_drafts_create` with a draft reply and save drafts only.

Sending is the founder's decision: show each reply and call `email_drafts_send`
or `email_threads_reply` only after they approve it. Report threads
by sender and subject, grouped as needs reply, FYI, and ignore.

The server hides tools a company has no access to. If a tool named above is unavailable, skip its step and say so.
