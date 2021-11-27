from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.brand import BrandPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import BD


class RunBrandDiagnostics(IscE2eTestCase):
    """Run a Brand Diagnostics Report"""

    def setUp(self):
        """Set Up"""
        super(RunBrandDiagnostics, self).setUp()
        # Initialize Page Objects
        self.brand = BrandPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_brand_diag(self):
        """Navigate to Brand Diagnostics"""
        self.brand.nav_link.click()
        self.brand.brand_diagnostics.click()
        self.assertEqual(self.select.title.text, ReportTypes.BRAND_DIAGNOSTICS.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, BD.PROD.value, BD.PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, BD.CAT.value, BD.CAT_LEV.value, BD.CAT_SEL.value)

    def test_d_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, BD.DATE.value)

    def test_e_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, BD.PG.value)

    def test_f_adv_product_level(self):
        self.select.search_input(Prompts.PRODUCT_LEVEL.value, BD.PROD_LEVEL.value)

    def test_g_adv_period(self):
        self.select.clear_prompt(PromptElements.YEAR_AGO.value).click()
        self.select.basic_input(Prompts.NONE.value, BD.PERIOD.value)

    def test_h_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, BD.STORE.value, BD.STORE_LEV.value)

    def test_i_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, BD.CHAN.value)

    def test_j_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, BD.LOCATION.value, BD.GEO_LEV.value)

    def test_k_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, BD.WEIGHT.value)

    def test_l_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, BD.STAT.value)

    def test_m_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.BRAND_DIAGNOSTICS.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
