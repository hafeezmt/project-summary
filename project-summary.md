# Summary

Project notes for **smart-summarizer**, an Agent Skill (MIT-licensed) that turns supplied conversations, study notes, coding sessions, and project notes into accurate, actionable Markdown reports. The notes describe the skill's purpose, behavior rules, output format, installation options, and a helper validation script. Source material: `SKILL.md`, `README.md`, `LICENSE`, and `scripts/check_summary.py` in `~/Downloads/smart-summarizer`.

## Key Points

- The skill produces a fixed report structure: Summary, Key Points, Decisions Made, Action Items, Unresolved Questions, Next Steps, plus optional Technical Context and Limitations sections.
- It works only with material supplied in the current context or files the user explicitly makes available; it does not access past chats, hidden files, terminals, or logs.
- Hard rules: never invent facts, decisions, owners, deadlines, or completed work; never output credentials (replace with `[REDACTED]`); never imply unverified work is complete.
- For student use, it summarizes and explains concepts rather than completing graded assessments.
- `scripts/check_summary.py` verifies required headings and flags likely secret patterns (API keys/tokens, private keys, credential-bearing URLs) using only the Python standard library.
- Install options documented: global (`~/.config/opencode/skills/`) or project-local (`.opencode/skills/`), then restart OpenCode.
- README points to the Agent Skills reference validator (`skills-ref validate ./smart-summarizer`) and the spec at https://agentskills.io/specification.

## Decisions Made

- None stated.

## Action Items

- [ ] Install the skill per README instructions (global or project-local copy) — no owner or deadline stated.

## Unresolved Questions

- None stated. (The notes do not record whether `skills-ref validate` has been run or passes.)

## Next Steps

1. Install the skill into `~/.config/opencode/skills/` using the README's in-folder copy commands, then start a new OpenCode session and test it with a sample summary request.

## Technical Context

- License: MIT, Copyright (c) 2026 Jungudo Muhammad Tukur.
- Files: `SKILL.md` (skill definition with YAML frontmatter: `name`, `description`, `license`), `README.md` (usage/install docs), `LICENSE`, `scripts/check_summary.py`.
- `check_summary.py` usage: `python3 scripts/check_summary.py path/to/summary.md`.
- Exit codes: `0` checks passed; `1` missing heading or possible secret detected; `2` file unreadable/invalid.
- Required headings checked (case-insensitive): Summary, Key Points, Decisions Made, Action Items, Unresolved Questions, Next Steps.
- Secret patterns detected: `api_key`/`access_token`/`secret_key` assignments, `-----BEGIN ... PRIVATE KEY-----`, URLs with embedded `user:password@` credentials; matches are reported by label only, values are not printed.
- The `references/` directory in the project folder is empty.

## Limitations

- Summary is based solely on the four supplied project files; no conversation history or repository metadata (e.g., git history) was available.
- The notes contain no explicit decisions, owners, deadlines, errors, or test results, so those sections are largely "None stated".
- Whether the project passes `skills-ref validate` or the checker script is untested in this session; the source does not record it.
