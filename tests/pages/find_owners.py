from selenium.webdriver.common.by import By

from .base import BasePage


class FindOwnersPage(BasePage):
    """Finds Owners Page Object Model"""

    _submit_button_locator = (By.CSS_SELECTOR, "button[type=\"submit\"]")
    _search_icon_locator = (By.CLASS_NAME, "icon-search")
    _add_owner_locator = (By.LINK_TEXT, "Add Owner")

    def click_submit(self):
        self.find_element(*self._submit_button_locator).click()

    def click_search(self):
        self.find_element(*self._search_icon_locator).click()

    def click_add_owner(self):
        self.find_element(*self._add_owner_locator).click()
