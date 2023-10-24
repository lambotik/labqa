import allure

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.timeout = 10

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    def open(self):
        with allure.step(f'Open page: {self.url}'):
            self.driver.get(self.url)

    @allure.step('Check element is visible and clickable')
    def element_is_presence_and_clickable(self, locator):
        return (Wait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}") and
                self.element_is_clickable(locator))

    @allure.step('Check element is clickable')
    def element_is_clickable(self, locator):
        return Wait(self.driver, self.timeout).until(ec.element_to_be_clickable(locator),
                                                     message=f"Can't find element by locator {locator}")

    @allure.step('Check element is presence')
    def element_is_presence(self, locator):
        return Wait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator),
                                                     message=f"Can't find element by locator {locator}")

    def go_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView({ block: "center"});',
                                   element)

    def element_is_visible_and_clickable(self, locator):
        self.go_to_element(self.element_is_presence(locator))
        return Wait(self.driver, self.timeout).until(ec.element_to_be_clickable(locator),
                                                     message=f"Can't find element by locator {locator}")
