from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.labs import LabsPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import HML


class RunHighMedLow(IscE2eTestCase):
    """Run a High, Medium, Low Report"""

    def setUp(self):
        """Set Up"""
        super(RunHighMedLow, self).setUp()
        # Initialize Page Objects
        self.labs = LabsPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_high_med_low(self):
        self.labs.nav_link.click()
        self.labs.high_med_low.click()
        self.assertEqual(self.select.title.text, ReportTypes.HIGH_MED_LOW.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, HML.PROD.value, HML.PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, HML.CAT.value, HML.CAT_LEV.value, HML.CAT_SEL.value)

    def test_d_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, HML.STORE.value, HML.STORE_LEV.value)

    def test_e_metric(self):
        self.select.hml_input(Prompts.ANY.value, HML.METRIC.value,
                              HML.HIGH.value, HML.MED.value, HML.LOW.value)

    def test_f_adv_date(self):
        self.select.advanced_options.click()
        self.select.clear_prompt(PromptElements.LATEST_12_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, HML.DATE.value)

    def test_g_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, HML.CHAN.value)

    def test_h_adv_pg(self):
        self.select.search_input(Prompts.PG.value, HML.PG.value)

    def test_i_adv_store_level(self):
        self.select.basic_input(Prompts.STORE_LEVEL.value, HML.STORE_LEVEL.value)

    def test_j_adv_prod_level(self):
        self.select.search_input(Prompts.PRODUCT_LEVEL.value, HML.PROD_LEVEL.value)

    def test_k_adv_benchmark_pg(self):
        self.select.search_input(Prompts.SHOPPERS.value, HML.BENCH_PG.value)

    def test_l_adv_location(self):
        self.select.folder_input(Prompts.LOCATION.value, HML.LOCATION.value, HML.GEO_LEV.value)

    def test_m_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, HML.WEIGHT.value)

    def test_n_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, HML.STAT.value)

    def test_o_run_report(self):
        name = ReportTypes.HIGH_MED_LOW.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
