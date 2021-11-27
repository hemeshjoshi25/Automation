from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.new_item import NewItemPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import NISOVA


class RunNewItemSOVA(IscE2eTestCase):
    """Run a New Item SOVA Report"""

    def setUp(self):
        """Set Up"""
        super(RunNewItemSOVA, self).setUp()
        # Initialize Page Objects
        self.new_item = NewItemPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_new_item_sova(self):
        """Navigate to New Item SOVA"""
        self.new_item.nav_link.click()
        self.new_item.new_item_sova.click()
        self.assertEqual(self.select.title.text, ReportTypes.NEW_ITEM_SOVA.value)

    def test_b_new_items(self):
        NI = [NISOVA.NI_1.value, NISOVA.NI_2.value, NISOVA.NI_3.value, NISOVA.NI_4.value, NISOVA.NI_5.value]
        self.select.new_items(Prompts.NEW_ITEMS.value, NI)
        if None not in NI:
            self.assertEqual(self.select.alert_text.text, PromptElements.MAX_5.value)
        self.select.deselect_list(NI)

    def test_c_adv_category(self):
        self.select.advanced_options.click()
        self.select.search_hierarchy_select(Prompts.CATEGORY.value, NISOVA.CAT.value,
                                            NISOVA.CAT_LEV.value, NISOVA.CAT_SEL.value)

    def test_d_adv_portfolio(self):
        self.select.search_hierarchy(Prompts.PORTFOLIO.value, NISOVA.PORT.value, NISOVA.PORT_LEV.value)

    def test_e_adv_period(self):
        self.select.clear_prompt(PromptElements.WEEKS_26.value).click()
        self.select.basic_input(Prompts.NUM_WEEKS.value, NISOVA.PERIOD.value)

    def test_f_adv_pg(self):
        self.select.search_input(Prompts.PG.value, NISOVA.PG.value)

    def test_g_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, NISOVA.STORE.value, NISOVA.STORE_LEV.value)

    def test_h_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, NISOVA.CHAN.value)

    def test_i_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, NISOVA.WEIGHT.value)

    def test_j_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, NISOVA.STAT.value)

    def test_k_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.NEW_ITEM_SOVA.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
