from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.promo import PromoPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts
from constants.prompt_selections import PROS


class RunPromotionScorecard(IscE2eTestCase):
    """Run a Promotion Scorecard Report"""

    def setUp(self):
        """Set Up"""
        super(RunPromotionScorecard, self).setUp()
        # Initialize Page Objects
        self.promo = PromoPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_promo_scorecard(self):
        """Navigate to Promotion Scorecard"""
        self.promo.nav_link.click()
        self.promo.promotion_scorecard.click()
        self.assertEqual(self.select.title.text, ReportTypes.PROMOTION_SCORECARD.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, PROS.PROD.value, PROS.PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, PROS.CAT.value,
                                            PROS.CAT_LEV.value, PROS.CAT_SEL.value)

    def test_d_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, PROS.STORE.value, PROS.STORE_LEV.value)

    def test_e_date_range(self):
        self.select.promo_dates(Prompts.DATE_RANGE.value, PROS.START.value, PROS.END.value)

    def test_f_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.PROMOTION_SCORECARD.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
