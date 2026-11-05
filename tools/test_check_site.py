"""Unit tests for check_site.py (run: python3 tools/test_check_site.py).

Covers the pure-logic pieces the CI run can't exercise: step counting,
footer extraction, GoatCounter/placeholder regexes, redaction patterns,
and the external-link classification (network mocked).
"""
import socket
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_site as cs


def html(body: str) -> ET.Element:
    return ET.fromstring(f"<html><body>{body}</body></html>")


class TestStepCounter(unittest.TestCase):
    def test_counts_top_level_only(self):
        root = html("<ol><li>a</li><li>b<ol><li>nested</li></ol></li></ol>"
                    "<ol><li>c</li></ol>")
        self.assertEqual(cs.walk_top_level_ol_li(root), 3)

    def test_ignores_ul(self):
        root = html("<ul><li>a</li></ul><ol><li>b</li></ol>")
        self.assertEqual(cs.walk_top_level_ol_li(root), 1)

    def test_empty(self):
        root = html("<p>no steps</p>")
        self.assertEqual(cs.walk_top_level_ol_li(root), 0)


class TestFooter(unittest.TestCase):
    def test_extracts_footer(self):
        raw = "<footer><p>x</p></footer>"
        self.assertEqual(cs.footer_of(raw), raw)

    def test_missing_footer_is_empty(self):
        self.assertEqual(cs.footer_of("<p>nope</p>"), "")


class TestGoatCounter(unittest.TestCase):
    def test_valid_tag_matches(self):
        raw = ('<script data-goatcounter="https://mysite.goatcounter.com/count" '
               'async src="//gc.zgo.at/count.js"></script>')
        self.assertTrue(cs.GC_RE.search(raw))
        self.assertFalse(cs.GC_PLACEHOLDER_RE.search(raw))

    def test_placeholder_detected(self):
        raw = '<script data-goatcounter="https://YOURCODE.goatcounter.com/count"></script>'
        self.assertTrue(cs.GC_PLACEHOLDER_RE.search(raw))

    def test_script_regex_counts(self):
        self.assertEqual(len(cs.SCRIPT_RE.findall("<script>a</script><script>b</script>")), 2)


class TestRedaction(unittest.TestCase):
    def test_vault_paths_fail(self):
        for bad in ["/home/kurt/secret", "~/Documents/notes",
                    "immutable-source-files", "Documents/equational-wiki"]:
            hits = [label for pat, label in cs.REDACTION_PATTERNS if pat.search(bad)]
            self.assertTrue(hits, f"{bad} should be flagged")

    def test_public_dotfiles_pass(self):
        for ok in ["~/.hermes/config.yaml", "source ~/.bashrc"]:
            hits = [label for pat, label in cs.REDACTION_PATTERNS if pat.search(ok)]
            self.assertFalse(hits, f"{ok} should NOT be flagged: {hits}")


class TestExternalClassification(unittest.TestCase):
    def test_404_is_hard_fail(self):
        import urllib.error
        err = urllib.error.HTTPError("u", 404, "nf", None, None)
        with patch.object(cs.urllib.request, "urlopen", side_effect=err):
            self.assertEqual(cs.check_external("https://x.test/a"), "FAIL")

    def test_429_is_warning(self):
        import urllib.error
        err = urllib.error.HTTPError("u", 429, "slow down", None, None)
        with patch.object(cs.urllib.request, "urlopen", side_effect=err):
            self.assertEqual(cs.check_external("https://x.test/a"), "WARN")

    def test_ok(self):
        import io
        class R:
            status = 200
            def __enter__(self): return self
            def __exit__(self, *a): return False
        with patch.object(cs.urllib.request, "urlopen", return_value=R()):
            self.assertEqual(cs.check_external("https://x.test/a"), "OK")

    def test_dns_gaierror_fails_after_retry(self):
        import urllib.error
        err = urllib.error.URLError(socket.gaierror(8, "nx"))
        with patch.object(cs.urllib.request, "urlopen", side_effect=err):
            self.assertEqual(cs.check_external("https://x.test/a"), "FAIL")

    def test_timeout_is_warning(self):
        with patch.object(cs.urllib.request, "urlopen", side_effect=TimeoutError()):
            self.assertEqual(cs.check_external("https://x.test/a"), "WARN")


if __name__ == "__main__":
    unittest.main(verbosity=2)
