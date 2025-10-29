import pytest

def test_intentional_failure():
    assert False, "This test is designed to fail for CI edge case testing."
