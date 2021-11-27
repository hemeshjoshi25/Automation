from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.adv_groups import AdvGroupsPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from constants.enums import PageTitles, GroupsTitles
from constants.prompt_selections import ADVADD


class AddAdvGroup(IscE2eTestCase):
    """Add an Advanced Group for testing"""

    def setUp(self):
        super(AddAdvGroup, self).setUp()
        # Initialize page objects
        self.adv = AdvGroupsPage(self.driver)
        self.select = SelectPromptPage(self.driver)

    def test_a_nav_adv_groups(self):
        """Navigate to Advanced Groups Page"""
        self.adv.nav_link.click()
        self.assertEqual(self.adv.title.text, PageTitles.PROD_GROUPS.value)

    def test_b_add_adv_group(self):
        """Click to add an Adv Group"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.adv.row_locator))
        self.adv.search_box.send_keys(GroupsTitles.ADV_FOLDER.value)
        self.adv.get_row_options(GroupsTitles.ADV_FOLDER.value).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.adv.row_options_locator))
        self.adv.option_add.click()
        self.assertEqual(self.adv.report_header.text, GroupsTitles.AG_CREATE.value)

    def test_c_prod_level(self):
        """Set product level 1 for Adv Group"""
        self.adv.combo_box.send_keys(ADVADD.PROD_LEV_1.value)
        self.adv.get_list_option(ADVADD.PROD_LEV_1.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVADD.PROD_LEV_1.value.upper()))
        self.adv.combo_box.send_keys(ADVADD.PROD_LEV_OP_1.value)
        self.adv.get_list_option(ADVADD.PROD_LEV_OP_1.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVADD.PROD_LEV_OP_1.value))

    def test_d_maj_cat(self):
        """Set major category for Adv Group"""
        self.adv.combo_box.send_keys(ADVADD.MAJOR_CAT.value)
        self.adv.get_list_option(ADVADD.MAJOR_CAT.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVADD.MAJOR_CAT.value.upper()))
        self.adv.combo_box.send_keys(ADVADD.CLOSE.value)
        self.assertEqual(self.adv.closed_condition[1].text, ADVADD.CLOSED.value)
        self.adv.combo_box.send_keys(ADVADD.CONJ_OP.value)
        self.adv.get_list_option(ADVADD.CONJ_OP.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVADD.CONJ_OP.value))

    def test_e_prod_level(self):
        """Set product level 2 for Adv Group"""
        self.adv.combo_box.send_keys(ADVADD.PROD_LEV_2.value)
        self.adv.get_list_option(ADVADD.PROD_LEV_2.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVADD.PROD_LEV_2.value.upper()))
        self.adv.combo_box.send_keys(ADVADD.PROD_LEV_OP_2.value)
        self.adv.get_list_option(ADVADD.PROD_LEV_OP_2.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVADD.PROD_LEV_OP_2.value))

    def test_f_parent_brand(self):
        """Set parent brand for Adv Group"""
        self.adv.combo_box.send_keys(ADVADD.PARENT_BRAND.value)
        self.adv.get_list_option(ADVADD.PARENT_BRAND.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVADD.PARENT_BRAND.value.upper()))
        self.adv.combo_box.send_keys(ADVADD.CLOSE.value)
        self.assertEqual(self.adv.closed_condition[3].text, ADVADD.CLOSED.value)

    def test_g_name_adv_group(self):
        """Click next and name Adv Group"""
        self.adv.next_button.click()
        self.assertEqual(self.adv.modal_title.text, GroupsTitles.AG_NAME.value.upper())
        self.adv.modal_pg_input.send_keys(GroupsTitles.ADV_ADD.value)
        self.adv.modal_save_btn.click()

    def test_h_validate_adv_group(self):
        """Validate Adv Group add"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.adv.title_locator))
        self.adv.search_box.send_keys(GroupsTitles.ADV_FOLDER.value)
        self.adv.get_row(GroupsTitles. ADV_FOLDER.value).click()
        self.assertEqual(self.adv.folder_title.text, GroupsTitles. ADV_FOLDER.value)
        self.assertTrue(self.adv.get_pg_row(GroupsTitles.ADV_ADD.value))
        self.assertTrue(self.adv.get_pg_row(GroupsTitles.ADV_NAME.value))
        # Set to Pass
        self.__class__.test_result = 'pass'
