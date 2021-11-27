from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.tools import ToolsPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts
from constants.prompt_selections import PH


class RunProductHierarchy(IscE2eTestCase):
    """Run a Product Hierarchy Report"""

    def setUp(self):
        """Set Up"""
        super(RunProductHierarchy, self).setUp()
        # Initialize Page Objects
        self.tools = ToolsPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_product_hierarchy(self):
        """Navigate to Product Hierarchy"""
        self.tools.nav_link.click()
        self.tools.product_hierarchy.click()
        self.assertEqual(self.select.title.text, ReportTypes.PRODUCT_HIERARCHY.value)

    def test_b_product(self):
        self.select.search_hierarchy_select(Prompts.PRODUCTS.value, PH.PROD.value, PH.PROD_LEV.value, PH.PROD_SEL.value)

    def test_c_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.PRODUCT_HIERARCHY.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
