from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.brand import BrandPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import SE


class RunShareExplorer(IscE2eTestCase):
    """Run a Share Explorer Report"""

    def setUp(self):
        """Set Up"""
        super(RunShareExplorer, self).setUp()
        # Initialize Page Objects
        self.brand = BrandPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_share_explorer(self):
        """Navigate to Share Explorer"""
        self.brand.nav_link.click()
        self.brand.share_explorer.click()
        self.assertEqual(self.select.title.text, ReportTypes.SHARE_EXPLORER.value)

    def test_b_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, SE.PROD.value, SE.PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, SE.CAT.value, SE.CAT_LEV.value, SE.CAT_SEL.value)

    def test_d_date_range(self):
        self.select.basic_input(Prompts.DATE_RANGE.value, SE.DATE.value)

    def test_e_split(self):
        self.select.basic_input(Prompts.SPLIT.value, SE.SPLIT.value)

    def test_f_level(self):
        self.select.folder_input(Prompts.LEVEL.value, SE.LEV.value, SE.LEV_LEV.value)

    def test_g_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, SE.PG.value)

    def test_h_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, SE.STORE.value, SE.STORE_LEV.value)

    def test_i_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, SE.CHAN.value)

    def test_j_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, SE.LOCATION.value, SE.GEO_LEV.value)

    def test_k_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, SE.WEIGHT.value)

    def test_l_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, SE.STAT.value)

    def test_m_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.SHARE_EXPLORER .value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
