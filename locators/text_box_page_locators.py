from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Input
    INPUT_FULL_NAME = (By.ID, "userName")
    INPUT_EMAIL = (By.ID, "userEmail")
    INPUT_CURRENT_ADDRESS = (By.ID, "currentAddress")
    INPUT_PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "#submit")

    # Table
    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    CURRENT_ADDRESS = (By.XPATH, '//p[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//p[@id="permanentAddress"]')
