import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage
from conftest import driver
class TestElements:
    class TestTextBox:


        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addr, output_perm_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "ошибка имени"
            assert email == output_email, "ошибка email"
            assert current_address == output_curr_addr, "ошибка текущего адреса"
            assert permanent_address == output_perm_addr, "ошибка постоянного адреса"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkbox()
            output_checkbox = check_box_page.get_output_checkbox()
            print()
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox, "checkbox is not selected"
            time.sleep(3)

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.choose_radio_button('yes')
            output_yes = radio_button_page.get_output_radiobutton()
            radio_button_page.choose_radio_button('impressive')
            output_impressive = radio_button_page.get_output_radiobutton()
            radio_button_page.choose_radio_button('no')
            output_no = radio_button_page.get_output_radiobutton()
            assert output_yes == "Yes", "RadioButton 'Yes' not valid"
            assert output_impressive == "Impressive", "RadioButton 'Impressive' not valid"
            assert output_no == "No", "RadioButton 'No' not valid"
