from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.brand import BrandPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import PS


class RunPeopleScorecardCG(IscE2eTestCase):
    """Run a People Scorecard Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunPeopleScorecardCG, self).setUp()
        # Initialize Page Objects
        self.brand = BrandPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_people_scorecard(self):
        """Navigate to People Scorecard"""
        self.brand.nav_link.click()
        self.brand.people_scorecard.click()
        self.assertEqual(self.select.title.text, ReportTypes.PEOPLE_SCORECARD.value)

    def test_b_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, PS.CG_CAT.value, PS.CG_CAT_LEV.value)

    def test_c_people_level(self):
        PEOPLE_LEVS = [PS.PEOPLE_LEV_1.value, PS.PEOPLE_LEV_2.value]
        LEV_LEVS = [PS.PEOPLE_LEV_LEV_1.value, PS.PEOPLE_LEV_LEV_2.value]
        self.select.list_inputs(Prompts.LEVEL.value, PEOPLE_LEVS, LEV_LEVS, 0)

    def test_d_product_level(self):
        self.select.folder_input(Prompts.LEVEL.value, PS.PROD_LEV.value, PS.PROD_LEV_LEV.value)

    def test_e_metric(self):
        METS = [PS.MET_1.value, PS.MET_2.value, PS.MET_3.value, PS.MET_4.value]
        MET_LEVS = [PS.MET_1_LEV.value, PS.MET_2_LEV.value, PS.MET_3_LEV.value, PS.MET_4_LEV.value]
        self.select.list_inputs(Prompts.METRICS.value, METS, MET_LEVS)

    def test_f_date_range(self):
        self.select.clear_prompt(PromptElements.LATEST_52_WEEKS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, PS.DATE.value)

    def test_g_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, PS.PG.value)

    def test_h_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, PS.STORE.value, PS.STORE_LEV.value)

    def test_i_adv_channel(self):
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, PS.CHAN.value, PS.CHAN_LEV.value)

    def test_j_benchmark(self):
        self.select.clear_prompt(PromptElements.AVG_SELECTION.value).click()
        self.select.basic_input(Prompts.BENCHMARK.value, PS.BENCH.value)

    def test_k_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, PS.LOCATION.value, PS.GEO_LEV.value)

    def test_l_adv_tg(self):
        self.select.search_input(Prompts.TG.value, PS.TG.value)

    def test_m_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, PS.WEIGHT.value)

    def test_n_adv_custom(self):
        self.select.folder_input(Prompts.CUSTOM_SELECT.value, PS.CUSTOM.value, PS.CUSTOM_LEV.value)

    def test_o_adv_adjustment(self):
        self.select.clear_prompt(PromptElements.TCC_TENURE.value).click()
        self.select.basic_input(Prompts.TCC_TENURE.value, PS.ADJUST.value)

    def test_p_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, PS.STAT.value)

    def test_q_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.PEOPLE_SCORECARD.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
