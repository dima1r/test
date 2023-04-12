from locators.elements_page_locators import TextBoxPagelocators
from pages.base_page import BasePage
from time import sleep

class TextBoxPage(BasePage):
    locators = TextBoxPagelocators()
    # def __init__(self, driver, url):
    #     super().__init__(driver, url)
        
    #     self.name = 'Vasiliy Petrov'
    #     self.email = 'Petrov@mail.com'
    #     self.cur_addr = 'Cur address'
    #     self.per_addr = 'Per address'

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Vasiliy Petrov')
        self.element_is_visible(self.locators.EMAIL).send_keys('Petrov@mail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('Cur address')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Per address')
        sleep(1)
        self.element_is_visible(self.locators.SUBMIT).click()

        sleep(5)

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text
        email = self.element_is_present(self.locators.CREATED_EMAIL).text
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text
        return full_name, email, current_address, permanent_address