import time
import allure
from playwright.async_api import Page
from models.user_details import user
from page_objects.authority_page import AuthorityPage


@allure.description("getting to authority page and do refresh for the page")
@allure.title("Test authority page functionality")
def test_authority_page_functions(page: Page):
    authority_page = AuthorityPage(page)
    authority_page.user_login_to_mast_with_asset(user.phone)
    time.sleep(5)
