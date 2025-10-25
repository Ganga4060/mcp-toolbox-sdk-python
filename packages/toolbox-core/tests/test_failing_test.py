import sys
import pytest


def test_failing_with_logs():
    """
    This test intentionally fails and prints logs to stdout and stderr.
    """
    print("[LOG] This is a test log message to stdout.")
    print("[LOG] Another info log for debugging.")
    print("[LOG] Simulating step 1 completed.")
    print("[ERROR] This is a test error message to stderr.", file=sys.stderr)
    print("[ERROR] Simulated error before failure.", file=sys.stderr)
    print("[WARN] This is a warning log.")
    print("[DEBUG] Debugging details here.")
    pytest.fail("Intentional failure for workflow and log extraction testing.")
