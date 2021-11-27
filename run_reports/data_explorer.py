from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.brand import BrandPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import DE


class RunDataExplorer(IscE2eTestCase):
    """Run a Data Explorer Report"""

    def setUp(self):
        """Set Up"""
        super(RunDataExplorer, self).setUp()
        # Initialize Page Objects
        self.brand = BrandPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_data_explorer(self):
        """Navigate to Data Explorer"""
        self.brand.nav_link.click()
        self.brand.data_explorer.click()
        self.assertEqual(self.select.title.text, ReportTypes.DATA_EXPLORER.value)

    def test_b_metrics(self):
        METS = [DE.MET_1.value, DE.MET_2.value, DE.MET_3.value, DE.MET_4.value]
        MET_LEVS = [DE.MET_1_LEV.value, DE.MET_2_LEV.value, DE.MET_3_LEV.value, DE.MET_4_LEV.value]
        self.select.list_inputs(Prompts.METRICS.value, METS, MET_LEVS)

    def test_c_level(self):
        LEVS = [DE.LEV_1.value, DE.LEV_2.value, DE.LEV_3.value, DE.LEV_4.value,
                DE.LEV_5.value, DE.LEV_6.value, DE.LEV_7.value, DE.LEV_8.value]
        LEV_LEVS = [DE.LEV_1_LEV.value, DE.LEV_2_LEV.value, DE.LEV_3_LEV.value, DE.LEV_4_LEV.value,
                    DE.LEV_5_LEV.value, DE.LEV_6_LEV.value, DE.LEV_7_LEV.value, DE.LEV_8_LEV.value]
        self.select.ranked_inputs(Prompts.LEVEL.value, LEVS, LEV_LEVS)
        if None not in LEVS:
            self.assertEqual(self.select.alert_text.text, PromptElements.MAX_8.value)
        self.select.attribute_ranker(LEVS, [7, 6, 5, 4], [2, 3, 4, 5, 6])

    def test_d_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, DE.PROD.value, DE.PROD_LEV.value)

    def test_e_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, DE.CAT.value, DE.CAT_LEV.value, DE.CAT_SEL.value)

    def test_f_date_range(self):
        self.select.clear_prompt(PromptElements.LATEST_12_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, DE.DATE.value)

    def test_g_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, DE.PG.value)

    def test_h_adv_period(self):
        self.select.basic_input(Prompts.NONE.value, DE.PERIOD.value)

    def test_i_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, DE.STORE.value, DE.STORE_LEV.value)

    def test_j_adv_channel(self):
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, DE.CHAN.value, DE.CHAN_LEV.value)

    def test_k_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, DE.LOCATION.value, DE.GEO_LEV.value)

    def test_l_adv_tg(self):
        self.select.search_input(Prompts.TG.value, DE.TG.value)

    def test_m_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, DE.WEIGHT.value)

    def test_n_adv_custom(self):
        self.select.folder_input(Prompts.CUSTOM_SELECT.value, DE.CUSTOM.value, DE.CUSTOM_LEV.value)

    def test_o_adv_adjustment(self):
        self.select.clear_prompt(PromptElements.TCC_TENURE.value).click()
        self.select.basic_input(Prompts.TCC_TENURE.value, DE.ADJUST.value)

    def test_p_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, DE.STAT.value)

    def test_q_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.DATA_EXPLORER.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
