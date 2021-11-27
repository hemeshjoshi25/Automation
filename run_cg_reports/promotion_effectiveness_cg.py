from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.shopper import ShopperPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import PE


class RunPromotionEffectivenessCG(IscE2eTestCase):
    """Run a Promotion Effectiveness Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunPromotionEffectivenessCG, self).setUp()
        # Initialize Page Objects
        self.shopper = ShopperPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_promo_effect(self):
        """Navigate to Promotion Effectiveness"""
        self.shopper.nav_link.click()
        self.shopper.promotion_effectiveness.click()
        self.assertEqual(self.select.title.text, ReportTypes.PROMOTION_EFFECTIVENESS.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, PE.CG_PROD.value, PE.CG_PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, PE.CG_CAT.value, PE.CG_CAT_LEV.value)

    def test_d_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, PE.STORE.value, PE.STORE_LEV.value)

    def test_e_promo_dates(self):
        self.select.promo_dates(Prompts.PROMO_DATES.value, PE.START.value, PE.END.value)

    def test_f_adv_portfolio(self):
        self.select.advanced_options.click()
        self.select.search_hierarchy(Prompts.PORTFOLIO.value, PE.PORT.value, PE.PORT_LEV.value)

    def test_g_adv_pre_period(self):
        self.select.clear_prompt(PromptElements.WEEKS_26.value).click()
        self.select.basic_input(Prompts.NUM_WEEKS.value, PE.PRE.value)

    def test_h_adv_post_period(self):
        self.select.clear_prompt(PromptElements.WEEKS_13.value).click()
        self.select.basic_input(Prompts.NUM_WEEKS.value, PE.POST.value)

    def test_i_adv_pg(self):
        self.select.search_input(Prompts.PG.value, PE.PG.value)

    def test_j_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, PE.LOCATION.value, PE.GEO_LEV.value)

    def test_k_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, PE.CHAN.value)

    def test_l_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, PE.WEIGHT.value)

    def test_m_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, PE.STAT.value)

    def test_n_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.PROMOTION_EFFECTIVENESS.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
