from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.people import PeoplePage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import PSY


class RunPsychographics(IscE2eTestCase):
    """Run a Psychographics Report"""

    def setUp(self):
        """Set Up"""
        super(RunPsychographics, self).setUp()
        # Initialize Page Objects
        self.people = PeoplePage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_psychographics(self):
        """Navigate to Psychographics"""
        self.people.nav_link.click()
        self.people.psychographics.click()
        self.assertEqual(self.select.title.text, ReportTypes.PSYCHOGRAPHICS.value)

    def test_b_people_group(self):
        self.select.search_input(Prompts.PG.value, PSY.PG.value)

    def test_c_comp_people_group(self):
        self.select.search_input(Prompts.SHOPPERS.value, PSY.COMP_PG.value)

    def test_d_date_range(self):
        self.select.clear_prompt(PromptElements.LATEST_12_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, PSY.DATE.value)

    def test_e_adv_geography(self):
        self.select.advanced_options.click()
        self.select.folder_input(Prompts.LOCATION.value, PSY.LOCATION.value, PSY.GEO_LEV.value)

    def test_f_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, PSY.STAT.value)

    def test_g_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.PSYCHOGRAPHICS.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
