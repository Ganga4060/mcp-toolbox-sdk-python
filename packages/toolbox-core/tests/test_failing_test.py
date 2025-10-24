import sys
import pytest

def test_failing_with_logs():
    """
    This test intentionally fails and prints logs to stdout and stderr.
    """
    print("[LOG] This is a test log message to stdout.")
    print("[ERROR] This is a test error message to stderr.", file=sys.stderr)
    pytest.fail("Intentional failure for workflow and log extraction testing.")
