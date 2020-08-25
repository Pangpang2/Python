import pytest
import smtplib

smtpserver = "mail.python.org"  # will be read by smtp fixture

'--env prod1'


@pytest.fixture(scope="module")
def smtp_connection(request):
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    print request.config.getoption("env")
    print request.param
    yield server
    # if request.node.rep_setup.failed:
    #     print("setting up a test failed!", request.node.nodeid)
    # elif request.node.rep_setup.passed:
    #     print("setting up a test passed")
    #     if request.node.rep_call.failed:
    #         print("executing test failed", request.node.nodeid)



def test_showhelo(smtp_connection):
    print smtp_connection
    assert smtp_connection == smtpserver

@pytest.mark.parametrize(smtp_connection, ['full'])
def test_sayhi(smtp_connection):
    print smtp_connection
    assert smtp_connection == smtpserver