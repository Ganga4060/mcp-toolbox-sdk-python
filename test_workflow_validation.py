"""
Test case designed to fail for testing the export complete logs workflow.

This test will intentionally fail to trigger our log export mechanism
and validate that external contributors can access complete error logs.
"""

import pytest


class TestWorkflowValidation:
    """Test cases for validating the export complete logs workflow."""
    
    def test_intentional_failure_for_workflow_testing(self):
        """
        This test is designed to fail intentionally to test our log export workflow.
        
        When this test fails in a PR, it should trigger the export_complete_logs.yml 
        workflow which will:
        1. Detect the Cloud Build PR test failure
        2. Extract the build ID from the Cloud Build URL
        3. Fetch complete logs using gcloud
        4. Create a public GitHub release with the complete logs
        5. Add a download link to the failed check run
        
        This allows external contributors to access complete error details
        that are normally truncated in GitHub's UI.
        """
        # Intentionally failing assertion with detailed error context
        error_message = (
            "This is an intentional test failure to validate the export complete logs workflow. "
            "This test should trigger our log export mechanism and provide external contributors "
            "with access to complete, untruncated build logs via a downloadable link. "
            "The complete logs should contain this full error message along with all build context."
        )
        
        # Create some complex error context that would be helpful in complete logs
        test_data = {
            "workflow": "export_complete_logs",
            "purpose": "testing log export for external contributors", 
            "expected_behavior": [
                "detect failed Cloud Build PR test",
                "extract build ID from details_url",
                "fetch complete logs via gcloud",
                "create public GitHub release",
                "add download link to check run"
            ],
            "test_environment": {
                "repository": "mcp-toolbox-sdk-python",
                "branch": "new-branch-build-logs", 
                "test_type": "integration_test_failure"
            }
        }
        
        # This assertion will fail and trigger the workflow
        assert False, f"INTENTIONAL FAILURE: {error_message}\n\nTest Context: {test_data}"
    
    def test_another_failing_scenario(self):
        """
        Another intentional failure to test multiple failed tests scenario.
        
        This tests whether our workflow handles multiple test failures correctly
        and provides separate download links for each failed test.
        """
        # Simulate a different type of failure
        missing_dependency = "required_package_for_external_contributors"
        available_packages = ["package1", "package2", "package3"]
        
        # This will create a different error signature in the logs
        assert missing_dependency in available_packages, (
            f"Missing required dependency '{missing_dependency}' for external contributors. "
            f"Available packages: {available_packages}. "
            "This error demonstrates how complete logs help debug dependency issues "
            "that external contributors face when trying to reproduce build failures locally."
        )
    
    def test_complex_error_with_stack_trace(self):
        """
        Test that generates a complex error with stack trace.
        
        This helps validate that our complete log export captures
        full stack traces that are often truncated in GitHub's UI.
        """
        def nested_function_level_3():
            """Innermost function that raises the error."""
            raise ValueError(
                "This is a deep stack trace error that demonstrates how "
                "complete logs preserve full error context including "
                "file paths, line numbers, and variable states that "
                "external contributors need for effective debugging."
            )
        
        def nested_function_level_2():
            """Middle function in the call stack."""
            context_data = {
                "user_type": "external_contributor",
                "access_level": "limited", 
                "needs_complete_logs": True
            }
            print(f"Debug context: {context_data}")
            nested_function_level_3()
        
        def nested_function_level_1():
            """Outer function in the call stack."""
            print("Starting complex operation that will fail...")
            nested_function_level_2()
        
        # This will generate a multi-level stack trace
        with pytest.raises(ValueError):
            nested_function_level_1()
        
        # Force failure to ensure this test shows up in failed tests
        assert False, "Forced failure to ensure this test appears in failed check runs"


if __name__ == "__main__":
    # Allow running this test file directly
    pytest.main([__file__, "-v"])