from models import payment_stub_details
from page_objects.search_payment_stub_page import SearchPaymentStubPage


class PaymentStubPage(SearchPaymentStubPage):
    def __init__(self, page):
        super().__init__(page, payment_stub_details)
        self.frame = page.frame_locator("iframe[src*='SearchPay']")

