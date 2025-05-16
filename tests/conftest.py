import json
import os
from unittest.mock import patch

import pytest
from playwright.sync_api import sync_playwright

from data_base.sms_registration import SmsRegistration


def load_config():
    # מקבל את הנתיב המוחלט לתיקייה שבה נמצא conftest.py
    base_path = os.path.dirname(os.path.abspath(__file__))
    # בונה נתיב ל-Appconfig.json בתיקיית האב של tests (השורש של הפרויקט)
    config_path = os.path.join(base_path, "..", "Appconfig.json")

    # להדפיס את הנתיב שמנסים לטעון, לצורך דיבאג
    print(f"Loading config from: {os.path.abspath(config_path)}")

    with open(config_path, "r", encoding="utf-8") as config_file:
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

@pytest.fixture(autouse=True)
def mock_db_on_ci():
    if os.getenv("CI"):
        with patch.object(SmsRegistration, 'get_last_sms_by_phone', return_value="123456"):
            yield
    else:
        yield