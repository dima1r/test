import conftest
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def goto_element(self, element):
        #self.driver.execute_script('argument[0].scrollIntoView(element);')
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 200)")
        sleep(5)

    def action_double_click(self):
        action = ActionChain(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self):
        action = ActionChain(self.driver)
        action.context_click(element)
        action.perform()