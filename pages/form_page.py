from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators
from sources.generator.generator import generated_person
from sources.generator.generator import generated_file
from selenium.webdriver.common.keys import Keys
import os

class FormPage(BasePage):
    locaors = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.element_is_visible(self.locaors.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locaors.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locaors.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locaors.GENDER).click()
        self.element_is_visible(self.locaors.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locaors.SUBJECT).send_keys('Math')
        self.element_is_visible(self.locaors.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locaors.HOBBIES).click()
        self.element_is_present(self.locaors.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locaors.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.locaors.SELECT_STATE).click()
        self.element_is_visible(self.locaors.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locaors.SELECT_CITY).click()
        self.element_is_visible(self.locaors.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locaors.SUBMIT).click()

        return person
