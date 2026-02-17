import time
from playwright.sync_api import Page

def safe_goto(page: Page, url: str, attempts: int = 3) -> None:
    last_err = None

    for i in range(attempts):
        try:
            # "commit" is earlier than domcontentloaded and more robust on protected sites
            page.goto(url, wait_until="commit", timeout=45000)

            # Then wait for DOM to be ready
            page.wait_for_load_state("domcontentloaded", timeout=45000)
            return
        except Exception as e:
            last_err = e
            time.sleep(1.5 * (i + 1))

    raise last_err
