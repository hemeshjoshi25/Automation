from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.groups import GroupsPage
from constants.enums import PageTitles, GroupsTitles


class DeleteTripGroup(IscE2eTestCase):
    """Delete test Trip Group"""

    def setUp(self):
        super(DeleteTripGroup, self).setUp()
        # Initialize Groups page object
        self.groups = GroupsPage(self.driver)

    def test_a_nav_trip_groups(self):
        """Navigate to TG Page"""
        self.groups.nav_link.click()
        self.assertEqual(self.groups.title.text, PageTitles.PEOPLE_GROUPS.value)
        self.groups.trip_groups.click()
        self.assertEqual(self.groups.title.text, PageTitles.TRIP_GROUPS.value)

    def test_b_delete_tg(self):
        """Delete test TG(s)"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.groups.row_locator))
        self.groups.search_box.send_keys(GroupsTitles.TRIP_RENAME.value)
        self.groups.select_rows(GroupsTitles.TRIP_RENAME.value)
        self.groups.get_row_options(GroupsTitles.TRIP_RENAME.value).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.groups.row_options_locator))
        self.groups.option_delete.click()
        sleep(1)  # Wait for modal open animation
        self.groups.confirm_delete.click()

    def test_c_validate_deleted(self):
        """Validate TG delete"""
        self.groups.search_box.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.groups.row_locator))
        self.groups.search_box.send_keys(GroupsTitles.TRIP_RENAME.value)
        self.assertTrue(self.groups.empty_search_message)
        # Set to Pass
        self.__class__.test_result = 'pass'
