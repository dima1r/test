from pages.elements_page import TextBoxPage, CheckboxPage, RadioButtonPage, WebTablePage, ButtonsPage
from pages.elements_page import LinksPage
from pages.elements_page import UploadAndDownloadPage
from pages.elements_page import DynamicPropertiesPage
import time
import random
import os

class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, url='https://demoqa.com/text-box')
            text_box_page.open()
            # text_box_page.fill_all_fields()
            full_name, email, cur_addr, per_addr = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

            print(full_name)
            print(output_name)
            assert full_name == output_name
            assert email == output_email


    class TestCheckBox:

        def test_checkbox(self, driver):
            checkbox_page = CheckboxPage(driver, url='https://demoqa.com/checkbox')
            checkbox_page.open()
            checkbox_page.open_full_list()
            checkbox_page.click_random_checkbox()
            input_checkbox = checkbox_page.get_checked_checkboxes()
            output_result = checkbox_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result


    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, url = 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            assert output_yes == 'Yes'
            assert output_impressive == 'Impressive'
            

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            time.sleep(5)
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            time.sleep(5)
            print(key_word)
            print(table_result)
            assert key_word in table_result

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            time.sleep(1)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            time.sleep(1)
            print(age)
            print(row)
            assert age in row

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100]

    class TestButtonPage:

        def test_different_click_on_the_buttons(self, driver):
            button_page = WebTablePage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            dbl = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            clck = button_page.click_on_different_button('click')
            print(dbl)
            print(right)
            print(clck)


    class TestLinksPage:

        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400


    class TestUploadAndDownload:

        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            local, uploaded = upload_download_page.upload_file()
            assert local == uploaded


        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True


    class TestDynamicPropertiesPage:

        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            # dynamic_properties_page.check_change_of_color()
            color_before, color_after = dynamic_properties_page.check_change_of_color()
            assert color_before != color_after

        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()
            assert appear is True

        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            ena = dynamic_properties_page.check_enable_button()
            assert ena is True