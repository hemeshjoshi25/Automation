from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.groups import GroupsPage
from pageobjects.modules.settings import SettingsPage
from pageobjects.login import LoginPage
from pageobjects.modules.people import PeoplePage
from constants.enums import PageTitles, GroupsTitles, Attributes
from settings import LOGIN_EMAIL_1, LOGIN_PASSWORD


class ShareTripGroup(IscE2eTestCase):
    """Test the functionality of sharing a Trip Group"""

    def setUp(self):
        super(ShareTripGroup, self).setUp()
        # Initialize page objects
        self.groups = GroupsPage(self.driver)
        self.settings = SettingsPage(self.driver)
        self.login = LoginPage(self.driver)
        self.people = PeoplePage(self.driver)

    def test_a_open_tg_page(self):
        """Navigate to TG Page"""
        self.groups.nav_link.click()
        self.assertEqual(self.groups.title.text, PageTitles.PEOPLE_GROUPS.value)
        self.groups.trip_groups.click()
        self.assertEqual(self.groups.title.text, PageTitles.TRIP_GROUPS.value)

    def test_b_share_tg(self):
        """Share TG with 2nd test account"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.groups.row_locator))
        self.groups.search_box.send_keys(GroupsTitles.TRIP_NAME.value)
        self.groups.get_row_options(GroupsTitles.TRIP_NAME.value).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.groups.row_options_locator))
        self.groups.option_tg_share.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.groups.share_user_locator))
        self.groups.share_input.send_keys(GroupsTitles.SHARE_SEARCH.value)
        self.groups.share_user(GroupsTitles.SHARE_USER.value).click()
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(
            self.groups.share_button_locator, GroupsTitles.SHARE_BUTTON.value.format('1')))
        self.groups.share_button.click()

    def test_c_change_account(self):
        """Change to 2nd test account"""
        self.groups.close_message.click()
        self.settings.nav_link.click()
        self.assertEqual(self.settings.title.text, PageTitles.SETTINGS.value)
        self.settings.logout.click()
        self.assertIsNotNone(self.login.login)
        self.login.log_in(LOGIN_EMAIL_1, LOGIN_PASSWORD)
        self.assertEqual(self.people.title.text, PageTitles.PEOPLE.value)

    def test_d_validate_share(self):
        """Validate TG share"""
        self.test_a_open_tg_page()
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.groups.row_locator))
        self.groups.shared_with.click()
        self.assertIn(Attributes.SELECTED.value, self.groups.shared_with.get_attribute(Attributes.CLASS.value))
        self.groups.search_box.send_keys(GroupsTitles.TRIP_NAME.value)
        self.groups.get_rows(GroupsTitles.TRIP_NAME.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
