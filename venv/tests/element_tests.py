import time
from pages.elements_page import TextBoxPage
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