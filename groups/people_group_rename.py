from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.groups import GroupsPage
from constants.enums import PageTitles, GroupsTitles


class RenamePeopleGroup(IscE2eTestCase):
    """Rename test People Group"""

    def setUp(self):
        super(RenamePeopleGroup, self).setUp()
        # Initialize Groups page object
        self.groups = GroupsPage(self.driver)

    def test_a_open_pg_page(self):
        """Navigate to PG Page"""
        self.groups.nav_link.click()
        self.assertEqual(self.groups.title.text, PageTitles.PEOPLE_GROUPS.value)

    def test_b_rename_pg(self):
        """Rename test PG(s)"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.groups.row_locator))
        self.groups.search_box.send_keys(GroupsTitles.PEOPLE_NAME.value)
        for r, row in enumerate(self.groups.get_rows(GroupsTitles.PEOPLE_NAME.value)):
            if r != 0:
                WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.groups.row_locator))
                self.groups.search_box.send_keys(GroupsTitles.PEOPLE_NAME.value)
            self.groups.get_row_options(GroupsTitles.PEOPLE_NAME.value).click()
            WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.groups.row_options_locator))
            self.groups.option_rename.click()
            self.groups.modal_input.send_keys(GroupsTitles.PEOPLE_RENAME.value)
            self.groups.modal_save_btn.click()
            sleep(1)  # Wait for modal close animation

    def test_c_validate_rename(self):
        """Validate PG rename"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.groups.row_locator))
        self.groups.search_box.click()
        self.groups.search_box.send_keys(GroupsTitles.PEOPLE_RENAME.value)
        for row in self.groups.get_rows(GroupsTitles.PEOPLE_RENAME.value):
            self.assertEqual(self.groups.get_row_title(row), GroupsTitles.PEOPLE_RENAME.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
