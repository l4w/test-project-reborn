from .base_page import BasePage
from .locators import BucketPageLocators

class BucketPage(BasePage):

    def should_be_empty_bucket_page(self):
        self.should_be_bucket_page_url()
        self.should_be_empty_bucket()
        self.should_be_message_if_empty_bucket()
    
    def should_be_bucket_page_url(self):
        assert 'basket' in self.browser.current_url, 'Bucket page URL isnt correct.'

    def should_be_empty_bucket(self):
        assert self.is_not_element_present(*BucketPageLocators.BUCKET_ITEMS_BLOCK), 'Bucket is not empty.'

    def should_be_message_if_empty_bucket(self):
        assert self.is_element_present(*BucketPageLocators.EMPTY_BUCKET_MESSAGE_SELECTOR), 'There is no message about empty bucket.'

    