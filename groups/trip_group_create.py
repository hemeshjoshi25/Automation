from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.groups import GroupsPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.prompts.prompt import GenericPromptPage
from constants.enums import PageTitles, GroupsTitles, Prompts
from constants.prompt_selections import TG


class CreateTripGroup(IscE2eTestCase):
    """Create a Trip Group for testing"""

    def setUp(self):
        super(CreateTripGroup, self).setUp()
        # Initialize page objects
        self.groups = GroupsPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.prompt = GenericPromptPage(self.driver)

    def test_a_open_tg_page(self):
        """Navigate to TG Page"""
        self.groups.nav_link.click()
        self.assertEqual(self.groups.title.text, PageTitles.PEOPLE_GROUPS.value)
        self.groups.trip_groups.click()
        self.assertEqual(self.groups.title.text, PageTitles.TRIP_GROUPS.value)

    def test_b_create_tg(self):
        """Click to add a new TG"""
        self.groups.create.click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.groups.report_title_locator, GroupsTitles.TG_CREATE.value))

    def test_c_adult_gender(self):
        """Set adult gender for TG"""
        self.select.folder_input(Prompts.ADULT_GENDERS.value, TG.GENDER.value, TG.GENDER_FOLDER.value)

    def test_d_children(self):
        """Set children for TG"""
        self.select.folder_input(Prompts.CHILDREN.value, TG.KIDS.value, TG.KID_FOLDER.value)

    def test_e_trip_attribute(self):
        """Set trip attribute for TG"""
        self.prompt.get_prompt(Prompts.TRIP_ATTR.value).click()
        self.prompt.validate_prompt(Prompts.TRIP_ATTR.value)

    def test_f_day_or_time(self):
        """Set day/time for TG"""
        self.select.folder_input(Prompts.DAY_OR_TIME.value, TG.DAY.value, TG.DAY_FOLDER.value)

    def test_g_name_tg(self):
        """Click next and name PG"""
        self.groups.next_button.click()
        self.assertEqual(self.groups.name_msg.text, GroupsTitles.TG_NAME.value)
        self.prompt.search_field.send_keys(GroupsTitles.TRIP_NAME.value)
        self.groups.next_button.click()

    def test_h_validate_tg(self):
        """Validate TG create"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.groups.row_locator))
        self.groups.search_box.send_keys(GroupsTitles.TRIP_NAME.value)
        rows = self.groups.get_rows(GroupsTitles.TRIP_NAME.value)
        for row in rows:
            self.assertEqual(self.groups.get_row_title(row), GroupsTitles.TRIP_NAME.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
