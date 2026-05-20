from pathlib import Path
import unittest

from tools.game_log_agent.analyzer import analyze_log, load_log
from tools.game_log_agent.report_generator import generate_markdown_report


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_LOGS = PROJECT_ROOT / "tools" / "game_log_agent" / "sample_logs"


class GameLogAgentTests(unittest.TestCase):
    def test_stuck_sample_detects_stuck_player(self):
        events = load_log(SAMPLE_LOGS / "stuck_bug.json")
        findings = analyze_log(events)

        self.assertIn("stuck_player", {finding.rule_id for finding in findings})

    def test_clean_sample_has_no_findings(self):
        events = load_log(SAMPLE_LOGS / "clean_run.json")
        findings = analyze_log(events)

        self.assertEqual(findings, [])

    def test_report_contains_developer_sections(self):
        events = load_log(SAMPLE_LOGS / "combat_no_damage_bug.json")
        findings = analyze_log(events)
        report = generate_markdown_report(findings, source_name="combat sample")

        self.assertIn("Evidence:", report)
        self.assertIn("Possible Module:", report)
        self.assertIn("Suggested Reproduction:", report)


if __name__ == "__main__":
    unittest.main()
