from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.labs import LabsPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import CR


class RunCountReportCG(IscE2eTestCase):
    """Run a Count Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunCountReportCG, self).setUp()
        # Initialize Page Objects
        self.labs = LabsPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_count_report(self):
        """Navigate to Count Report"""
        self.labs.nav_link.click()
        self.labs.count_report.click()
        self.assertEqual(self.select.title.text, ReportTypes.COUNT_REPORT.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, CR.CG_PROD.value, CR.CG_PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, CR.CG_CAT.value, CR.CG_CAT_LEV.value)

    def test_d_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, CR.STORE.value, CR.STORE_LEV.value)

    def test_e_level(self):
        LEVS = [CR.LEV_1.value, CR.LEV_2.value, CR.LEV_3.value, CR.LEV_4.value, CR.LEV_5.value]
        LEV_LEVS = [CR.LEV_1_LEV.value, CR.LEV_2_LEV.value, CR.LEV_3_LEV.value, CR.LEV_4_LEV.value, CR.LEV_5_LEV.value]
        self.select.ranked_inputs(Prompts.LEVEL.value, LEVS, LEV_LEVS)
        if None not in LEVS:
            self.assertEqual(self.select.alert_text.text, PromptElements.MAX_5.value)

    def test_f_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, CR.STAT.value)

    def test_g_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, CR.PG.value)

    def test_h_adv_date_range(self):
        self.select.clear_prompt(PromptElements.LATEST_12_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, CR.DATE.value)

    def test_i_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, CR.LOCATION.value, CR.GEO_LEV.value)

    def test_j_adv_tg(self):
        self.select.search_input(Prompts.TG.value, CR.TG.value)

    def test_k_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, CR.CHAN.value)

    def test_l_adv_transcription(self):
        self.select.clear_prompt(PromptElements.FULL.value).click()
        self.select.basic_input(Prompts.NONE.value, CR.TRANS.value)

    def test_m_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.COUNT_REPORT.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
