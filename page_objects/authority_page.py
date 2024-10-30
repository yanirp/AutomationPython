from page_objects.base_page import BasePage

class AuthorityPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.standing_order_icon_btn = page.locator("//div[contains(text(),'הצטרפות להוראת קבע באשראי')]")

    def click_standing_order_icon_btn(self):
        self.standing_order_icon_btn.click()
