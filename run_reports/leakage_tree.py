from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.shopper import ShopperPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import LT


class RunLeakageTree(IscE2eTestCase):
    """Run a Leakage Tree Report"""

    def setUp(self):
        """Set Up"""
        super(RunLeakageTree, self).setUp()
        # Initialize Page Objects
        self.shopper = ShopperPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_leakage_tree(self):
        """Navigate to Leakage Tree"""
        self.shopper.nav_link.click()
        self.shopper.leakage_tree.click()
        self.assertEqual(self.select.title.text, ReportTypes.LEAKAGE_TREE.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, LT.PROD.value, LT.PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, LT.CAT.value, LT.CAT_LEV.value, LT.CAT_SEL.value)

    def test_d_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, LT.STORE.value, LT.STORE_LEV.value)

    def test_e_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, LT.DATE.value)

    def test_f_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, LT.PG.value)

    def test_g_adv_store_level(self):
        self.select.basic_input(Prompts.SAME_STORE_LEVEL.value, LT.STORE_LEVEL.value)

    def test_h_adv_benchmark(self):
        self.select.clear_prompt(PromptElements.TOP_STORES.value).click()
        self.select.basic_input(Prompts.NONE_SELECT.value, LT.BENCHMARK.value)

    def test_i_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, LT.LOCATION.value, LT.GEO_LEV.value)

    def test_j_adv_channel(self):
        self.select.clear_prompt(PromptElements.FMCG.value).click()
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, LT.CHAN.value, LT.CHAN_LEV.value)

    def test_k_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, LT.WEIGHT.value)

    def test_l_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, LT.STAT.value)

    def test_m_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.LEAKAGE_TREE.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
