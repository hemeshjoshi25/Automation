from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.adv_groups import AdvGroupsPage
from constants.enums import PageTitles, GroupsTitles
from constants.prompt_selections import STGRADD


class AddStoreGroup(IscE2eTestCase):
    def setUp(self):
        super(AddStoreGroup, self).setUp()
        self.adv = AdvGroupsPage(self.driver)

    def test_a_nav_store_groups(self):
        """Navigate to Store Groups Page"""
        self.adv.nav_link.click()
        self.assertEqual(self.adv.title.text, PageTitles.PROD_GROUPS.value)
        self.adv.store_groups.click()
        self.assertEqual(self.adv.title.text, PageTitles.STORE_GROUPS.value)

    def test_b_add_store_group(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.send_keys(GroupsTitles.STG_FOLDER.value)
        self.adv.get_row_options(GroupsTitles.STG_FOLDER.value).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.adv.row_options_locator))
        self.adv.option_add.click()
        self.assertEqual(self.adv.report_header.text,
                         GroupsTitles.STORE_CREATE.value)

    def test_c_store_level(self):
        """Set Product Level 1 for Store Group"""
        self.adv.combo_box.send_keys(STGRADD.STORE_LEV.value)
        self.adv.get_list_option(STGRADD.STORE_LEV.value).click()
        self.assertTrue(
            self.adv.get_prompt_block(STGRADD.STORE_LEV.value.upper()))
        self.adv.combo_box.send_keys(STGRADD.PROD_LEV_OP_1.value)
        self.adv.get_list_option(STGRADD.PROD_LEV_OP_1.value).click()
        self.assertTrue(
            self.adv.get_prompt_block(STGRADD.PROD_LEV_OP_1.value.upper()))

    def test_d_channel_level(self):
        """Set Channel Level 1 for Store Group"""
        self.adv.combo_box.send_keys(STGRADD.STORE.value)
        self.adv.get_list_option(STGRADD.STORE.value).click()
        self.assertTrue(self.adv.get_prompt_block(STGRADD.STORE.value.upper()))
        self.adv.combo_box.send_keys(STGRADD.STORE_2.value)
        self.adv.get_list_option(STGRADD.STORE_2.value).click()
        self.assertTrue(
            self.adv.get_prompt_block(STGRADD.STORE_2.value.upper()))
        self.adv.combo_box.send_keys(STGRADD.CLOSE.value)
        self.assertEqual(self.adv.closed_condition[1].text,
                         STGRADD.CLOSED.value)

    def test_e_name_store_group(self):
        """Adding store group"""
        self.adv.next_button.click()
        self.assertEqual(self.adv.modal_title.text,
                         GroupsTitles.SG_NAME.value.upper())
        self.adv.modal_pg_input.send_keys(GroupsTitles.STG_ADD.value)
        self.adv.modal_save_btn.click()

    def test_f_validate_store_group(self):
        """Validate Store Group create"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.adv.title_locator))
        self.adv.search_box.send_keys(GroupsTitles.STG_FOLDER.value)
        self.adv.get_row(GroupsTitles.STG_FOLDER.value).click()
        self.driver.refresh()
        self.assertEqual(self.adv.folder_title.text,
                         GroupsTitles.STG_FOLDER.value)
        self.assertTrue(self.adv.get_pg_row(GroupsTitles.STG_ADD.value))
        self.assertTrue(self.adv.get_pg_row(GroupsTitles.STG_NAME.value))
        # Set to Pass
        self.__class__.test_result = 'pass'
