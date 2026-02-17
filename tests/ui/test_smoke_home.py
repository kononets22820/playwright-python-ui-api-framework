import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
def test_home_smoke(page):
    home = HomePage(page)
    home.open()
    home.assert_loaded()
