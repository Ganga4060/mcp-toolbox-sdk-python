"""
Simple failing test for workflow validation.
Place this in any existing test directory to trigger failures.
"""

def test_workflow_log_export_validation():
    """
    Simple test that fails to validate log export workflow.
    
    This test will fail in Cloud Build and should trigger our
    export_complete_logs.yml workflow to create downloadable
    complete logs for external contributors.
    """
    # Intentional failure with descriptive message
    failure_reason = (
        "This test intentionally fails to validate the export complete logs workflow. "
        "External contributors should see a download link for complete logs when this fails."
    )
    
    assert 1 == 2, failure_reason


def test_missing_environment_variable():
    """Test that fails due to missing environment variable."""
    import os
    
    required_var = "NONEXISTENT_TEST_VARIABLE"
    actual_value = os.getenv(required_var)
    
    assert actual_value is not None, (
        f"Missing required environment variable: {required_var}. "
        "This type of error often needs complete build logs to debug "
        "environment setup issues that external contributors face."
    )


def test_import_failure_simulation():
    """Test that fails due to import issues."""
    try:
        # Try to import a module that doesn't exist
        import nonexistent_module_for_testing  # This will fail
        assert True
    except ImportError as e:
        # Convert ImportError to assertion failure for test framework
        assert False, (
            f"Import failed: {e}. "
            "Import errors often require complete logs to see the full "
            "dependency chain and help external contributors understand "
            "what packages need to be installed."
        )