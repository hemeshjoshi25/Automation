from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.brand import BrandPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import BC


class RunBricksClicksCG(IscE2eTestCase):
    """Run a Bricks and Clicks Report with Custom Groups"""

    def setUp(self):
        """Set Up"""
        super(RunBricksClicksCG, self).setUp()
        # Initialize Page Objects
        self.brand = BrandPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_bricks_clicks(self):
        """Navigate to Bricks and Clicks"""
        self.brand.nav_link.click()
        self.brand.bricks_clicks.click()
        self.assertEqual(self.select.title.text, ReportTypes.BRICKS_AND_CLICKS.value)

    def test_b_category(self):
        self.select.search_hierarchy(Prompts.CATEGORY.value, BC.CG_CAT.value, BC.CG_CAT_LEV.value)

    def test_c_product(self):
        self.select.search_hierarchy(Prompts.PRODUCT.value, BC.CG_PROD.value, BC.CG_PROD_LEV.value)

    def test_d_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, BC.PG.value)

    def test_e_adv_date_range(self):
        self.select.clear_prompt(PromptElements.LATEST_12_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, BC.DATE.value)

    def test_f_adv_period(self):
        self.select.clear_prompt(PromptElements.YEAR_AGO.value).click()
        self.select.basic_input(Prompts.NONE.value, BC.PERIOD.value)

    def test_g_adv_channel(self):
        prompt = PromptElements.FMCG.value + ' or 1 more'
        self.select.get_prompt(prompt).click()
        self.select.validate_prompt(prompt)

    def test_h_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, BC.LOCATION.value, BC.GEO_LEV.value)

    def test_i_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, BC.WEIGHT.value)

    def test_j_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, BC.STAT.value)

    def test_k_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.BRICKS_AND_CLICKS.value
        rename = ReportTypes.PREFIX_CG.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
