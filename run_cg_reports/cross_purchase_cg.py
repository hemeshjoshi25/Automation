from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.people import PeoplePage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import CP


class RunCrossPurchaseCG(IscE2eTestCase):
    """Run a Cross Purchase Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunCrossPurchaseCG, self).setUp()
        # Initialize Page Objects
        self.people = PeoplePage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_cross_purchase(self):
        """Navigate to Cross Purchase"""
        self.people.nav_link.click()
        self.people.cross_purchase.click()
        self.assertEqual(self.select.title.text, ReportTypes.CROSS_PURCHASE.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, CP.CG_PROD.value, CP.CG_PROD_LEV.value)

    def test_c_product_level(self):
        self.select.search_input(Prompts.PRODUCT_LEVEL.value, CP.PROD_LEVEL.value, 0)

    def test_d_comp_product(self):
        self.select.search_hierarchy(Prompts.COMP_PRODUCT.value,
                                     CP.CG_COMP_PROD.value, CP.CG_COMP_PROD_LEV.value)

    def test_e_comp_product_level(self):
        self.select.search_input(Prompts.PRODUCT_LEVEL.value, CP.COMP_PROD_LEV.value)

    def test_f_adv_date_range(self):
        self.select.advanced_options.click()
        self.select.clear_prompt(PromptElements.LATEST_6_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, CP.DATE.value)

    def test_g_adv_pg(self):
        self.select.search_input(Prompts.PG.value, CP.PG.value)

    def test_h_adv_focus_cat(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, CP.FOCUS_CAT.value,
                                            CP.FOCUS_CAT_LEV.value, CP.FOCUS_CAT_SEL.value, 0)

    def test_i_adv_focus_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, CP.FOCUS_STORE.value, CP.FOCUS_STORE_LEV.value, 0)

    def test_j_adv_comp_cat(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, CP.COMP_CAT.value,
                                            CP.COMP_CAT_LEV.value, CP.COMP_CAT_SEL.value)

    def test_k_adv_comp_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, CP.COMP_STORE.value, CP.COMP_STORE_LEV.value)

    def test_l_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, CP.CHAN.value)

    def test_m_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, CP.LOCATION.value, CP.GEO_LEV.value)

    def test_n_adv_tg(self):
        self.select.search_input(Prompts.TG.value, CP.TG.value)

    def test_o_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, CP.STAT.value)

    def test_p_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.CROSS_PURCHASE.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
