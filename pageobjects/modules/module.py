from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.IscE2eTestCase import IscE2eTestCase
from utils.decorators import update_implicit_timeout, retry_on_stale_element
from constants.enums import Selectors


class GenericModulePage(IscE2eTestCase):

    def __init__(self, driver):
        self.driver = driver
        self.test_case = IscE2eTestCase

    @property
    def title(self):
        return self.driver.find_element_by_css_selector(Selectors.MOD_TITLE.value)

    @property
    def report_title(self):
        return self.driver.find_element_by_css_selector(Selectors.REPORT_TITLE.value)

    @property
    def report_title_locator(self):
        return (By.CSS_SELECTOR, Selectors.REPORT_TITLE.value)

    def module_nav_link(self, slug):
        return self.driver.find_element_by_css_selector(Selectors.MOD_NAV_LINK.value.format(slug))

    @update_implicit_timeout(15)
    def report_nav_link(self, slug):
        return self.driver.find_element_by_css_selector(Selectors.REPORT_NAV_LINK.value.format(slug))

    @property
    def report_container_locator(self):
        return (By.CSS_SELECTOR, Selectors.REPORT_CONTAINER.value)

    @property
    def report_running_locator(self):
        return (By.CSS_SELECTOR, Selectors.REPORT_RUNNING.value)

    @property
    def close_notification(self):
        return self.driver.find_element_by_css_selector(Selectors.CLOSE_NOTIF.value)

    def assert_intercom(self):
        try:
            self.driver.find_element_by_xpath(Selectors.INTERCOM.value)
        except():
            raise Exception('Intercom button not found')

    @retry_on_stale_element
    def validate_nav(self, title):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.report_container_locator))
        self.assert_intercom()
        if self.report_title.text != title:
            raise Exception('Report title: {}, does not equal {} as expected'.format(self.report_title.text, title))
