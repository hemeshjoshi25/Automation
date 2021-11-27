from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.shopper import ShopperPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import SH


class RunShopperHistogramRV(IscE2eTestCase):
    """Run a Shopper Histogram Report in Retailer View"""

    def setUp(self):
        """Set Up"""
        super(RunShopperHistogramRV, self).setUp()
        # Initialize Page Objects
        self.shopper = ShopperPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_shopper_histogram(self):
        """Navigate to Shopper Histogram"""
        self.shopper.nav_link.click()
        self.shopper.shopper_histogram.click()
        self.assertEqual(self.select.title.text, ReportTypes.SHOPPER_HISTOGRAM.value)

    def test_b_product(self):
        self.select.get_prompt(Prompts.PRODUCT.value).click()
        self.select.validate_prompt(Prompts.PRODUCT.value)

    def test_c_category(self):
        self.select.get_prompt(Prompts.CATEGORY.value).click()
        self.select.validate_prompt(Prompts.CATEGORY.value)

    def test_d_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, SH.DATE.value)

    def test_e_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, SH.PG.value)

    def test_f_adv_bin_controls(self):
        BINS = [SH.BIN_1.value, SH.BIN_2.value, SH.BIN_3.value]
        self.select.bins_input(Prompts.ANY.value, BINS, SH.WIDTH.value, SH.LOWER.value, SH.UPPER.value)

    def test_g_adv_outliers(self):
        self.select.clear_prompt(PromptElements.REMOVE_OUTLIERS.value).click()
        self.select.basic_input(Prompts.NONE.value, SH.OUT.value)

    def test_h_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, SH.STORE.value, SH.STORE_LEV.value)

    def test_i_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, SH.CHAN.value)

    def test_j_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, SH.LOCATION.value, SH.GEO_LEV.value)

    def test_k_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, SH.STAT.value)

    def test_l_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.SHOPPER_HISTOGRAM.value
        rename = ReportTypes.PREFIX_RV.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
