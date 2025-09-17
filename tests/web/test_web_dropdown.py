import subprocess
import time
import requests
import pytest
from playwright.sync_api import sync_playwright


def wait_for_server(url="http://127.0.0.1:8000", timeout=30):
    """Poll until the server responds or timeout."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(url)
            if r.status_code < 500:  # 2xx or 3xx is fine
                return True
        except Exception:
            time.sleep(1)
    raise RuntimeError(f"Server {url} not ready after {timeout} seconds")


@pytest.fixture(scope="session", autouse=True)
def start_server():
    proc = subprocess.Popen(
        ["uvicorn", "web.app:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    wait_for_server("http://127.0.0.1:8000")
    yield
    proc.terminate()
    proc.wait()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # set headless=False for debugging
        yield browser
        browser.close()


def test_dropdown_updates(browser):
    page = browser.new_page()
    page.goto("http://127.0.0.1:8000/quiz")

    # check default selection
    assert page.locator("#selectcategory").input_value() == "random"
    assert page.locator("#selectcommand").input_value() == "random"

    # select a category (example: "encoding")
    page.select_option("#selectcategory", "encoding")

    # commands list should update
    options = page.locator("#selectcommand option").all_text_contents()
    assert len(options) > 1
    assert "Random Question" in options[0]

    # select a command
    first_cmd = page.locator("#selectcommand option").nth(1).get_attribute("value")
    page.select_option("#selectcommand", first_cmd)

    # args form should be populated
    assert page.locator("#argsForm div").count() > 0


def test_reset_button(browser):
    page = browser.new_page()
    page.goto("http://127.0.0.1:8000/quiz")

    # change category
    page.select_option("#selectcategory", "encoding")
    assert page.locator("#selectcategory").input_value() == "encoding"

    # click reset
    page.click("text=Reset")

    # verify restored defaults
    assert page.locator("#selectcategory").input_value() == "random"
    assert page.locator("#selectcommand").input_value() == "random"
    assert page.locator("#argsForm").inner_html().strip() == ""
