from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.promo import PromoPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts
from constants.prompt_selections import RCA


class RunRetailerCircularAnalysis(IscE2eTestCase):
    """Run a Retailer Circular Analysis Report"""

    def setUp(self):
        """Set Up"""
        super(RunRetailerCircularAnalysis, self).setUp()
        # Initialize Page Objects
        self.promo = PromoPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_retailer_circular_analysis(self):
        """Navigate to Retailer Circular Analysis"""
        self.promo.nav_link.click()
        self.promo.retailer_circular_analysis.click()
        self.assertEqual(self.select.title.text, ReportTypes.RETAILER_CIRCULAR_ANALYSIS.value)

    def test_b_banner(self):
        self.select.search_input(Prompts.BANNER.value, RCA.BANNER.value)

    def test_c_comp_banner(self):
        self.select.search_input(Prompts.COMP_BANNER.value, RCA.COMP_BANNER.value)

    def test_d_date_range(self):
        self.select.promo_dates(Prompts.DATE_RANGE.value, RCA.START.value, RCA.END.value)

    def test_e_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, RCA.PG.value)

    def test_f_adv_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, RCA.CAT.value, RCA.CAT_LEV.value, RCA.CAT_SEL.value)

    def test_g_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.RETAILER_CIRCULAR_ANALYSIS.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
