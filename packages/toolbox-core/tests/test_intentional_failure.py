# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Intentional failing test to trigger the Cloud Build failure log workflow.
This test is meant to verify that the error handling and log export workflow functions correctly.
"""

import pytest


def test_intentional_failure_to_trigger_workflow():
    """
    This test intentionally fails to trigger the workflow dispatch and error log collection.
    Remove this test once workflow functionality has been verified.
    """
    assert False, "Intentional failure to test the Cloud Build failure log export workflow"

