from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_bucket(self):
        bucket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BUCKET_BTN)
        bucket_btn.click()

    def should_be_message_after_add_to_bucket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_AFTER_ADDING), 'Message after adding a product to the busket is absent.'
        
    def should_be_correct_product_name_in_message(self):  
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message_after_adding = self.browser.find_element(*ProductPageLocators.MESSAGE_AFTER_ADDING_TEXT)
        assert product_name.text == message_after_adding.text, 'There is no product name in the message after adding to the busket.'

    def should_be_busket_cost_message(self):
        assert self.is_element_present(*ProductPageLocators.BUSKET_MESSAGE), 'There is no bucket cost message.'

    def should_be_correct_price_in_busket(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        bucket_cost = self.browser.find_element(*ProductPageLocators.BUSKET_COST)
        assert product_cost.text == bucket_cost.text, 'Product cost doesnt equal bucket cost.'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_AFTER_ADDING), 'Success message after adding a product in the busket is present.'

    def success_message_should_dissapear(self):
        assert self.is_dissapeared(*ProductPageLocators.MESSAGE_AFTER_ADDING), 'Success message after adding a product in the busket wont dissapear.'
