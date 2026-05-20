"""Deterministic report generation for the Smash112 log QA agent."""

from __future__ import annotations

from datetime import datetime
from typing import Protocol


class ReportFinding(Protocol):
    rule_id: str
    title: str
    severity: str
    evidence: list[str]
    possible_modules: list[str]
    suggested_reproduction: str


def generate_markdown_report(
    findings: list[ReportFinding],
    source_name: str = "game log",
) -> str:
    """Convert rule findings into a developer-readable Markdown report.

    This is the deterministic version of the "LLM summarizer" stage. It keeps
    the same structured input/output shape that a future ChatGPT or Doubao API
    call could replace.
    """

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Smash112 Gameplay QA Report",
        "",
        f"Source: `{source_name}`",
        f"Generated: {generated_at}",
        "",
        "## Summary",
        "",
    ]

    if not findings:
        lines.extend(
            [
                "No critical issues found in this gameplay log.",
                "",
                "The analyzer did not detect stuck movement, negative health, "
                "repeated collision errors, AI idle loops, or hit-without-damage "
                "patterns.",
            ]
        )
        return "\n".join(lines) + "\n"

    high_count = sum(1 for finding in findings if finding.severity == "high")
    medium_count = sum(1 for finding in findings if finding.severity == "medium")
    lines.extend(
        [
            (
                f"Detected {len(findings)} potential issue(s): "
                f"{high_count} high severity, {medium_count} medium severity."
            ),
            "",
            _summarize_findings(findings),
            "",
            "## Findings",
            "",
        ]
    )

    for index, finding in enumerate(findings, start=1):
        lines.extend(
            [
                f"### {index}. {finding.title}",
                "",
                f"Severity: `{finding.severity}`",
                f"Rule: `{finding.rule_id}`",
                "",
                "Evidence:",
            ]
        )
        lines.extend(f"- {item}" for item in finding.evidence)
        lines.extend(
            [
                "",
                "Possible Module:",
            ]
        )
        lines.extend(f"- {module}" for module in finding.possible_modules)
        lines.extend(
            [
                "",
                "Suggested Reproduction:",
                f"- {finding.suggested_reproduction}",
                "",
            ]
        )

    lines.extend(
        [
            "## Agent Pipeline",
            "",
            "1. Rule-based detector scanned structured gameplay events.",
            "2. Report generator converted suspicious patterns into a bug report.",
            "3. Future extension: send the same structured findings to an LLM API "
            "for richer natural-language summaries.",
            "",
        ]
    )

    return "\n".join(lines)


def build_llm_prompt(findings: list[ReportFinding]) -> str:
    """Build the prompt that a future LLM summarizer could receive."""

    if not findings:
        return (
            "Summarize this Smash112 gameplay QA run: no rule-based issues were "
            "detected. Mention that the log should still be reviewed manually if "
            "the player observed visible bugs."
        )

    sections = [
        "You are helping summarize gameplay QA findings for Smash112, a "
        "platform fighting game prototype. Write a concise developer bug report "
        "with potential bug, evidence, likely module, and reproduction steps.",
        "",
        "Rule findings:",
    ]

    for finding in findings:
        sections.append(
            (
                f"- {finding.rule_id}: {finding.title}; severity={finding.severity}; "
                f"evidence={finding.evidence}; modules={finding.possible_modules}; "
                f"repro={finding.suggested_reproduction}"
            )
        )

    return "\n".join(sections)


def _summarize_findings(findings: list[ReportFinding]) -> str:
    titles = [finding.title for finding in findings]
    if len(titles) == 1:
        return f"Primary issue: {titles[0]}."
    return "Primary issues: " + "; ".join(titles) + "."
