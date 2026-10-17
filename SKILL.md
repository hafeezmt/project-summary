---
name: smart-summarizer
description: Summarizes long conversations, study materials, coding sessions, and project notes into accurate Markdown reports with key points, decisions, action items, unresolved questions, and next steps. Use when a user says "summarize this conversation", "summarize my coding session", or "what did we decide?". It is not for inventing missing facts, exposing secrets, or claiming unverified work is complete.
license: MIT
---

# Smart Summarizer

## When to use this skill

Use this skill when a student or developer asks to summarize supplied conversation text, study notes, coding-session logs, project documentation, or meeting notes. It supports both learning and software-project workflows.

Trigger examples:
- "Summarize this conversation."
- "Summarize my coding session."
- "What did we decide?"

Do not assume access to previous chats, hidden files, terminals, repositories, or logs. Work only with material available in the current context or files the user explicitly makes available.

## Gather first

1. Identify the source material and intended audience if not obvious.
2. Ask for the transcript, notes, log, or relevant files if the source is not available.
3. Ask whether the user prefers a brief or detailed summary only when the distinction materially affects the result; otherwise use a concise report.
4. For student materials, preserve learning concepts and terminology. Do not complete graded work on the user's behalf; summarize the material and explain concepts instead.

## Process

1. Read the supplied material and determine its topic, purpose, and time range if stated.
2. Extract the central message, key facts, explicit decisions, tasks, open questions, and next steps.
3. For coding sessions, preserve relevant filenames, commands, errors, technologies, and confirmed changes.
4. Separate explicit facts from interpretation. Label uncertainty and conflicting details rather than resolving them by guessing.
5. Do not say a task was completed unless the source provides evidence. Distinguish proposed, in-progress, and completed work when useful.
6. Check for credentials or sensitive values. Do not repeat secrets in the report; replace them with `[REDACTED]` and advise the user to rotate exposed credentials when appropriate.
7. Write the report using the output format below. Omit a section only if it genuinely has no applicable content; write `None stated` when that absence matters.
8. If helpful, use `scripts/check_summary.py` to check that a saved Markdown report has the expected headings and to detect likely secret patterns. The script is a lightweight check, not proof that the report is accurate or safe.
9. Re-read the result against the source to catch unsupported claims, missing decisions, and accidental repetition.

## Output format

# Summary
A short overview of the material and its purpose.

## Key Points
- The main facts, concepts, and context.

## Decisions Made
- Decisions explicitly supported by the source.

## Action Items
- [ ] Task — include an owner or deadline only when stated.

## Unresolved Questions
- Questions or uncertainties that remain open.

## Next Steps
1. The most useful immediate action supported by the source.

## Technical Context
Include this section when relevant to coding or project work. Record confirmed technologies, filenames, commands, errors, and verified changes.

## Limitations
Mention missing source material, conflicts, or uncertainty that affects the summary.

## Rules

- Never invent facts, quotes, decisions, owners, deadlines, metrics, or completed work.
- Never imply that the skill has read a prior conversation or local file unless that content was actually provided or accessed.
- Never include passwords, API keys, access tokens, private keys, or other credentials in the output.
- Keep quotations short and preserve the source's meaning.
- Do not turn assumptions or suggestions into confirmed decisions.
- For student use, support understanding and revision rather than producing answers for graded assessments.
- Prefer concise, clear language and Markdown that is easy to save in a project repository.
