from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.brand import BrandPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import BS


class RunBrandSwitchingCG(IscE2eTestCase):
    """Run a Brand Switching Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunBrandSwitchingCG, self).setUp()
        # Initialize Page Objects
        self.brand = BrandPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_brand_switch(self):
        """Navigate to Brand Switching"""
        self.brand.nav_link.click()
        self.brand.brand_switching.click()
        self.assertEqual(self.select.title.text, ReportTypes.BRAND_SWITCHING.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, BS.CG_PROD.value, BS.CG_PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, BS.CG_CAT.value, BS.CG_CAT_LEV.value)

    def test_d_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, BS.DATE.value)

    def test_e_adv_product_level(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.SAME_PRODUCT_LEVEL_LOWER.value, BS.PROD_LEVEL.value)

    def test_f_adv_portfolio(self):
        self.select.search_hierarchy(Prompts.PORTFOLIO.value, BS.PORT.value, BS.PORT_LEV.value)

    def test_g_adv_pg(self):
        self.select.search_input(Prompts.PG.value, BS.PG.value)

    def test_h_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, BS.STORE.value, BS.STORE_LEV.value)

    def test_i_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, BS.CHAN.value)

    def test_j_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, BS.LOCATION.value, BS.GEO_LEV.value)

    def test_k_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, BS.WEIGHT.value)

    def test_l_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, BS.STAT.value)

    def test_m_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.BRAND_SWITCHING.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
