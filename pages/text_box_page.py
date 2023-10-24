import allure

from data.generator import generated_person
from locators.text_box_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    person_info = next(generated_person())
    user_info = {f'full_name': person_info.full_name,
                 'email': person_info.email,
                 'current_address': person_info.current_address,
                 'permanent_address': person_info.permanent_address}

    def fill_fields(self) -> list:
        """
        This method's fill fields use user data generated from the Faker library.:

        user_info['full_name']: str

        user_info['email']: str

        user_info['current_address']: str

       user_info['permanent_address']: str

        And click button Submit
        """
        with allure.step(f"Input customer full name:{self.user_info['full_name']}."):
            self.element_is_presence_and_clickable(self.locators.INPUT_FULL_NAME).send_keys(self.user_info['full_name'])
        with allure.step(f"Input customer email:{self.user_info['email']}."):
            self.element_is_presence_and_clickable(self.locators.INPUT_EMAIL).send_keys(self.user_info['email'])
        with allure.step(f"Input customer current_address:{self.user_info['current_address']}."):
            self.element_is_presence_and_clickable(self.locators.INPUT_CURRENT_ADDRESS).send_keys(
                self.user_info['current_address'])
        with allure.step(f"Input customer permanent_address:{self.user_info['permanent_address']}."):
            self.element_is_presence_and_clickable(self.locators.INPUT_PERMANENT_ADDRESS).send_keys(
                self.user_info['permanent_address'])
        with allure.step(f"Scroll to Submit button."):
            self.element_is_visible_and_clickable(self.locators.BUTTON_SUBMIT)
        with allure.step(f"Click to Submit button."):
            self.element_is_presence_and_clickable(self.locators.BUTTON_SUBMIT).click()
        return list(self.user_info.values())

    def get_user_info_from_table(self) -> list:
        """
        This method checks the parameters from the table while stripping the column names.
        :return: [name, email, current_address, permanent_address]
        """
        name = self.element_is_presence(self.locators.NAME).text.replace('Name:', '')
        email = self.element_is_presence(self.locators.EMAIL).text.replace('Email:', '')
        current_address = self.element_is_presence(self.locators.CURRENT_ADDRESS).text.replace('Current Address :', '')
        permanent_address = self.element_is_presence(self.locators.PERMANENT_ADDRESS).text.replace(
            'Permananet Address :', '')
        with allure.step(f'Getting table values:{[name, email, current_address, permanent_address]}'):
            pass
        return [name, email, current_address, permanent_address]
