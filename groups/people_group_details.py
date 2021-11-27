from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.groups import GroupsPage
from constants.enums import PageTitles, GroupsTitles, PromptElements
from constants.prompt_selections import PG


class PeopleGroupDetails(IscE2eTestCase):
    """Check that the Details Modal works for People Groups"""

    def setUp(self):
        super(PeopleGroupDetails, self).setUp()
        # Initialize Groups page object
        self.groups = GroupsPage(self.driver)

    def test_a_open_pg_page(self):
        """Navigate to PG Page"""
        self.groups.nav_link.click()
        self.assertEqual(self.groups.title.text, PageTitles.PEOPLE_GROUPS.value)

    def test_b_open_details(self):
        """Open details modal for test PG"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.groups.row_locator))
        self.groups.search_box.send_keys(GroupsTitles.PEOPLE_NAME.value)
        self.groups.get_row_options(GroupsTitles.PEOPLE_NAME.value).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.groups.row_options_locator))
        self.groups.option_details.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.groups.details_title_locator))

    def test_c_validate_details(self):
        """Validate details info"""
        DETAIL_PROMPTS = [PromptElements.STORE_CHANNEL.value, PromptElements.PRODUCT.value,
                          PromptElements.CATEGORIES.value, PromptElements.DEMOGRAPHICS.value,
                          PromptElements.GEOGRAPHY.value, PromptElements.FIXED_FILTERS.value]
        DETAIL_ANSWERS = [PG.STORE_LEV.value + ': ' + PG.STORE.value,
                          PG.PROD_LEV.value + ': ' + PG.PRODUCT.value,
                          PG.CAT_LEV.value + ': ' + PG.CATEGORY.value,
                          PG.AGE_FOLDER.value + ': ' + PG.AGE.value,
                          PG.GEO_LEV.value + ': ' + PG.LOCATION.value,
                          PG.FIXED_FILTER.value]
        self.assertEqual(self.groups.details_title.text, GroupsTitles.PEOPLE_NAME.value)
        self.assertEqual(self.groups.details_description.text, GroupsTitles.PG_DETAIL.value)
        self.groups.validate_details_prompts(DETAIL_PROMPTS)
        self.groups.validate_details_answers(DETAIL_ANSWERS)

    def test_d_close_modal(self):
        """Close modal"""
        self.groups.modal_close.click()
        self.assertEqual(self.groups.title.text, PageTitles.PEOPLE_GROUPS.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
