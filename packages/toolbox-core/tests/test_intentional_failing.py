def intentional_fail_test():
    """This test is intentionally failing to validate that :
    1. Cloud Build checks fail as expected or not.
    2. The export_build_logs workflow detects the failure 
    3. Failed check information is correctly extracted or not2 

    """
    assert False, "Intentional failure to test Exporting Cloud Build Failure Logs"
