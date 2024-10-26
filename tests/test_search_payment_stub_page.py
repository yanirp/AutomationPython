import pytest
from playwright.sync_api import Page
from models import payment_stub_details
from models.payment_stub_details import get_payment_stub_details
from page_objects.search_payment_stub_page import SearchPaymentStubPage


@pytest.mark.parametrize("payment_stub_details" , get_payment_stub_details())
def test_search_payment_stub(page: Page,payment_stub_details):
    search_payment_stub_page = SearchPaymentStubPage(page,payment_stub_details)

    payment_page_url = f"https://stage.mast.co.il/{payment_stub_details['companyId']}/payment"
    page.goto(payment_page_url)

    search_payment_stub_page.search_payment_stub(payment_stub_details['PayerNumber'], payment_stub_details['StubNumber'])
