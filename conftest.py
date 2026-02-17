import os
import re
from datetime import datetime
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright
from utils.config import API_BASE_URL

ARTIFACTS_DIR = Path("artifacts")


def _safe_name(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", text)[:120]


@pytest.fixture(scope="session")
def browser():
    headless = os.getenv("HEADLESS", "true").lower() == "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            slow_mo=50,  # nice for demo
            args=[
                "--disable-http2",
                "--disable-blink-features=AutomationControlled",
            ],
        )
        yield browser
        browser.close()


@pytest.fixture()
def context(browser):
    ctx = browser.new_context(
        locale="en-US",
        viewport={"width": 1440, "height": 900},
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/121.0.0.0 Safari/537.36"
        ),
    )
    yield ctx
    ctx.close()


@pytest.fixture()
def page(context):
    p = context.new_page()
    yield p
    p.close()


# Start tracing for every test
@pytest.fixture(autouse=True)
def _trace(context):
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    # If test passed, stop without saving. If it failed, we save in the hook below.
    try:
        context.tracing.stop()
    except Exception:
        # already stopped/saved in hook
        pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        ARTIFACTS_DIR.mkdir(exist_ok=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = _safe_name(item.nodeid)

        page = item.funcargs.get("page")
        context = item.funcargs.get("context")

        if page:
            page.screenshot(
                path=str(ARTIFACTS_DIR / f"{ts}_{name}.png"),
                full_page=True,
            )

        if context:
            try:
                context.tracing.stop(
                    path=str(ARTIFACTS_DIR / f"{ts}_{name}_trace.zip")
                )
            except Exception:
                pass

@pytest.fixture()
def api_request(context):
    # Uses Playwright's APIRequestContext via the browser context
    request = context.request
    yield request

