from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.people import PeoplePage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import MC


class RunMediaConsumption(IscE2eTestCase):
    """Run a Media Consumption Report"""

    def setUp(self):
        """Set Up"""
        super(RunMediaConsumption, self).setUp()
        # Initialize Page Objects
        self.people = PeoplePage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_media_cons(self):
        """Navigate to Media Consumption"""
        self.people.nav_link.click()
        self.people.media_consumption.click()
        self.assertEqual(self.select.title.text, ReportTypes.MEDIA_CONSUMPTION.value)

    def test_b_people_group(self):
        self.select.search_input(Prompts.PG.value, MC.PG.value)

    def test_c_comp_people_group(self):
        self.select.search_input(Prompts.SHOPPERS.value, MC.COMP_PG.value)

    def test_d_date_range(self):
        self.select.clear_prompt(PromptElements.LATEST_12_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, MC.DATE.value)

    def test_e_adv_geography(self):
        self.select.advanced_options.click()
        self.select.folder_input(Prompts.LOCATION.value, MC.LOCATION.value, MC.GEO_LEV.value)

    def test_f_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, MC.STAT.value)

    def test_g_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.MEDIA_CONSUMPTION.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
