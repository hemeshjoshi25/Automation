from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.promo import PromoPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import EA


class RunEventAnalysisCG(IscE2eTestCase):
    """Run an Event Analysis Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunEventAnalysisCG, self).setUp()
        self.promo = PromoPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_event_analysis(self):
        """Navigate to Event Analysis"""
        self.promo.nav_link.click()
        self.promo.event_analysis.click()
        self.assertEqual(self.select.title.text, ReportTypes.EVENT_ANALYSIS.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, EA.CG_PROD.value, EA.CG_PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, EA.CG_CAT.value, EA.CG_CAT_LEV.value)

    def test_d_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, EA.STORE.value, EA.STORE_LEV.value)

    def test_e_promo_dates(self):
        self.select.promo_dates(Prompts.PROMO_DATES.value, EA.START.value, EA.END.value)

    def test_f_adv_promo(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PROMO.value, EA.PROMO.value)

    def test_g_adv_portfolio(self):
        self.select.search_hierarchy(Prompts.PORTFOLIO.value, EA.PORT.value, EA.PORT_LEV.value)

    def test_h_adv_pre_period(self):
        self.select.clear_prompt(PromptElements.WEEKS_26.value).click()
        self.select.basic_input(Prompts.NUM_WEEKS.value, EA.PRE.value)

    def test_i_adv_post_period(self):
        self.select.clear_prompt(PromptElements.WEEKS_13.value).click()
        self.select.search_input(Prompts.NUM_WEEKS.value, EA.POST.value)

    def test_j_adv_pg(self):
        self.select.search_input(Prompts.PG.value, EA.PG.value)

    def test_k_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, EA.LOCATION.value, EA.GEO_LEV.value)

    def test_l_adv_channel(self):
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, EA.CHAN.value, EA.CHAN_LEV.value)

    def test_m_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, EA.WEIGHT.value)

    def test_n_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, EA.STAT.value)

    def test_o_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.EVENT_ANALYSIS.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
