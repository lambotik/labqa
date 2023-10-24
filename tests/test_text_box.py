import allure

from pages.text_box_page import TextBoxPage


@allure.title("Test text box form.")
def test_textbox_form(driver):
    """This test checks the data entered and the data in the displayed table."""
    text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    text_box_page.open()
    user_entered = text_box_page.fill_fields()
    info_in_table = text_box_page.get_user_info_from_table()
    assert user_entered == info_in_table, 'The data entered and the data in the table do not match.'
