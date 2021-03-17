from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.browser.find_element(By.CSS_SELECTOR, '[name="login_submit"]')

