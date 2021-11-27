from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.shopper import ShopperPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import LRN


class RunLapsedRepeatNewCG(IscE2eTestCase):
    """Run a Lapsed, Repeat, New Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunLapsedRepeatNewCG, self).setUp()
        # Initialize Page Objects
        self.shopper = ShopperPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_lapsed_repeat_new(self):
        """Navigate to Lapsed, Repeat, New"""
        self.shopper.nav_link.click()
        self.shopper.lapsed_repeat_new.click()
        self.assertEqual(self.select.title.text, ReportTypes.LAPSED_REPEAT_NEW.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, LRN.CG_PROD.value, LRN.CG_PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, LRN.CG_CAT.value, LRN.CG_CAT_LEV.value)

    def test_d_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, LRN.STORE.value, LRN.STORE_LEV.value)

    def test_e_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, LRN.DATE.value)

    def test_f_adv_period(self):
        self.select.advanced_options.click()
        self.select.clear_prompt(PromptElements.YEAR_AGO.value).click()
        self.select.basic_input(Prompts.NONE.value, LRN.PERIOD.value)

    def test_g_adv_product_level(self):
        self.select.search_input(Prompts.SAME_PRODUCT_LEVEL.value, LRN.PROD_LEVEL.value)

    def test_h_adv_store_level(self):
        self.select.basic_input(Prompts.SAME_STORE.value, LRN.STORE_LEVEL.value)

    def test_i_adv_pg(self):
        self.select.search_input(Prompts.PG.value, LRN.PG.value)

    def test_j_adv_channel(self):
        self.select.clear_prompt(PromptElements.FMCG.value).click()
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, LRN.CHAN.value, LRN.CHAN_LEV.value)

    def test_k_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, LRN.LOCATION.value, LRN.GEO_LEV.value)

    def test_l_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, LRN.WEIGHT.value)

    def test_m_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, LRN.STAT.value)

    def test_n_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.LAPSED_REPEAT_NEW.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
