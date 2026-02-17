from playwright.sync_api import Page, expect
from utils.config import BASE_URL
from utils.navigation import safe_goto


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        safe_goto(self.page, BASE_URL, attempts=2)

    def assert_loaded(self):
        h1 = self.page.locator("h1.heading")
        expect(h1).to_be_visible()
        expect(h1).to_contain_text("Welcome to the-internet")
