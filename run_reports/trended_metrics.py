from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.brand import BrandPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import TM


class RunTrendedMetrics(IscE2eTestCase):
    """Run a Trended Metrics Report"""

    def setUp(self):
        """Set Up"""
        super(RunTrendedMetrics, self).setUp()
        # Initialize Page Objects
        self.brand = BrandPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_trended_metrics(self):
        """Navigate to Trended Metrics"""
        self.brand.nav_link.click()
        self.brand.trended_metrics.click()
        self.assertEqual(self.select.title.text, ReportTypes.TRENDED_METRICS.value)

    def test_b_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, TM.CAT.value, TM.CAT_LEV.value, TM.CAT_SEL.value)

    def test_c_level(self):
        LEVS = [TM.LEV_1.value, TM.LEV_2.value, TM.LEV_3.value, TM.LEV_4.value, TM.LEV_5.value]
        LEV_LEVS = [TM.LEV_1_LEV.value, TM.LEV_2_LEV.value, TM.LEV_3_LEV.value, TM.LEV_4_LEV.value, TM.LEV_5_LEV.value]
        self.select.ranked_inputs(Prompts.LEVEL.value, LEVS, LEV_LEVS)
        if None not in LEVS:
            self.assertEqual(self.select.alert_text.text, PromptElements.MAX_5.value)
        self.select.attribute_ranker(LEVS, [2, 1, 3, 2], [3, 2])

    def test_d_metric(self):
        METS = [TM.MET_1.value, TM.MET_2.value, TM.MET_3.value, TM.MET_4.value]
        MET_LEVS = [TM.MET_1_LEV.value, TM.MET_2_LEV.value, TM.MET_3_LEV.value, TM.MET_4_LEV.value]
        self.select.list_inputs(Prompts.METRICS.value, METS, MET_LEVS)

    def test_e_time_interval(self):
        self.select.search_input(Prompts.TIME_INTERVAL.value, TM.TIME.value)

    def test_f_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, TM.DATE.value)

    def test_g_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, TM.PG.value)

    def test_h_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, TM.STORE.value, TM.STORE_LEV.value)

    def test_i_adv_channel(self):
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, TM.CHAN.value, TM.CHAN_LEV.value)

    def test_j_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, TM.LOCATION.value, TM.GEO_LEV.value)

    def test_k_adv_tg(self):
        self.select.search_input(Prompts.TG.value, TM.TG.value)

    def test_l_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, TM.WEIGHT.value)

    def test_m_adv_custom(self):
        self.select.folder_input(Prompts.CUSTOM_SELECT.value, TM.CUSTOM.value, TM.CUSTOM_LEV.value)

    def test_n_adv_adjustment(self):
        self.select.clear_prompt(PromptElements.TCC_TENURE.value).click()
        self.select.basic_input(Prompts.TCC_TENURE.value, TM.ADJUST.value)

    def test_o_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, TM.STAT.value)

    def test_p_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.TRENDED_METRICS.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
