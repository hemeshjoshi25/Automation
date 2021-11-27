from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.adv_groups import AdvGroupsPage
from constants.enums import PageTitles, GroupsTitles


class DeleteAdvGroup(IscE2eTestCase):
    """Delete test Advanced Group"""

    def setUp(self):
        super(DeleteAdvGroup, self).setUp()
        # Initialize Advanced Groups page object
        self.adv = AdvGroupsPage(self.driver)

    def test_a_nav_adv_groups(self):
        """Navigate to Adv Groups Page"""
        self.adv.nav_link.click()
        self.assertEqual(self.adv.title.text, PageTitles.PROD_GROUPS.value)

    def test_b_delete_adv_group(self):
        """Delete test Advanced Group Folder(s)"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.send_keys(GroupsTitles.ADV_RENAME.value)
        for r, row in enumerate(self.adv.get_rows(GroupsTitles.ADV_RENAME.value)):
            if r != 0:
                WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.adv.row_locator))
                self.adv.search_box.send_keys(GroupsTitles.ADV_RENAME)
            self.adv.get_row_options(GroupsTitles.ADV_RENAME.value).click()
            WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.adv.row_options_locator))
            self.adv.option_delete.click()
            sleep(1)  # Wait for modal open animation
            self.adv.confirm_delete.click()
            sleep(1)  # Wait for modal close animation

    def test_c_validate(self):
        """Validate Adv Group Delete"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.click()
        self.adv.search_box.send_keys(GroupsTitles.ADV_RENAME.value)
        self.assertTrue(self.adv.empty_search_message)
        # Set to Pass
        self.__class__.test_result = 'pass'
