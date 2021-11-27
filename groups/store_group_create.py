from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.adv_groups import AdvGroupsPage
from constants.enums import PageTitles, GroupsTitles
from constants.prompt_selections import STGR


class CreateStoreGroup(IscE2eTestCase):
    """Create a store gorup for testing"""

    def setUp(self):
        super(CreateStoreGroup, self).setUp()
        self.adv = AdvGroupsPage(self.driver)

    def test_a_nav_store_groups(self):
        """Navigate to Store Groups Page"""
        self.adv.nav_link.click()
        self.assertEqual(self.adv.title.text, PageTitles.PROD_GROUPS.value)
        self.adv.store_groups.click()
        self.assertEqual(self.adv.title.text, PageTitles.STORE_GROUPS.value)

    def test_b_create_store_group(self):
        """Click to add a new Store Group"""
        self.adv.create.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.adv.report_title_locator, GroupsTitles.STORE_CREATE.value))

    def test_c_store_level(self):
        """Set Product Level 1 for Store Group"""
        self.adv.combo_box.send_keys(STGR.STORE_LEV.value)
        self.adv.get_list_option(STGR.STORE_LEV.value).click()
        self.assertTrue(
            self.adv.get_prompt_block(STGR.STORE_LEV.value.upper()))
        self.adv.combo_box.send_keys(STGR.PROD_LEV_OP_1.value)
        self.adv.get_list_option(STGR.PROD_LEV_OP_1.value).click()
        self.assertTrue(
            self.adv.get_prompt_block(STGR.PROD_LEV_OP_1.value.upper()))

    def test_d_channel_level(self):
        """Set Channel Level 1 for Store Group"""
        self.adv.combo_box.send_keys(STGR.STORE.value)
        self.adv.get_list_option(STGR.STORE.value).click()
        self.assertTrue(self.adv.get_prompt_block(STGR.STORE.value.upper()))
        self.adv.combo_box.send_keys(STGR.STORE_2.value)
        self.adv.get_list_option(STGR.STORE_2.value).click()
        self.assertTrue(self.adv.get_prompt_block(STGR.STORE_2.value.upper()))
        self.adv.combo_box.send_keys(STGR.CLOSE.value)
        self.assertEqual(self.adv.closed_condition[1].text, STGR.CLOSED.value)

    def test_e_name_store_group(self):
        self.adv.next_button.click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.adv.modal_title_locator))
        self.adv.modal_folder_input.send_keys(GroupsTitles.STG_FOLDER.value)
        self.adv.modal_pg_input.send_keys(GroupsTitles.STG_NAME.value)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.adv.modal_save_locator))
        self.adv.modal_save_btn.click()

    def test_f_validate_store_group(self):
        """Validate Store Group create"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.adv.title_locator))
        self.adv.search_box.send_keys(GroupsTitles.STG_FOLDER.value)
        for row in self.adv.get_rows(GroupsTitles.STG_FOLDER.value):
            self.assertEqual(
                self.adv.get_row_title(row), GroupsTitles.STG_FOLDER.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
