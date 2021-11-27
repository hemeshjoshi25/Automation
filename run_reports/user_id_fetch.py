from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.labs import LabsPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import UIDF


class RunUserIDFetch(IscE2eTestCase):
    """Run a User ID Fetch Report"""

    def setUp(self):
        """Set Up"""
        super(RunUserIDFetch, self).setUp()
        # Initialize Page Objects
        self.labs = LabsPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_user_id_fetch(self):
        """Navigate to User ID Fetch"""
        self.labs.nav_link.click()
        self.labs.user_id_fetch.click()
        self.assertEqual(self.select.title.text, ReportTypes.USER_ID_FETCH.value)

    def test_b_pg(self):
        self.select.search_input(Prompts.PG.value, UIDF.PG.value)

    def test_c_adv_date_range(self):
        self.select.advanced_options.click()
        self.select.clear_prompt(PromptElements.LATEST_52_WEEKS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, UIDF.DATE.value)

    def test_d_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, UIDF.STAT.value)

    def test_e_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.USER_ID_FETCH.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
