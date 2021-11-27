from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.shopper import ShopperPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import RSOW


class RunRetailerShareWalletCG(IscE2eTestCase):
    """Run a Retailer Share of Wallet Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunRetailerShareWalletCG, self).setUp()
        # Initialize Page Objects
        self.shopper = ShopperPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_rsow(self):
        """Navigate to Retailer Share of Wallet"""
        self.shopper.nav_link.click()
        self.shopper.retailer_share_wallet.click()
        self.assertEqual(self.select.title.text, ReportTypes.RETAILER_SHARE_WALLET.value)

    def test_b_product_level(self):
        PROD_LEVS = [RSOW.PROD_LEV_1.value, RSOW.PROD_LEV_2.value]
        self.select.product_levels(Prompts.PRODUCT_LEVEL.value, PROD_LEVS)
        if None not in PROD_LEVS:
            self.assertEqual(self.select.alert_text.text, PromptElements.MAX_2.value)

    def test_c_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, RSOW.CG_CAT.value, RSOW.CG_CAT_LEV.value)

    def test_d_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, RSOW.STORE.value, RSOW.STORE_LEV.value)

    def test_e_date_range(self):
        self.select.clear_prompt(PromptElements.LATEST_12_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, RSOW.DATE.value)

    def test_f_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, RSOW.PG.value)

    def test_g_adv_prior_period(self):
        self.select.clear_prompt(PromptElements.YEAR_AGO.value).click()
        self.select.basic_input(Prompts.NONE.value, RSOW.PRIOR.value)

    def test_h_adv_channel(self):
        self.select.clear_prompt(PromptElements.FMCG.value).click()
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, RSOW.CHAN.value, RSOW.CHAN_LEV.value)

    def test_i_adv_store_level(self):
        self.select.basic_input(Prompts.SAME_STORE_LEVEL.value, RSOW.STORE_LEVEL.value)

    def test_j_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, RSOW.LOCATION.value, RSOW.GEO_LEV.value)

    def test_k_adv_tg(self):
        self.select.search_input(Prompts.TG.value, RSOW.TG.value)

    def test_l_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, RSOW.WEIGHT.value)

    def test_m_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, RSOW.STAT.value)

    def test_n_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.RETAILER_SHARE_WALLET.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
