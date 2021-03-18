from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_page_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_page_url(self):
        assert 'login' in self.browser.current_url, 'Check URL of your login page.'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'No login form on the page.'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'No register form on the page.'

