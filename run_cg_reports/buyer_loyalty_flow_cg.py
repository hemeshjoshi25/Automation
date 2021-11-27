from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.brand import BrandPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import BLF


class RunBuyerLoyaltyFlowCG(IscE2eTestCase):
    """Run a Buyer Loyalty Flow Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunBuyerLoyaltyFlowCG, self).setUp()
        # Initialize Page Objects
        self.brand = BrandPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_buyer_loyalty_flow(self):
        """Navigate to Buyer Loyalty Flow"""
        self.brand.nav_link.click()
        self.brand.buyer_loyalty_flow.click()
        self.assertEqual(self.select.title.text, ReportTypes.BUYER_LOYALTY_FLOW.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, BLF.CG_PROD.value, BLF.CG_PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, BLF.CG_CAT.value, BLF.CG_CAT_LEV.value)

    def test_d_adv_date_range(self):
        self.select.advanced_options.click()
        self.select.clear_prompt(PromptElements.LATEST_12_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, BLF.DATE.value)

    def test_e_adv_period(self):
        self.select.clear_prompt(PromptElements.YEAR_AGO.value).click()
        self.select.basic_input(Prompts.NONE.value, BLF.PERIOD.value)

    def test_f_adv_pg(self):
        self.select.search_input(Prompts.PG.value, BLF.PG.value)

    def test_g_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, BLF.STORE.value, BLF.STORE_LEV.value)

    def test_h_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, BLF.CHAN.value)

    def test_i_adv_product_level(self):
        self.select.search_input(Prompts.PRODUCT_LEVEL.value, BLF.PROD_LEVEL.value)

    def test_j_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, BLF.LOCATION.value, BLF.GEO_LEV.value)

    def test_k_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, BLF.WEIGHT.value)

    def test_l_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, BLF.STAT.value)

    def test_m_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.BUYER_LOYALTY_FLOW.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
