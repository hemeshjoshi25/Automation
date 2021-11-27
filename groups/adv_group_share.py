from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.adv_groups import AdvGroupsPage
from pageobjects.modules.settings import SettingsPage
from pageobjects.login import LoginPage
from pageobjects.modules.people import PeoplePage
from constants.enums import PageTitles, GroupsTitles, Attributes
from settings import LOGIN_EMAIL_1, LOGIN_PASSWORD


class ShareAdvGroup(IscE2eTestCase):
    """Test the functionality of sharing an Advanced Group"""

    def setUp(self):
        super(ShareAdvGroup, self).setUp()
        # Initialize page objects
        self.adv = AdvGroupsPage(self.driver)
        self.settings = SettingsPage(self.driver)
        self.login = LoginPage(self.driver)
        self.people = PeoplePage(self.driver)

    def test_a_nav_adv_groups(self):
        """Navigate to Advanced Groups Page"""
        self.adv.nav_link.click()
        self.assertEqual(self.adv.title.text, PageTitles.PROD_GROUPS.value)

    def test_b_share_adv_group(self):
        """Share Adv Group with 2nd test account"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.send_keys(GroupsTitles.ADV_FOLDER.value)
        self.adv.get_row_options(GroupsTitles.ADV_FOLDER.value).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.adv.row_options_locator))
        self.adv.option_share.click()
        sleep(1)  # Wait for modal open animation
        self.adv.share_input.send_keys(GroupsTitles.SHARE_SEARCH.value)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.adv.share_user_locator))
        self.adv.share_user(GroupsTitles.SHARE_USER.value).click()
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(
            self.adv.share_button_locator, GroupsTitles.SHARE_BUTTON.value.format('1')))
        self.adv.share_button.click()

    def test_c_change_account(self):
        """Change to 2nd test account"""
        self.adv.close_message.click()
        self.settings.nav_link.click()
        self.assertEqual(self.settings.title.text, PageTitles.SETTINGS.value)
        self.settings.logout.click()
        self.assertIsNotNone(self.login.login)
        self.login.log_in(LOGIN_EMAIL_1, LOGIN_PASSWORD)
        self.assertEqual(self.people.title.text, PageTitles.PEOPLE.value)

    def test_d_validate_share(self):
        """Validate Adv Group share"""
        self.test_a_nav_adv_groups()
        self.adv.shared_with.click()
        self.assertIn(Attributes.SELECTED.value, self.adv.shared_with.get_attribute(Attributes.CLASS.value))
        self.adv.search_box.send_keys(GroupsTitles.ADV_FOLDER.value)
        self.adv.get_rows(GroupsTitles.ADV_FOLDER.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
