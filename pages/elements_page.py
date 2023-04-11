from locators.elements_page_locators import TextBoxPagelocators
from pages.base_page import BasePage
from time import sleep

class TextBoxPage(BasePage):
    locators = TextBoxPagelocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Vasiliy Petrov')
        self.element_is_visible(self.locators.EMAIL).send_keys('Petrov@mail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('Cur address')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Per address')
        self.element_is_visible(self.locators.SUBMIT).click()

        sleep(5)
