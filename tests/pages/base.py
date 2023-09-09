from pypom import Page
from selenium.webdriver.common.by import By


class BasePage(Page):
    """Interact with elements common on every page, which in this case are the top menu links."""

    _home_locator = (By.CSS_SELECTOR, "a[title=\"home page\"]")
    _find_owners_locator = (By.CSS_SELECTOR, "a[title=\"find owners\"]")
    _veterinarians_locator = (By.CSS_SELECTOR, "a[title=\"veterinarians\"]")

    _footer_logo_locator = (By.CSS_SELECTOR, "img.logo")
    _heading_locator = (By.TAG_NAME, "h2")

    @property
    def is_footer_present(self):
        return self.is_element_present(*self._footer_logo_locator)

    @property
    def heading_text(self):
        return self.find_element(*self._heading_locator).text

    def click_home(self):
        self.find_element(*self._home_locator).click()

    def click_find_owners(self):
        self.find_element(*self._find_owners_locator).click()

    def click_veterinarians(self):
        self.find_element(*self._veterinarians_locator).click()
