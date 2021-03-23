from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BUCKET_VIEW = (By.CSS_SELECTOR, '.btn-group .btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class BucketPageLocators:
    EMPTY_BUCKET_MESSAGE_SELECTOR = (By.CSS_SELECTOR, '#content_inner>p')
    BUCKET_ITEMS_BLOCK = (By.CSS_SELECTOR, '#basket-items')

class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_BTN = (By.CSS_SELECTOR, '.register_form .btn-primary')

class ProductPageLocators:
    ADD_TO_BUCKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_COST = (By.CSS_SELECTOR, 'p.price_color')
    MESSAGE_AFTER_ADDING = (By.CSS_SELECTOR, '.alert-success')
    MESSAGE_AFTER_ADDING_TEXT = (By.CSS_SELECTOR, '.alertinner strong')
    BUSKET_MESSAGE = (By.CSS_SELECTOR, '.alert-info')
    BUSKET_COST = (By.CSS_SELECTOR, '.alert-info strong')
