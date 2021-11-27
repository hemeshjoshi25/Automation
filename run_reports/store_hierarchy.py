from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.tools import ToolsPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts
from constants.prompt_selections import STH


class RunStoreHierarchy(IscE2eTestCase):
    """Run a Store Hierarchy Report"""

    def setUp(self):
        """Set Up"""
        super(RunStoreHierarchy, self).setUp()
        # Initialize Page Objects
        self.tools = ToolsPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_store_hierarchy(self):
        """Navigate to Store Hierarchy"""
        self.tools.nav_link.click()
        self.tools.store_hierarchy.click()
        self.assertEqual(self.select.title.text, ReportTypes.STORE_HIERARCHY.value)

    def test_b_store(self):
        self.select.search_hierarchy(Prompts.STORES.value, STH.STORE.value, STH.STORE_LEV.value)

    def test_c_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.STORE_HIERARCHY.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
