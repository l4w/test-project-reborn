from pages.main_page import MainPage
from pages.login_page import LoginPage

main_link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_01(browser):

    page = MainPage(browser, main_link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_02(browser):
    
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_login_page()
    # verifying that we are exact on the login page
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()




