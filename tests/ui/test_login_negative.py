from pages.login_page import LoginPage

def test_login_invalid_username(page):
    login = LoginPage(page)
    login.open()
    login.login("wronguser", "SuperSecretPassword!")
    login.assert_failure()