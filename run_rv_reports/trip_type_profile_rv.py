from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.shopper import ShopperPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import TTP


class RunTripTypeProfileRV(IscE2eTestCase):
    """Run a Trip Type Profile in Retailer View"""

    def setUp(self):
        """Set Up"""
        super(RunTripTypeProfileRV, self).setUp()
        # Initialize Page Objects
        self.shopper = ShopperPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_trip_type(self):
        """Navigate to Trip Type Profile"""
        self.shopper.nav_link.click()
        self.shopper.trip_type_profile.click()
        self.assertEqual(self.select.title.text, ReportTypes.TRIP_TYPE_PROFILE.value)

    def test_b_category(self):
        self.select.get_prompt(Prompts.CATEGORY.value).click()
        self.select.validate_prompt(Prompts.CATEGORY.value)

    def test_c_product_level(self):
        self.select.search_input(Prompts.PRODUCT_LEVEL.value, TTP.RV_PROD_LEV.value)

    def test_d_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, TTP.RV_STORE.value, TTP.RV_STORE_LEV.value)

    def test_e_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, TTP.DATE.value)

    def test_f_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, TTP.PG.value)

    def test_g_adv_store_level(self):
        self.select.basic_input(Prompts.STORE_LEVEL.value, TTP.STORE_LEVEL.value)

    def test_h_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, TTP.LOCATION.value, TTP.GEO_LEV.value)

    def test_i_adv_channel(self):
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, TTP.CHAN.value, TTP.CHAN_LEV.value)

    def test_j_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, TTP.WEIGHT.value)

    def test_k_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, TTP.STAT.value)

    def test_l_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.TRIP_TYPE_PROFILE.value
        rename = ReportTypes.PREFIX_RV.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
