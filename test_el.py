from pages.base_page import BasePage
from time import sleep

def test(driver):
    page = BasePage(driver, 'https://www.google.com')
    #page = BasePage(driver, 'google.com')
    page.open()
    sleep(5)