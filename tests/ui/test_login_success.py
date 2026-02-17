import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_success(page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    login.assert_success()