from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.brand import BrandPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import MOT


class RunMomentsOfTruth(IscE2eTestCase):
    """Run a Moments of Truth Report"""

    def setUp(self):
        """Set Up"""
        super(RunMomentsOfTruth, self).setUp()
        # Initialize Page Objects
        self.brand = BrandPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_moments_of_truth(self):
        """Navigate to Moments of Truth"""
        self.brand.nav_link.click()
        self.brand.moments_of_truth.click()
        self.assertEqual(self.select.title.text, ReportTypes.MOMENTS_OF_TRUTH.value)

    def test_b_product_level(self):
        self.select.search_input(Prompts.PRODUCT_LEVEL.value, MOT.PROD_LEV.value)

    def test_c_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, MOT.CAT.value, MOT.CAT_LEV.value, MOT.CAT_SEL.value)

    def test_d_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, MOT.PG.value)

    def test_e_adv_date_range(self):
        self.select.clear_prompt(PromptElements.LATEST_52_WEEKS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, MOT.DATE.value)

    def test_f_adv_store(self):
        self.select.folder_input(Prompts.STORE.value, MOT.STORE.value, MOT.STORE_LEV.value)

    def test_g_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, MOT.CHAN.value)

    def test_h_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, MOT.LOCATION.value, MOT.GEO_LEV.value)

    def test_i_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, MOT.STAT.value)

    def test_j_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.MOMENTS_OF_TRUTH.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
