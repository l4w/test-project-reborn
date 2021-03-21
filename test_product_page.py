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
    pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail(reason='FIXING')),
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

product_page_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'

@pytest.mark.skip(reason='Test case is for test')
def test_guest_cant_see_success_message_after_adding_product_to_busket_02(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.add_to_bucket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message_03(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip(reason='Test case is for test')
def test_message_dissapear_after_adding_product_to_busket_04(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.add_to_bucket()
    page.success_message_should_dissapear()
