from pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('product_page_link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'
])
def test_guest_can_add_product_to_busket_01(browser, product_page_link):
    
    page = ProductPage(browser, product_page_link)
    page.open()
    page.add_to_bucket()
    page.solve_quiz_and_get_code()
    page.should_be_message_after_add_to_bucket()
    page.should_be_correct_product_name_in_message()
    page.should_be_busket_cost_message()
    page.should_be_correct_price_in_busket()
