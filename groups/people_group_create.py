from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.groups import GroupsPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from constants.enums import PageTitles, GroupsTitles, Prompts, Attributes
from constants.prompt_selections import PG


class CreatePeopleGroup(IscE2eTestCase):
    """Create a People Group for testing"""

    def setUp(self):
        super(CreatePeopleGroup, self).setUp()
        # Initialize page objects
        self.groups = GroupsPage(self.driver)
        self.select = SelectPromptPage(self.driver)

    def test_a_open_pg_page(self):
        """Navigate to PG Page"""
        self.groups.nav_link.click()
        self.assertEqual(self.groups.title.text, PageTitles.PEOPLE_GROUPS.value)

    def test_b_create_pg(self):
        """Click to add a new PG"""
        self.groups.create.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.groups.report_title_locator, GroupsTitles.PG_CREATE.value))

    def test_c_store(self):
        """Set store for PG"""
        self.select.folder_input(Prompts.STORE.value, PG.STORE.value, PG.STORE_LEV.value)

    def test_d_product(self):
        """Set product for PG"""
        self.select.search_hierarchy(Prompts.PRODUCT.value, PG.PRODUCT.value, PG.PROD_LEV.value)

    def test_e_category(self):
        """Set category for PG"""
        self.select.search_hierarchy_select(
            Prompts.CATEGORY.value, PG.CATEGORY.value, PG.CAT_LEV.value, PG.CAT_SELECT.value)

    def test_f_demographic(self):
        """Set demographic for PG"""
        self.select.folder_input(Prompts.DEMOGRAPHIC.value, PG.AGE.value, PG.AGE_FOLDER.value)

    def test_g_location(self):
        """Set location for PG"""
        self.select.folder_input(Prompts.LOCATION.value, PG.LOCATION.value, PG.GEO_LEV.value)

    def test_h_adv_custom_filter(self):
        """Set custom filter for PG"""
        self.select.advanced_options.click()
        self.select.basic_input(Prompts.ANY.value, PG.CUSTOM_FILTER.value, 1)
        # Validate only numeric characters can be typed into input field
        self.groups.custom_filter_textbox.send_keys('abc')
        self.assertEqual(self.groups.custom_filter_textbox.get_attribute(Attributes.VALUE.value), '')
        self.groups.custom_filter_textbox.send_keys(PG.FILTER_VALUE.value)
        self.assertEqual(self.groups.custom_filter_textbox.get_attribute(Attributes.VALUE.value), PG.FILTER_VALUE.value)
        # Clear prompt to select another one
        self.select.clear_prompt(PG.CUSTOM_FILTER.value + ': Equal to ' + PG.FILTER_VALUE.value).click()

    def test_i_adv_fixed_filter(self):
        """Set fixed filter for PG"""
        self.select.basic_input(Prompts.ANY.value, PG.FIXED_FILTER.value, 0)

    def test_j_name_pg(self):
        """Click next and name PG"""
        self.groups.next_button.click()
        self.assertEqual(self.groups.name_msg.text, GroupsTitles.PG_NAME.value)
        self.select.search_field.send_keys(GroupsTitles.PEOPLE_NAME.value)
        self.groups.next_button.click()

    def test_k_validate_pg(self):
        """Validate PG create"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.groups.row_locator))
        self.groups.search_box.send_keys(GroupsTitles.PEOPLE_NAME.value)
        for row in self.groups.get_rows(GroupsTitles.PEOPLE_NAME.value):
            self.assertEqual(self.groups.get_row_title(row), GroupsTitles.PEOPLE_NAME.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
