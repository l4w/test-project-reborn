from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.bucket_page import BucketPage
import pytest

main_link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_should_see_login_link_01(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_02(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.go_to_login_page()
        # verifying that we are exact on the login page
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_bucket_opened_from_main_page_03(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_bucket()
    # verifying that we are exact on the bucket page
    bucket_page = BucketPage(browser, browser.current_url)
    bucket_page.should_be_empty_bucket_page()





