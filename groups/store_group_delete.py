from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.adv_groups import AdvGroupsPage
from constants.enums import PageTitles, GroupsTitles


class DeleteStoreGroup(IscE2eTestCase):

    def setUp(self):
        super(DeleteStoreGroup, self).setUp()
        self.adv = AdvGroupsPage(self.driver)

    def test_a_nav_store_groups(self):
        """Navigate to Store Groups Page"""
        self.adv.nav_link.click()
        self.assertEqual(self.adv.title.text, PageTitles.PROD_GROUPS.value)
        self.adv.store_groups.click()
        self.assertEqual(self.adv.title.text, PageTitles.STORE_GROUPS.value)

    def test_b_delete_store_group(self):
        """Delete test Advanced Group Folder(s)"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.send_keys(GroupsTitles.STG_RENAME.value)
        for _ in self.adv.get_rows(GroupsTitles.STG_RENAME.value):
            self.adv.get_row_options(GroupsTitles.STG_RENAME.value).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(
                    self.adv.row_options_locator))
            self.adv.option_delete.click()
            sleep(1)  # Wait for modal open animation
            self.adv.confirm_delete.click()

    def test_c_validate(self):
        sleep(1)  # Wati for modal close animation
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.send_keys(GroupsTitles.STG_RENAME.value)
        self.assertTrue(self.adv.empty_search_message)
        # Set to Pass
        self.__class__.test_result = 'pass'
