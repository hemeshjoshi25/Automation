from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.adv_groups import AdvGroupsPage
from constants.enums import PageTitles, GroupsTitles


class RenameStoreGroup(IscE2eTestCase):

    def setUp(self):
        super(RenameStoreGroup, self).setUp()
        self.adv = AdvGroupsPage(self.driver)

    def test_a_nav_store_groups(self):
        """Navigate to Store Groups Page"""
        self.adv.nav_link.click()
        self.assertEqual(self.adv.title.text, PageTitles.PROD_GROUPS.value)
        self.adv.store_groups.click()
        self.assertEqual(self.adv.title.text, PageTitles.STORE_GROUPS.value)

    def test_b_rename_store_group(self):
        """Rename test Adv Group Folder(s)"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.send_keys(GroupsTitles.STG_FOLDER.value)
        for _ in self.adv.get_rows(GroupsTitles.STG_FOLDER.value):
            self.adv.get_row_options(GroupsTitles.STG_FOLDER.value).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(
                    self.adv.row_options_locator))
            self.adv.option_rename.click()
            self.adv.modal_input.send_keys(GroupsTitles.STG_RENAME.value)
            self.adv.rename_save_btn.click()

    def test_c_validate_rename(self):
        """Validate Adv Group Folder rename"""
        sleep(1)  # Wait for modal close animation
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.send_keys(GroupsTitles.STG_RENAME.value)
        for row in self.adv.get_rows(GroupsTitles.STG_RENAME.value):
            self.assertEqual(self.adv.get_row_title(row),
                             (GroupsTitles.STG_RENAME.value))
        # Set to Pass
        self.__class__.test_result = 'pass'
