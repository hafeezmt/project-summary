# smart-summarizer

A small Agent Skill that helps students and developers turn supplied conversations, study notes, coding sessions, and project notes into accurate, actionable Markdown summaries.

> See [`project-summary.md`](project-summary.md) for a summary of this project.

## What it produces

- A concise summary and key points
- Explicit decisions
- Action items
- Unresolved questions
- Next steps
- Technical context when relevant
- Limitations or uncertainty when the source is incomplete

The skill does not automatically access past conversations or hidden files. Provide the source text or make the relevant files available to the agent. It avoids inventing details, repeating credentials, and presenting unverified work as complete. For students, it supports understanding and revision rather than completing graded assessments.

## Folder structure

```text
smart-summarizer/
├── SKILL.md
├── README.md
├── LICENSE
└── scripts/
    └── check_summary.py
```

## Install in OpenCode

OpenCode's current documentation lists `~/.config/opencode/skills/` for global skills and `.opencode/skills/` for project-local skills.

### Global install (all projects)

From the directory where you extracted this folder, run:

```bash
mkdir -p ~/.config/opencode/skills
cp -r smart-summarizer ~/.config/opencode/skills/
```

If you are already inside the `smart-summarizer` folder, instead run:

```bash
mkdir -p ~/.config/opencode/skills/smart-summarizer/scripts
cp SKILL.md README.md LICENSE ~/.config/opencode/skills/smart-summarizer/
cp scripts/check_summary.py ~/.config/opencode/skills/smart-summarizer/scripts/
chmod +x ~/.config/opencode/skills/smart-summarizer/scripts/check_summary.py
```

### Project-local install

From the root of the project where you want the skill available:

```bash
mkdir -p .opencode/skills
cp -r /path/to/smart-summarizer .opencode/skills/
```

Replace `/path/to/smart-summarizer` with the actual extracted folder path. Restart OpenCode or start a new session, then ask it to use `smart-summarizer` to summarize the supplied text.

## Use the checker script

The script checks for expected Markdown headings and flags a few common secret patterns. It uses only the Python standard library.

```bash
python3 scripts/check_summary.py path/to/summary.md
```

Exit codes: `0` means the configured checks passed; `1` means a heading is missing or a possible secret pattern was detected; `2` means the input file could not be read or was invalid. A pass does not prove that a summary is accurate or that it contains no secrets; review it manually.

## Validate against Agent Skills

Install and run the reference validator as described by the Agent Skills specification:

```bash
python3 -m pip install skills-ref
skills-ref validate ./smart-summarizer
```

If your system protects its system Python, use a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install skills-ref
skills-ref validate ./smart-summarizer
```

Reference specification: https://agentskills.io/specification
