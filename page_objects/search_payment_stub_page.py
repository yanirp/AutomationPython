import re
from playwright._impl._errors import TimeoutError
from playwright.sync_api import Page, Expect
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
        self.error_message = self.frame.locator("//label[@id='info_message']")

    def search_payment_stub(self, payer_number , stub_number):
        self.payer_number.fill(payer_number)
        self.stub_number.fill(stub_number)
        self.proceed_payment_btn.click()


    def check_errors_for_getting_to_payment_page(self) -> str:
        """Check for error messages immediately after clicking the button."""
        if self.error_message.is_visible():
            error_text = self.error_message.inner_text()
            if "ספח זה שולם" in error_text:
                return "Stub already paid"
            elif "שגיאה בחיבור לשרת הספחים, נסה מאוחר יותר" in error_text:
                return "Connection error"
            elif "הספח לא נמצא. נא לנסות שנית" in error_text or "הספח לא נמצא. נא לנסות שנית" in error_text:
                return "Stub is not valid / not found"

        return "No errors"

    def is_success_to_load_payment_stub(self) -> bool:
        pattern = re.compile(r"PayNow")
        iframe = self.page.locator("iframe[src*='SearchPay']").element_handle()
        iframe_content = iframe.content_frame() if iframe else None
        if iframe_content:
            try:
                # Attempt to wait for the URL in the iframe to match the pattern
                iframe_content.wait_for_url(pattern, timeout=5000)
                return self.text_success_to_load_payment_stub.is_visible()
            except TimeoutError:
                # Handle specific errors if timeout occurs by checking error message text
                error_message = self.check_errors_for_getting_to_payment_page()
                if error_message != "No errors":
                    print(f"Error detected: {error_message}")
                else:
                    print("Unknown timeout error occurred while waiting for iframe URL.")
                return False
        else:
            print("Iframe or iframe content could not be accessed.")
            return False