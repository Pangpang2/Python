import pytest


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="prod", help="Testing environment")
    parser.addoption("--test_run_id", action="store", help="Test Run ID in Testrail")
    parser.addoption("--test_case_id", action="store", help="Test Case ID in Testrail")


def pytest_runtest_setup(item):
    cmd_env = item.config.getoption('--env')
    env_names = item.get_closest_marker(name='env')
    if env_names:
        matches_env = False
        for env_name in env_names.args:
            if env_name in cmd_env:
                matches_env = True
                break
        if not matches_env:
            pytest.skip("Test requires environments in %r" % env_names)

