from playwright.sync_api import Page
from page_objects.base_page import BasePage


class StandingOrderPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.full_name = page.locator("//input[@id='name']")
        self.id_number = page.locator("//input[@id='tz']")
        self.phone_number = page.locator("//input[@id='lastName']")  # Potential ID typo
        self.payer_number = page.locator("//input[@id='payerId']")
        self.asset_number = page.locator("//input[@id='assetNum']")
        self.mail = page.locator("//input[@id='email']")
        self.next_button = page.locator("//button[@id='next']")
        self.card_number = page.locator("//input[@id='creditCard']")
        self.valid_month = page.locator("//select[@id='validMonth']")
        self.valid_year = page.locator("//select[@id='validYear']")
        self.disclaimer = page.locator("//input[@id='disclaimer']")
        self.signature = page.locator("//body/app-root/app-main-nav/mat-sidenav-container/mat-sidenav-content/div/app-standing-order/div/form/app-standing-order-disclaimer/div/section/div[2]/figure/app-digital-signature/div/canvas")
        self.submit_button = page.locator("//body/app-root[1]/app-main-nav[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/div[1]/app-standing-order[1]/div[1]/form[1]/app-standing-order-disclaimer[1]/div[1]/section[1]/div[3]/input[1]")
        self.standing_order_success_message = page.locator("body.INDlangdirRTL.INDpositionLeft.INDDesktop.INDChrome.INDhasDragTooltip:nth-child(2) mat-sidenav-container.mat-drawer-container.mat-sidenav-container.sidenav-container mat-sidenav-content.mat-drawer-content.mat-sidenav-content:nth-child(5) div.main-content:nth-child(2) app-standing-order.ng-star-inserted:nth-child(2) app-standing-order-final-page.ng-star-inserted div.theWizard section.marginTop > h2:nth-child(5)")

    def fill_first_page_standing_order(self, name, id_number, phone_number, payer_id, asset_num, email):
        self.page.fill("#name", name)
        self.page.fill("#tz", id_number)
        self.page.fill("#lastName", phone_number)
        self.page.fill("#payerId", payer_id)
        self.page.fill("#assetNum", asset_num)
        self.page.fill("#email", email)
        self.next_button.click()

    def fill_second_page_standing_order(self, card_number, month, year):
        self.page.fill("#creditCard",card_number)
        self.page.select_option("#validMonth", month)
        self.page.select_option("#validYear", year)
        self.next_button.click()

    def fill_third_page_standing_order(self):
        self.page.check("#disclaimer")
        self.signature.click()

    def submit_fill_standing_order(self):
        self.submit_button.click()
