from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.adv_groups import AdvGroupsPage
from constants.enums import PageTitles, GroupsTitles


class RenameAdvGroup(IscE2eTestCase):
    """Rename test Advanced Group Folder"""

    def setUp(self):
        super(RenameAdvGroup, self).setUp()
        # Initialize Adv Groups page object
        self.adv = AdvGroupsPage(self.driver)

    def test_a_nav_adv_groups(self):
        """Navigate to Adv Groups Page"""
        self.adv.nav_link.click()
        self.assertEqual(self.adv.title.text, PageTitles.PROD_GROUPS.value)

    def test_b_rename_adv_group(self):
        """Rename test Adv Group Folder(s)"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.send_keys(GroupsTitles.ADV_FOLDER.value)
        for r, row in enumerate(self.adv.get_rows(GroupsTitles.ADV_FOLDER.value)):
            if r != 0:
                WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.adv.row_locator))
                self.adv.search_box.send_keys(GroupsTitles.ADV_FOLDER.value)
            self.adv.get_row_options(GroupsTitles.ADV_FOLDER.value).click()
            WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.adv.row_options_locator))
            self.adv.option_rename.click()
            self.adv.modal_input.send_keys(GroupsTitles.ADV_RENAME.value)
            self.adv.rename_save_btn.click()
            sleep(1)  # Wait for modal close animation

    def test_c_validate_rename(self):
        """Validate Adv Group Folder rename"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.click()
        self.adv.search_box.send_keys(GroupsTitles.ADV_RENAME.value)
        for row in self.adv.get_rows(GroupsTitles.ADV_RENAME.value):
            self.assertEqual(self.adv.get_row_title(row), (GroupsTitles.ADV_RENAME.value))
        # Set to Pass
        self.__class__.test_result = 'pass'
