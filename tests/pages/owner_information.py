from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base import BasePage


class OwnerInformationPage(BasePage):
    """Owner Information Page Object Model."""

    _submit_button_locator = (By.CSS_SELECTOR, "button[type=\"submit\"]")
    _add_new_pet_locator = (By.LINK_TEXT, "Add New Pet")
    _edit_pet_locator = (By.LINK_TEXT, "Edit Pet")
    _add_visit_locator = (By.LINK_TEXT, "Add Visit")

    # Pet Info
    _name_input_locator = (By.ID, "name")
    _birth_date_input_locator = (By.ID, "birthDate")
    _type_locator = (By.ID, "type")

    # Pets & Visits Info
    _description_locator = (By.ID, "description")
    _pets_locator = (By.XPATH, "//table/tbody/tr/td//dl")

    def click_add_new_pet(self):
        self.find_element(*self._add_new_pet_locator).click()

    def click_edit_pet(self):
        self.find_element(*self._edit_pet_locator).click()

    def click_add_visit(self):
        self.find_element(*self._add_visit_locator).click()

    def fill_out_pet_info(self, name=None, birth_date=None, type=None):
        name_input = self.find_element(*self._name_input_locator)
        # name_input.click()
        name_input.clear()

        if name:
            name_input.send_keys(name)

        birth_date_input = self.find_element(*self._birth_date_input_locator)
        # birth_date_input.click()
        birth_date_input.clear()

        if birth_date:
            birth_date_input.send_keys(birth_date.strftime("%Y-%m-%d"))

        if type:
            select = Select(self.find_element(*self._type_locator))
            select.select_by_value(type)

    def click_submit(self):
        self.find_element(*self._submit_button_locator).click()

    def clear_description(self):
        self.find_element(*self._description_locator).clear()

    def set_description(self, text=""):
        self.find_element(*self._description_locator).send_keys(text)

    @property
    def number_of_pets(self):
        return len(self.find_elements(*self._pets_locator))
