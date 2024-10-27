

from page_objects.base_page import BasePage
from page_objects.search_payment_stub_page import SearchPaymentStubPage


class PaymentStubPage(SearchPaymentStubPage):
    def __init__(self, page):
        super().__init__(page)


