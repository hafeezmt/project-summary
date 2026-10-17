#!/usr/bin/env python3
"""Check a saved Smart Summarizer Markdown report for expected sections and likely secrets."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = (
    "Summary",
    "Key Points",
    "Decisions Made",
    "Action Items",
    "Unresolved Questions",
    "Next Steps",
)
SECRET_PATTERNS = (
    ("possible API key/token", re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|secret[_-]?key)\s*[:=]\s*['\"]?[^\s'\"]{8,}")),
    ("possible private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("possible credential-bearing URL", re.compile(r"(?i)https?://[^\s/:@]+:[^\s/@]+@")),
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check a Smart Summarizer Markdown report's headings and flag likely secrets without printing their values."
    )
    parser.add_argument("markdown_file", help="Path to the Markdown report to check")
    args = parser.parse_args()
    path = Path(args.markdown_file)
    if not path.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        return 2
    if not path.is_file():
        print(f"Error: not a regular file: {path}", file=sys.stderr)
        return 2
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print("Error: file is not valid UTF-8 text.", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"Error: could not read file: {exc}", file=sys.stderr)
        return 2

    headings = {match.strip().lower() for match in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", content)}
    missing = [heading for heading in REQUIRED_HEADINGS if heading.lower() not in headings]
    if missing:
        print("Missing required headings: " + ", ".join(missing))
    else:
        print("Required summary headings: OK")

    warnings = []
    for label, pattern in SECRET_PATTERNS:
        if pattern.search(content):
            warnings.append(label)
    if warnings:
        for warning in warnings:
            print(f"WARNING: {warning} detected. Review the report and remove or redact sensitive values.")
    else:
        print("Likely-secret scan: no configured patterns detected (this is not a guarantee).")

    if missing:
        return 1
    if warnings:
        return 1
    print("Check passed. Human review is still required for factual accuracy and privacy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
