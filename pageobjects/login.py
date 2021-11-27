from selenium.common.exceptions import NoSuchElementException
from utils.decorators import retry_on_no_element, retry_on_stale_element
from constants.enums import Selectors


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    @retry_on_no_element
    @retry_on_stale_element
    def username(self):
        """Returns username input box"""
        return self.driver.find_element_by_id(Selectors.USERNAME.value)

    @property
    @retry_on_no_element
    @retry_on_stale_element
    def password(self):
        """Returns password input box"""
        return self.driver.find_element_by_id(Selectors.PASSWORD.value)

    @property
    @retry_on_no_element
    @retry_on_stale_element
    def login(self):
        """Returns 'Log In' button"""
        return self.driver.find_element_by_css_selector(Selectors.LOGIN.value)

    def log_in(self, user, password):
        """
        Enters username & password and clicks 'Log In' button
        :Args:
         - user - username for login (test@numerator.com)
         - password - password for login (insights2.0)
        """
        try:
            self.username.send_keys(user)
            self.password.send_keys(password)
            self.login.click()
        except NoSuchElementException:
            self.driver.navigate().refresh()
            self.username.send_keys(user)
            self.password.send_keys(password)
            self.login.click()
