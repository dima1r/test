from pages.elements_page import TextBoxPage, CheckboxPage

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
            