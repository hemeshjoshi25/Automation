from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.shopper import ShopperPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import TC


class RunTripCircuits(IscE2eTestCase):
    """Run a Trip Circuits Report"""

    def setUp(self):
        """Set Up"""
        super(RunTripCircuits, self).setUp()
        # Initialize Page Objects
        self.shopper = ShopperPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_trip_circuits(self):
        """Navigate to Trip Circuits"""
        self.shopper.nav_link.click()
        self.shopper.trip_circuits.click()
        self.assertEqual(self.select.title.text, ReportTypes.TRIP_CIRCUITS.value)

    def test_b_trip_circuit_type(self):
        self.select.basic_input(Prompts.TRIP_CIRCUIT_TYPE.value, TC.TYPE.value)

    def test_c_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, TC.PROD.value, TC.PROD_LEV.value)

    def test_d_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, TC.CAT.value, TC.CAT_LEV.value, TC.CAT_SEL.value)

    def test_e_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, TC.STORE.value, TC.STORE_LEV.value)

    def test_f_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, TC.PG.value)

    def test_g_adv_tg(self):
        self.select.search_input(Prompts.TG.value, TC.TG.value)

    def test_h_adv_prod_lev(self):
        self.select.search_input(Prompts.SAME_PROD.value, TC.PROD_LEV_PROMPT.value)

    def test_i_adv_group_prod_lev(self):
        self.select.search_input(Prompts.SAME_CAT.value, TC.GROUP_PROD_LEV.value)

    def test_j_adv_store_lev(self):
        self.select.basic_input(Prompts.STORE_LEVEL.value, TC.STORE_LEVEL.value)

    def test_k_adv_date_range(self):
        self.select.clear_prompt(PromptElements.LATEST_3_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, TC.DATE.value)

    def test_l_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, TC.LOCATION.value, TC.GEO_LEV.value)

    def test_m_adv_channel(self):
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, TC.CHAN.value, TC.CHAN_LEV.value)

    def test_n_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, TC.STAT.value)

    def test_o_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.TRIP_CIRCUITS.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
