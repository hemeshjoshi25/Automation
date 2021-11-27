from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.new_item import NewItemPage
from pageobjects.prompts.select_prompt import SelectPromptPage
from pageobjects.history import HistoryPage
from constants.enums import ReportTypes, Prompts, PromptElements
from constants.prompt_selections import NIT


class RunNewItemTracker(IscE2eTestCase):
    """Run a New Item Tracker Report"""

    def setUp(self):
        """Set Up"""
        super(RunNewItemTracker, self).setUp()
        # Initialize Page Objects
        self.new_item = NewItemPage(self.driver)
        self.select = SelectPromptPage(self.driver)
        self.history = HistoryPage(self.driver)

    def test_a_nav_new_item_tracker(self):
        """Navigate to New Item Tracker"""
        self.new_item.nav_link.click()
        self.new_item.new_item_tracker.click()
        self.assertEqual(self.select.title.text, ReportTypes.NEW_ITEM_TRACKER.value)

    def test_b_new_items(self):
        NI = [NIT.NI_1.value, NIT.NI_2.value, NIT.NI_3.value, NIT.NI_4.value, NIT.NI_5.value]
        self.select.new_items(Prompts.NEW_ITEMS.value, NI)
        if None not in NI:
            self.assertEqual(self.select.alert_text.text, PromptElements.MAX_5.value)
        self.select.deselect_list(NI)

    def test_c_adv_pg(self):
        self.select.advanced_options.click()
        self.select.search_input(Prompts.PG.value, NIT.PG.value)

    def test_d_adv_store(self):
        self.select.search_hierarchy(Prompts.STORE.value, NIT.STORE.value, NIT.STORE_LEV.value)

    def test_e_adv_geography(self):
        self.select.folder_input(Prompts.LOCATION.value, NIT.LOCATION.value, NIT.GEO_LEV.value)

    def test_f_adv_channel(self):
        self.select.basic_input(Prompts.PARENT_CHANNEL.value, NIT.CHAN.value)

    def test_g_adv_weight(self):
        self.select.search_input(Prompts.CHANNEL_WEIGHT.value, NIT.WEIGHT.value)

    def test_h_adv_static(self):
        self.select.clear_prompt(PromptElements.BRICK_MORTAR.value).click()
        self.select.basic_input(Prompts.STATIC.value, NIT.STAT.value)

    def test_i_run_report(self):
        """Run and Rename Report"""
        name = ReportTypes.NEW_ITEM_TRACKER.value
        rename = ReportTypes.PREFIX.value + name
        self.select.run_report_button.click()
        self.history.rename_report(name, rename)
        # Set to Pass
        self.__class__.test_result = 'pass'
