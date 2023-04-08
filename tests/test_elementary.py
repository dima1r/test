from pages.base_page import BasePage
from time import sleep

def test_main(driver):
    page = BasePage(driver, 'https://www.google.com')
    #page = BasePage(driver, 'google.com')
    page.open()
    sleep(5)
    cur_url = driver.current_url
    print(cur_url)
    assert 'https://www.google.com' in cur_url, 'Page not found'