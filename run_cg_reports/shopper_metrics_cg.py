from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.shopper import ShopperPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import SM


class RunShopperMetricsCG(IscE2eTestCase):
    """Run a Shopper Metrics Report with Custom Groups"""

    def setUp(self):
        "Set Up"
        super(RunShopperMetricsCG, self).setUp()
        # Initialize Page Objects
        self.shopper = ShopperPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_shopper_metrics(self):
        """Navigate to Shopper Metrics"""
        self.shopper.nav_link.click()
        self.shopper.shopper_metrics.click()
        self.assertEqual(self.select.title.text, ReportTypes.SHOPPER_METRICS.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, SM.CG_PROD.value, SM.CG_PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, SM.CG_CAT.value, SM.CG_CAT_LEV.value)

    def test_d_level(self):
        self.select.folder_input(Prompts.LEVEL.value, SM.LEV.value, SM.LEV_LEV.value)

    def test_e_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, SM.STORE.value, SM.STORE_LEV.value)

    def test_f_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, SM.DATE.value)

    def test_g_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, SM.PG.value)

    def test_h_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, SM.CHAN.value)

    def test_i_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, SM.LOCATION.value, SM.GEO_LEV.value)

    def test_j_adv_tg(self):
        self.select.search_input(Prompts.TG.value, SM.TG.value)

    def test_k_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, SM.WEIGHT.value)

    def test_l_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, SM.STAT.value)

    def test_m_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.SHOPPER_METRICS.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
