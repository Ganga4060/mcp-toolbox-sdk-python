# Workflow Testing Strategy

## Overview
This branch contains intentional failing tests to validate the `export_complete_logs.yml` workflow.

## Test Files Created

### 1. `test_workflow_validation.py`
- **Purpose**: Comprehensive failing tests with detailed error messages
- **Features**: 
  - Multiple test scenarios (assertion failures, missing dependencies, stack traces)
  - Rich error context to validate complete log content
  - Demonstrates different types of failures external contributors face

### 2. `simple_failing_test.py`  
- **Purpose**: Simple failing tests for basic workflow validation
- **Features**:
  - Basic assertion failures
  - Environment variable issues
  - Import failures
  - Easy to understand and modify

## How to Test the Workflow

### Step 1: Create PR with Failing Tests
```bash
# Current branch: new-branch-build-logs
# Files committed: test_workflow_validation.py, simple_failing_test.py
# Next: Push and create PR to trigger Cloud Build
```

### Step 2: Observe Cloud Build Failures
When you create a PR:
1. Cloud Build will run and detect the failing tests
2. Tests will fail (as intended)
3. Cloud Build check runs will show "FAILURE" status

### Step 3: Validate Workflow Activation  
After the workflow is merged and active:
1. Failing tests trigger `export_complete_logs.yml`
2. Workflow detects the failed Cloud Build check runs
3. Fetches complete logs using `gcloud builds log`
4. Creates GitHub releases with downloadable log files
5. Adds download links to the failed check runs

### Step 4: Verify External Contributor Experience
External contributors should see:
```
❌ core-python-sdk-pr-py311 (toolbox-testing-438616)
   Build failed - Click for details
   
   [Truncated logs...]
   
   Build Log: https://console.cloud.google.com/logs/viewer?... (❌ Access Denied)
   View more details on Google Cloud Build (❌ Access Denied)
   📥 Download complete logs: https://github.com/.../complete-logs.txt (✅ Accessible!)
```

## Expected Test Failures

These tests are **designed to fail** and will show these error types:

1. **Assertion Failures**: Basic test failures with detailed context
2. **Missing Dependencies**: Simulated package/environment issues  
3. **Import Errors**: Module import problems external contributors face
4. **Stack Trace Errors**: Complex multi-level error scenarios

## Cleanup After Testing

After validating the workflow works:
```bash
# Remove the failing test files
git rm test_workflow_validation.py simple_failing_test.py
git commit -m "Remove test validation files after successful workflow testing"
```

## Success Criteria

The workflow is working correctly when:
- ✅ Failed Cloud Build tests are detected
- ✅ Build IDs are extracted from Cloud Build URLs  
- ✅ Complete logs are fetched via gcloud
- ✅ GitHub releases are created with log files
- ✅ Download links appear in failed check runs
- ✅ External contributors can access complete logs without permissions

## Notes

- These tests will cause **intentional failures** in Cloud Build
- The failures are **expected and safe** - they're for testing purposes
- The complete logs will contain the full error messages and context
- External contributors will finally have access to debugging information they need