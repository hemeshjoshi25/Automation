from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.new_item_tracker import NewItemTrackerPage
from constants.enums import ReportTypes
from constants.reports.new_item_tracker import NIT


class TestNewItemTracker(IscE2eTestCase):
    def setUp(self):
        super(TestNewItemTracker, self).setUp()
        self.history = HistoryPage(self.driver)
        self.nit = NewItemTrackerPage(self.driver)

    def test_a_nav_nit(self):
        nit = ReportTypes.NEW_ITEM_TRACKER.value
        title = ReportTypes.PREFIX.value + nit
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.nit.title.text, nit + ': ' + title)

    def test_b_summary_tab(self):
        self.nit.summary_tab()
        self.nit.dropdown_validate(NIT.NI_1)
        self.nit.tree_titles_validate(NIT.TREE_TITLES)
        self.nit.download_diagram()

    def test_c_trial_repeat_tab(self):
        self.nit.trial_repeat_tab()
        self.nit.dropdown_validate(NIT.TIME_DROP[0])
        self.nit.dropdown_validate(NIT.MET_DROP[0], 1)
        for t in range(2):
            self.nit.select_dropdown(t, NIT.TIME_DROP[t])
            for m in range(7):
                self.nit.select_dropdown(m, NIT.MET_DROP[m], 1)
                self.nit.chart_legend_validate([NIT.TRIAL_LEG.format(NIT.MET_DROP[m])])
                self.nit.headers_validate(NIT.TRIAL_HEAD, form=NIT.MET_DROP[m].upper())
                for c in range(2):
                    self.nit.test_sort(c)
                self.nit.scroll_top()

    def test_d_repeat_drivers_tab(self):
        self.nit.repeat_drivers_tab()
        self.nit.dropdown_validate(NIT.REPEAT_DROP[0])
        for d in range(2):
            self.nit.select_dropdown(d, NIT.REPEAT_DROP[d])
            self.nit.legend_validate(NIT.REPEAT_LEG)
            self.nit.headers_validate(NIT.REPEAT_HEAD)
            for c in range(6):
                self.nit.test_sort(c)
            self.nit.scroll_top()

    def test_e_retailer_drivers_tab(self):
        self.nit.retailer_drivers_tab()
        self.nit.dropdown_validate(NIT.NI_1)
        self.nit.headers_validate(NIT.RETAIL_HEAD)
        for c in range(4):
            self.nit.test_sort(c)
        self.nit.scroll_top()

    def test_f_top_items_tabs(self):
        self.nit.top_items_tab()
        self.nit.dropdown_validate(NIT.NI_1)
        self.nit.dropdown_validate(NIT.TOP_DROP[0], 1)
        for d in range(2):
            self.nit.select_dropdown(d, NIT.TOP_DROP[d], 1)
            self.nit.headers_validate(NIT.TOP_HEAD)
            for c in range(4):
                self.nit.test_sort(c)
            self.nit.scroll_top()

    def test_g_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestNewItemTrackerCG(IscE2eTestCase):
    def setUp(self):
        super(TestNewItemTrackerCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.nit = NewItemTrackerPage(self.driver)

    def test_a_nav_nit(self):
        nit = ReportTypes.NEW_ITEM_TRACKER.value
        title = ReportTypes.PREFIX_CG.value + nit
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.nit.title.text, nit + ': ' + title)

    def test_b_summary_tab(self):
        self.nit.summary_tab()
        self.nit.dropdown_validate(NIT.NI_1)
        self.nit.tree_titles_validate(NIT.TREE_TITLES)
        self.nit.download_diagram()

    def test_c_trial_repeat_tab(self):
        self.nit.trial_repeat_tab()
        self.nit.dropdown_validate(NIT.TIME_DROP[0])
        self.nit.dropdown_validate(NIT.MET_DROP[0], 1)
        for t in range(2):
            self.nit.select_dropdown(t, NIT.TIME_DROP[t])
            for m in range(7):
                self.nit.select_dropdown(m, NIT.MET_DROP[m], 1)
                self.nit.chart_legend_validate([NIT.TRIAL_LEG.format(NIT.MET_DROP[m])])
                self.nit.headers_validate(NIT.TRIAL_HEAD, form=NIT.MET_DROP[m].upper())
                for c in range(2):
                    self.nit.test_sort(c)
                self.nit.scroll_top()

    def test_d_repeat_drivers_tab(self):
        self.nit.repeat_drivers_tab()
        self.nit.dropdown_validate(NIT.REPEAT_DROP[0])
        for d in range(2):
            self.nit.select_dropdown(d, NIT.REPEAT_DROP[d])
            self.nit.legend_validate(NIT.REPEAT_LEG)
            self.nit.headers_validate(NIT.REPEAT_HEAD)
            for c in range(6):
                self.nit.test_sort(c)
            self.nit.scroll_top()

    def test_e_retailer_drivers_tab(self):
        self.nit.retailer_drivers_tab()
        self.nit.dropdown_validate(NIT.NI_1)
        self.nit.headers_validate(NIT.RETAIL_HEAD)
        for c in range(4):
            self.nit.test_sort(c)
        self.nit.scroll_top()

    def test_f_top_items_tabs(self):
        self.nit.top_items_tab()
        self.nit.dropdown_validate(NIT.NI_1)
        self.nit.dropdown_validate(NIT.TOP_DROP[0], 1)
        for d in range(2):
            self.nit.select_dropdown(d, NIT.TOP_DROP[d], 1)
            self.nit.headers_validate(NIT.TOP_HEAD)
            for c in range(4):
                self.nit.test_sort(c)
            self.nit.scroll_top()

    def test_g_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
