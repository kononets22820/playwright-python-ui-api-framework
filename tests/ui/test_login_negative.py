import pytest
from pages.login_page import LoginPage
from data.login_data import INVALID_USER

@pytest.mark.regression
def test_login_invalid_username(page):
    login = LoginPage(page)
    login.open()
    login.login(INVALID_USER["username"], INVALID_USER["password"])
    login.assert_failure()