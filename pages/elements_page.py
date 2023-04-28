from sources.generator.generator import generated_person
from locators.elements_page_locators import TextBoxPagelocators
from locators.elements_page_locators import CheckboxPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
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
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        sleep(1)
        self.scroll_down()
        self.element_is_present(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address
        sleep(5)

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckboxPage(BasePage):
    locators = CheckboxPageLocators()

    def open_full_list(self):
        btn = self.element_is_visible(self.locators.EXPAND_ALL_BUTTON)
        print(btn)
        # btn.click()
        btn = self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/div/button[1]')
        print(btn)
        btn.click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        for item in item_list:
            print(item.text)

