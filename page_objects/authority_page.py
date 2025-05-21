import time

from data_base.sms_registration import SmsRegistration
from page_objects.base_page import BasePage

class AuthorityPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.standing_order_icon_btn = page.locator("//div[contains(text(),'הצטרפות להוראת קבע באשראי')]")
        self.login_btn = page.locator("//button[contains(text(),'התחברות')]")
        self.login_input = page.locator("//input[@data-placeholder='מספר נייד']")
        self.otp_input = page.locator("//input[@data-placeholder='הזן כאן את הקוד']")
        self.submit_login_btn = page.locator("//button[contains(text(),'שלח')]")

    def click_standing_order_icon_btn(self):
        self.standing_order_icon_btn.click()

    def user_login_to_mast_with_asset(self,phone):
        self.login_btn.click()
        self.page.fill("//input[@data-placeholder='מספר נייד']", phone)
        self.submit_login_btn.click()
        time.sleep(5)
        otp = SmsRegistration.get_last_sms_by_phone(phone)
        assert otp, "OTP was None – failed to get password from DB or CI"
        self.page.fill("//input[@data-placeholder='הזן כאן את הקוד']" ,str(otp))
        self.submit_login_btn.click()