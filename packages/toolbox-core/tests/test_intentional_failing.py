import pytest

def test_intentional_fail():

    """This test is intentionally failing to validate CI failure detection."""
    
    assert False, "Intentional failure for CI workflow validation."
