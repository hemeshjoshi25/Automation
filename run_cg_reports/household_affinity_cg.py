from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.people import PeoplePage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import HA


class RunHouseholdAffinityCG(IscE2eTestCase):
    """Run a Household Affinity Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunHouseholdAffinityCG, self).setUp()
        # Initialize Page Objects
        self.people = PeoplePage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_household_affinity(self):
        """Navigate to Household Affinity"""
        self.people.nav_link.click()
        self.people.household_affinity.click()
        self.assertEqual(self.select.title.text, ReportTypes.HOUSEHOLD_AFFINITY.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, HA.CG_PROD.value, HA.CG_PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, HA.CG_CAT.value, HA.CG_CAT_LEV.value)

    def test_d_people_group(self):
        self.select.search_input(Prompts.PG.value, HA.PG.value)

    def test_e_all_shoppers(self):
        self.select.search_input(Prompts.SHOPPERS.value, HA.COMP_PG.value)

    def test_f_product_level(self):
        PROD_LEVS = [HA.PROD_LEV_1.value, HA.PROD_LEV_2.value, HA.PROD_LEV_3.value]
        self.select.product_levels(Prompts.PRODUCT_LEVEL.value, PROD_LEVS)
        if None not in PROD_LEVS:
            self.assertEqual(self.select.alert_text.text, PromptElements.MAX_3.value)

    def test_g_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, HA.DATE.value)

    def test_h_adv_store(self):
        self.select.advanced_options.click()
        self.select.search_hierarchy(Prompts.STORE.value, HA.STORE.value, HA.STORE_LEV.value)

    def test_i_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, HA.LOCATION.value, HA.GEO_LEV.value)

    def test_j_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, HA.CHAN.value)

    def test_k_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, HA.WEIGHT.value)

    def test_l_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, HA.STAT.value)

    def test_m_run_report(self):
        name = ReportTypes.HOUSEHOLD_AFFINITY.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
