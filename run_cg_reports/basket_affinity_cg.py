from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.people import PeoplePage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import BA


class RunBasketAffinityCG(IscE2eTestCase):
    """Run a Basket Affinity Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunBasketAffinityCG, self).setUp()
        # Initialize Page Objects
        self.people = PeoplePage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_basket_affinity(self):
        """Navigate to Basket Affinity"""
        self.people.nav_link.click()
        self.people.basket_affinity.click()
        self.assertEqual(self.select.title.text, ReportTypes.BASKET_AFFINITY.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, BA.CG_PROD.value, BA.CG_PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, BA.CG_CAT.value, BA.CG_CAT_LEV.value)

    def test_d_product_level(self):
        PROD_LEVS = [BA.PROD_LEV_1.value, BA.PROD_LEV_2.value]
        self.select.product_levels(Prompts.PRODUCT_LEVEL.value, PROD_LEVS)
        if None not in PROD_LEVS:
            self.assertEqual(self.select.alert_text.text, PromptElements.MAX_2.value)

    def test_e_comp_product(self):
        self.select.search_hierarchy_select(Prompts.COMP_PRODUCT.value, BA.COMP_PROD.value,
                                            BA.COMP_PROD_LEV.value, BA.COMP_PROD_SEL.value)

    def test_f_adv_date_range(self):
        self.select.advanced_options.click()
        self.select.clear_prompt(PromptElements.LATEST_3_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, BA.DATE.value)

    def test_g_adv_people_group(self):
        self.select.search_input(Prompts.PG.value, BA.PG.value)

    def test_h_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, BA.STORE.value, BA.STORE_LEV.value)

    def test_i_adv_channel(self):
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, BA.CHAN.value, BA.CHAN_LEV.value)

    def test_j_adv_location(self):
        self.select.folder_input(Prompts.LOCATION.value, BA.LOCATION.value, BA.GEO_LEV.value)

    def test_k_adv_trip_group(self):
        self.select.search_input(Prompts.TG.value, BA.TG.value)

    def test_l_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, BA.WEIGHT.value)

    def test_m_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, BA.STAT.value)

    def test_n_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.BASKET_AFFINITY.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
