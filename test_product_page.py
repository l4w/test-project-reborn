from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.bucket_page import BucketPage
import time
import pytest

product_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'

# LOGIN BLOCK (IMPLEMENT class LATER)

def test_guest_can_see_login_link_on_product_page_05(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_from_product_page_06(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()
    # verifying that we are exact on the login page
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
# ----------------------------------

class TestUserCanAddToBucketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, "!&@^%^$(kHJDSmnDSd876")
        login_page.should_be_authorized_user()

    def test_user_can_add_product_to_bucket_08(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_to_bucket()
        # page.solve_quiz_and_get_code() #its used w/ promo-actions
        page.should_be_message_after_add_to_bucket()
        page.should_be_correct_product_name_in_message()
        page.should_be_busket_cost_message()
        page.should_be_correct_price_in_busket()

    def test_user_cant_see_success_message_09(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()

# GUEST BUCKET BLOCK (IMPLEMENT class LATER)

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
def test_guest_can_add_product_to_bucket_01(browser, product_page_link):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.add_to_bucket()
    page.solve_quiz_and_get_code()
    page.should_be_message_after_add_to_bucket()
    page.should_be_correct_product_name_in_message()
    page.should_be_busket_cost_message()
    page.should_be_correct_price_in_busket()

@pytest.mark.skip(reason='Test case is for test negative cases')
def test_guest_cant_see_success_message_after_adding_product_to_bucket_02(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_bucket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message_03(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip(reason='Test case is for test negative cases')
def test_message_dissapear_after_adding_product_to_bucket_04(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_bucket()
    page.success_message_should_dissapear()

def test_guest_cant_see_product_in_bucket_opened_from_product_page_07(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_bucket()
    # verifying that we are exact on the bucket page
    bucket_page = BucketPage(browser, browser.current_url)
    bucket_page.should_be_empty_bucket_page()
#-------------------------------------------