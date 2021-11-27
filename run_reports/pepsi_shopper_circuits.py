from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.tools import ToolsPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import PSC


class RunPepsiShopperCircuits(IscE2eTestCase):
    """Run a Pepsi Shopper Circuits Report"""

    def setUp(self):
        """Set Up"""
        super(RunPepsiShopperCircuits, self).setUp()
        # Initialize Page Objects
        self.tools = ToolsPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_pepsi_shopper_circuits(self):
        """Navigate to Pepsi Shopper Circuits"""
        self.tools.nav_link.click()
        self.tools.pepsi_shopper_circuits.click()
        self.assertEqual(self.select.title.text, ReportTypes.PEPSI_SHOPPER_CIRCUITS.value)

    def test_b_analysis_retailer(self):
        self.select.search_input(Prompts.RETAILER.value, PSC.RETAILER.value)

    def test_c_store_level(self):
        self.select.clear_prompt(PromptElements.PEPSI_WHOLE_FOODS.value).click()
        self.select.basic_input(Prompts.STORE_LEVEL.value, PromptElements.PEPSI_WHOLE_FOODS.value)

    def test_d_category(self):
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, PSC.CAT.value, PSC.CAT_LEV.value, PSC.CAT_SEL.value)

    def test_e_area(self):
        self.select.folder_input(Prompts.COMP_AREA.value, PSC.AREA.value, PSC.AREA_LEV.value)

    def test_f_adv_people_group(self):
        self.select.search_input(Prompts.PG.value, PSC.PG.value)

    def test_g_date(self):
        self.select.clear_prompt(PromptElements.LATEST_12_MONTHS.value).click()
        self.select.basic_input(Prompts.DATE_RANGE.value, PSC.DATE.value)

    def test_h_adv_channel_circuit(self):
        self.select.advanced_options.click()
        self.select.get_prompt(PromptElements.PEPSI_CHANNEL.value).click()
        self.select.validate_prompt(PromptElements.PEPSI_CHANNEL.value)

    def test_i_adv_pepsi_edible(self):
        self.select.get_prompt(PromptElements.PEPSI_EDIBLE.value, 0).click()
        self.select.validate_prompt(PromptElements.PEPSI_EDIBLE.value, 0)

    def test_j_adv_total_edible(self):
        self.select.get_prompt(PromptElements.PEPSI_EDIBLE.value).click()
        self.select.validate_prompt(PromptElements.PEPSI_EDIBLE.value)

    def test_k_adv_channel(self):
        self.select.folder_input(Prompts.CHANNEL_PARENT_CHANNEL.value, PSC.CHAN.value, PSC.CHAN_LEV.value)

    def test_l_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, PSC.WEIGHT.value)

    def test_m_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, PSC.STAT.value)

    def test_n_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.PEPSI_SHOPPER_CIRCUITS.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
