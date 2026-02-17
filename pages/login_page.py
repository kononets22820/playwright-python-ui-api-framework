from playwright.sync_api import Page, expect
from utils.config import BASE_URL
from utils.navigation import safe_goto

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_btn = page.get_by_role("button", name="Login")
        self.flash = page.locator("#flash")

    def open(self):
        safe_goto(self.page, f"{BASE_URL}/login", attempts=2)

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()

    def assert_success(self):
        expect(self.flash).to_contain_text("You logged into a secure area!")

    def assert_failure(self):
        expect(self.flash).to_contain_text("Your username is invalid!")