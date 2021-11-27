from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.people import PeoplePage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import SP


class RunShopperProfile(IscE2eTestCase):
    """Run a Shopper Profile Report"""

    def setUp(self):
        """Set Up"""
        super(RunShopperProfile, self).setUp()
        # Initialize Page Objects
        self.people = PeoplePage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_shopper_profile(self):
        """Navigate to Shopper Profile"""
        self.people.nav_link.click()
        self.people.shopper_profile.click()
        self.assertEqual(self.select.title.text, ReportTypes.SHOPPER_PROFILE.value)

    def test_b_people_group(self):
        self.select.search_input(Prompts.PG.value, SP.PG.value)

    def test_c_all_shoppers(self):
        self.select.search_input(Prompts.SHOPPERS.value, SP.COMP_PG.value)

    def test_d_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, SP.DATE.value)

    def test_e_adv_product(self):
        self.select.advanced_options.click()
        self.select.search_hierarchy(Prompts.PRODUCT.value, SP.PROD.value, SP.PROD_LEV.value)

    def test_f_adv_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, SP.CAT.value, SP.CAT_LEV.value, SP.CAT_SEL.value, 0)

    def test_g_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, SP.STORE.value, SP.STORE_LEV.value, 0)

    def test_h_adv_comp_product(self):
        self.select.search_hierarchy(Prompts.COMP_PRODUCT.value, SP.COMP_PROD.value, SP.COMP_PROD_LEV.value)

    def test_i_adv_comp_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, SP.COMP_CAT.value,
                                            SP.COMP_CAT_LEV.value, SP.COMP_CAT_SEL.value)

    def test_j_adv_comp_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, SP.COMP_STORE.value, SP.COMP_STORE_LEV.value)

    def test_k_adv_channel(self):
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, SP.CHAN.value, SP.CHAN_LEV.value)

    def test_l_adv_location(self):
        self.select.folder_input(Prompts.LOCATION.value, SP.LOCATION.value, SP.GEO_LEV.value)

    def test_m_adv_trip_group(self):
        self.select.search_input(Prompts.TG.value, SP.TG.value)

    def test_n_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, SP.WEIGHT.value)

    def test_o_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, SP.STAT.value)

    def test_p_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.SHOPPER_PROFILE.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
