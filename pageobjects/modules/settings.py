from selenium.webdriver.common.by import By
from pageobjects.modules.module import GenericModulePage
from constants.enums import Selectors


class SettingsPage(GenericModulePage):

    def __init__(self, driver):
        self.driver = driver

    @property
    def nav_link(self):
        return self.module_nav_link(Selectors.USER.value)

    @property
    def nav_link_locator(self):
        return (By.CSS_SELECTOR, Selectors.MOD_NAV_LINK.value.format(Selectors.USER.value))

    @property
    def logout(self):
        return self.driver.find_element_by_css_selector(Selectors.LOGOUT.value)
