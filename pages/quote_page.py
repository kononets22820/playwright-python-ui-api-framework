from playwright.sync_api import Page, expect
from utils.config import BASE_URL
from utils.navigation import safe_goto

class QuotePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, symbol: str):
        url = f"{BASE_URL}/market-activity/stocks/{symbol.lower()}"
        safe_goto(self.page, url, attempts=3)

    def assert_ticker_visible(self, ticker: str):
        expect(self.page.get_by_text(ticker, exact=True).first).to_be_visible(timeout=20000)

    def go_to_news(self):
        self.page.get_by_role("link", name="News").click()
        # URL patterns can vary; keep it flexible
        expect(self.page).to_have_url(lambda url: "news" in url.lower())