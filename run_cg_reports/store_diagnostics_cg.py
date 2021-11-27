from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.shopper import ShopperPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import SD


class RunStoreDiagnosticsCG(IscE2eTestCase):
    """Run a Store Diagnostics Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunStoreDiagnosticsCG, self).setUp()
        # Initialize Page Objects
        self.shopper = ShopperPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_store_diag(self):
        """Navigate to Store Diagnostics"""
        self.shopper.nav_link.click()
        self.shopper.store_diagnostics.click()
        self.assertEqual(self.select.title.text, ReportTypes.STORE_DIAGNOSTICS.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, SD.CG_PROD.value, SD.CG_PROD_LEV.value)

    def test_c_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, SD.STORE.value, SD.STORE_LEV.value)

    def test_d_comp_channel(self):
        self.select.folder_input(Prompts.COMP_CHANNEL.value, SD.CHAN.value, SD.CHAN_LEV.value)

    def test_e_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, SD.PG.value)

    def test_f_adv_date_range(self):
        self.select.clear_prompt(PromptElements.LATEST_12_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, SD.DATE.value)

    def test_g_adv_period(self):
        self.select.clear_prompt(PromptElements.YEAR_AGO.value).click()
        self.select.basic_input(Prompts.NONE.value, SD.PERIOD.value)

    def test_h_adv_store_level(self):
        self.select.basic_input(Prompts.SAME_STORE_LEVEL.value, SD.STORE_LEVEL.value)

    def test_i_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, SD.LOCATION.value, SD.GEO_LEV.value)

    def test_j_adv_tg(self):
        self.select.search_input(Prompts.TG.value, SD.TG.value)

    def test_k_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, SD.WEIGHT.value)

    def test_l_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, SD.STAT.value)

    def test_m_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.STORE_DIAGNOSTICS.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
