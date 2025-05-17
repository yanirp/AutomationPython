import time
import pytest
from playwright.async_api import Page
from models.credit_card_user_details import credit_card_data
from models.standing_order_user_details import standing_order_data
from page_objects.authority_page import AuthorityPage
from page_objects.standing_order_page import StandingOrderPage


@pytest.mark.description("Test end to end standing order process")
def test_standing_order_page_e2e(page: Page):
    authority_page = AuthorityPage(page)
    standing_order_page = StandingOrderPage(page)

    authority_page.click_standing_order_icon_btn()
    standing_order_page.fill_first_page_standing_order(
        standing_order_data.name,
        standing_order_data.id,
        standing_order_data.phone,
        standing_order_data.payer,
        standing_order_data.asset,
        standing_order_data.mail)
    standing_order_page.fill_second_page_standing_order(
        credit_card_data.card_number,
        credit_card_data.month,
        credit_card_data.year)
    standing_order_page.fill_third_page_standing_order()
    standing_order_page.submit_fill_standing_order()
    time.sleep(30)
    assert standing_order_page.standing_order_success_message.is_visible(),"Success message not visible"



#def test_standing_order_page_e2e_with_data(page: Page):
  #  test_standing_order_page_e2e(page, standing_order_data,credit_card_data)
