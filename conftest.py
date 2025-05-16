import json
import pytest
from playwright.sync_api import sync_playwright


def load_config():
    with open("C:/Repos/AutomationPython/Appconfig.json") as config_file:
        return json.load(config_file)

@pytest.fixture(scope="session")
def page():
    config = load_config()
    base_url = config['base_url']
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto(base_url)
        yield page
        context.close()
        browser.close()


