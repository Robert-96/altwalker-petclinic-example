from selenium.webdriver.common.by import By

from .base import BasePage


class NewOwnerPage(BasePage):
    """New Owner Page Object Model"""

    _submit_button_locator = (By.CSS_SELECTOR, "button[type=\"submit\"]")

    _firstname_locator = (By.ID, "firstName")
    _lastname_locator = (By.ID, "lastName")
    _address_locator = (By.ID, "address")
    _city_locator = (By.ID, "city")
    _telephone_locator = (By.ID, "telephone")

    _error_message_locator = (By.CSS_SELECTOR, "form span.help-inline")

    @property
    def error_message(self):
        return self.find_element(*self._error_message_locator).text

    def fill_owner_data(self, first_name="", last_name="", address="", city="", telephone=""):
        self.find_element(*self._firstname_locator).clear()
        self.find_element(*self._firstname_locator).send_keys(first_name)
        self.find_element(*self._lastname_locator).clear()
        self.find_element(*self._lastname_locator).send_keys(last_name)
        self.find_element(*self._address_locator).clear()
        self.find_element(*self._address_locator).send_keys(address)
        self.find_element(*self._city_locator).clear()
        self.find_element(*self._city_locator).send_keys(city)
        self.find_element(*self._telephone_locator).clear()
        self.find_element(*self._telephone_locator).send_keys(telephone)

    def fill_telephone(self, telephone):
        self.find_element(*self._telephone_locator).send_keys(telephone)

    def click_submit(self):
        self.find_element(*self._submit_button_locator).click()
