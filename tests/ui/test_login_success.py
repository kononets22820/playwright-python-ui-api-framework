import pytest
from pages.login_page import LoginPage
from data.login_data import VALID_USER

@pytest.mark.smoke
def test_login_success(page):
    login = LoginPage(page)
    login.open()
    login.login(VALID_USER["username"], VALID_USER["password"])
    login.assert_success()