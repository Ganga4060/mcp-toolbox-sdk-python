import sys
import pytest


def test_failing_with_logs():
    """
    This test intentionally fails and prints logs to stdout and stderr and test is for step3 and step4 of the workflow now updated .
    """
    print("[LOG] This is a test log message to stdout.")
    print("[ERROR] Simulated error before failure.", file=sys.stderr)
    print("[WARN] This is a warning log.")
    print("[DEBUG] Debugging details here.")
    pytest.fail("Intentional failure for workflow and log extraction testing.")
