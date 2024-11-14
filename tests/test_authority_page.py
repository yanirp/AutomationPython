import time

import pytest
from playwright.async_api import Page

from page_objects.authority_page import AuthorityPage

@pytest.mark.description("Test authority page functionality")
def test_authority_page_functions(page: Page):
    authority_page = AuthorityPage(page)
    page.reload()
