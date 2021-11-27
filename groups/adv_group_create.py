from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.adv_groups import AdvGroupsPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from constants.enums import PageTitles, GroupsTitles
from constants.prompt_selections import ADVG


class CreateAdvGroup(IscE2eTestCase):
    """Create an Advanced Group for testing"""

    def setUp(self):
        super(CreateAdvGroup, self).setUp()
        # Initialize page objects
        self.adv = AdvGroupsPage(self.driver)
        self.select = SelectPromptPage(self.driver)

    def test_a_nav_adv_groups(self):
        """Navigate to Advanced Groups Page"""
        self.adv.nav_link.click()
        self.assertEqual(self.adv.title.text, PageTitles.PROD_GROUPS.value)

    def test_b_create_adv_group(self):
        """Click to add a new Adv Group"""
        self.adv.create.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.adv.report_title_locator, GroupsTitles.AG_CREATE.value))

    def test_c_prod_level(self):
        """Set product level 1 for Adv Group"""
        self.adv.combo_box.send_keys(ADVG.PROD_LEV_1.value)
        self.adv.get_list_option(ADVG.PROD_LEV_1.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVG.PROD_LEV_1.value.upper()))
        self.adv.combo_box.send_keys(ADVG.PROD_LEV_OP_1.value)
        self.adv.get_list_option(ADVG.PROD_LEV_OP_1.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVG.PROD_LEV_OP_1.value.upper()))

    def test_d_maj_cat(self):
        """Set major category for Adv Group"""
        self.adv.combo_box.send_keys(ADVG.MAJOR_CAT.value)
        self.adv.get_list_option(ADVG.MAJOR_CAT.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVG.MAJOR_CAT.value.upper()))
        self.adv.combo_box.send_keys(ADVG.CLOSE.value)
        self.assertEqual(self.adv.closed_condition[1].text, ADVG.CLOSED.value)
        self.adv.combo_box.send_keys(ADVG.CONJ_OP.value)
        self.adv.get_list_option(ADVG.CONJ_OP.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVG.CONJ_OP.value.upper()))

    def test_e_prod_level(self):
        """Set product level 2 for Adv Group"""
        self.adv.combo_box.send_keys(ADVG.PROD_LEV_2.value)
        self.adv.get_list_option(ADVG.PROD_LEV_2.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVG.PROD_LEV_2.value.upper()))
        self.adv.combo_box.send_keys(ADVG.PROD_LEV_OP_2.value)
        self.adv.get_list_option(ADVG.PROD_LEV_OP_2.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVG.PROD_LEV_OP_2.value.upper()))

    def test_f_parent_brand(self):
        """Set parent brand for Adv Group"""
        self.adv.combo_box.send_keys(ADVG.PARENT_BRAND.value)
        self.adv.get_list_option(ADVG.PARENT_BRAND.value).click()
        self.assertTrue(self.adv.get_prompt_block(ADVG.PARENT_BRAND.value.upper()))
        self.adv.combo_box.send_keys(ADVG.CLOSE.value)
        self.assertEqual(self.adv.closed_condition[3].text, ADVG.CLOSED.value)

    def test_g_name_adv_group(self):
        """Click next and name Adv Group"""
        self.adv.next_button.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.adv.modal_title_locator))
        self.adv.modal_folder_input.send_keys(GroupsTitles.ADV_FOLDER.value)
        self.adv.modal_pg_input.send_keys(GroupsTitles.ADV_NAME.value)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.adv.modal_save_locator))
        self.adv.modal_save_btn.click()

    def test_h_validate_adv_group(self):
        """Validate Adv Group create"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.adv.title_locator))
        self.adv.search_box.send_keys(GroupsTitles.ADV_FOLDER.value)
        for row in self.adv.get_rows(GroupsTitles.ADV_FOLDER.value):
            self.assertEqual(self.adv.get_row_title(row), GroupsTitles.ADV_FOLDER.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
