from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.groups import GroupsPage
from constants.enums import PageTitles, GroupsTitles, PromptElements
from constants.prompt_selections import TG


class TripGroupDetails(IscE2eTestCase):
    """Check that the Details Modal works for Trip Groups"""

    def setUp(self):
        super(TripGroupDetails, self).setUp()
        # Initialize Groups page object
        self.groups = GroupsPage(self.driver)

    def test_a_open_tg_page(self):
        """Navigate to TG Page"""
        self.groups.nav_link.click()
        self.assertEqual(self.groups.title.text, PageTitles.PEOPLE_GROUPS.value)
        self.groups.trip_groups.click()
        self.assertEqual(self.groups.title.text, PageTitles.TRIP_GROUPS.value)

    def test_b_open_details(self):
        """Open details modal for test TG"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.groups.row_locator))
        self.groups.search_box.send_keys(GroupsTitles.TRIP_NAME.value)
        self.groups.get_row_options(GroupsTitles.TRIP_NAME.value).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.groups.row_options_locator))
        self.groups.option_details.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.groups.details_title_locator))

    def test_c_validate_details(self):
        """Validate details info"""
        DETAIL_PROMPTS = [PromptElements.ADULT_GENDERS.value, PromptElements.KIDS.value,
                          PromptElements.DAY_TIME.value]
        DETAIL_ANSWERS = [TG.GENDER_FOLDER.value + ': ' + TG.GENDER.value,
                          TG.KID_FOLDER.value + ': ' + TG.KIDS.value,
                          TG.DAY_FOLDER.value + ': ' + TG.DAY.value]
        self.assertEqual(self.groups.details_title.text, GroupsTitles.TRIP_NAME.value)
        self.assertEqual(self.groups.details_description.text, GroupsTitles.TG_DETAIL.value)
        self.groups.validate_details_prompts(DETAIL_PROMPTS)
        self.groups.validate_details_answers(DETAIL_ANSWERS)

    def test_d_close_modal(self):
        """Close modal"""
        self.groups.modal_close.click()
        self.assertEqual(self.groups.title.text, PageTitles.TRIP_GROUPS.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
