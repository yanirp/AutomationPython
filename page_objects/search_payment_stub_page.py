from playwright.sync_api import Page
from page_objects.base_page import BasePage


class SearchPaymentStubPage(BasePage):
    def __init__(self, page: Page, payment_stub_details):
        super().__init__(page)
        self.payment_stub_details = payment_stub_details

        self.frame = page.frame_locator("iframe[src*='SearchPay']")
        self.payer_number = self.frame.locator("//input[@id='txtMeshalem']")
        self.stub_number = self.frame.locator("//input[@id='txtSefah']")
        self.proceed_payment_btn = self.frame.locator("//button[@id='submit']")
        self.text_success_to_load_payment_stub = self.frame.locator("//h2[contains(text(),'נא מלא את פרטי התשלום')]")

    def search_payment_stub(self, payer_number , stub_number):
        self.payer_number.fill(payer_number)
        self.stub_number.fill(stub_number)
        self.proceed_payment_btn.click()