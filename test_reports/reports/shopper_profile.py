from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.shopper_profile import ShopperProfilePage
from constants.enums import ReportTypes
from constants.reports.shopper_profile import SP


class TestShopperProfile(IscE2eTestCase):
    def setUp(self):
        super(TestShopperProfile, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sp = ShopperProfilePage(self.driver)

    def test_a_nav_sp(self):
        sp = ReportTypes.SHOPPER_PROFILE.value
        title = ReportTypes.PREFIX.value + sp
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sp.title.text, sp + ': ' + title)

    def test_b_demo_tab(self):
        self.sp.demo_tab()
        for d in range(6):
            self.sp.select_dropdown(d, SP.DEMO_DROP[d])
            self.sp.table_validate(1, SP.DEMO_TABLE[d])
            for t, tab in enumerate(self.sp.tables()):
                self.sp.headers_validate(SP.DEMO_STATIC_HEAD, SP.DEMO_HEAD[d][t], table_idx=t)
                self.sp.copy_table_validate(t)
                for c in range(1, 4):
                    self.sp.test_sort(c, table_idx=t)
            self.sp.scroll_top()

    def test_c_metrics_tab(self):
        self.sp.basic_mets_tab()
        self.sp.headers_validate(SP.METRIC_HEAD)
        self.sp.table_validate(1, SP.METRIC_TABLE)
        self.sp.copy_table_validate()
        self.sp.test_sort(3)

    def test_d_top_stores_tab(self):
        self.sp.top_stores_tab()
        for d in range(3):
            self.sp.select_dropdown(d, SP.STORES_DROP[d])
            for t in range(2):
                self.sp.toggle_buttons[t].click()
                self.sp.legend_validate(SP.STORES_LEG[t])
                self.sp.headers_validate(SP.STORES_HEAD[t])
                self.sp.copy_table_validate()
                for c in range(4):
                    self.sp.test_sort(c)
                self.sp.scroll_top()

    def test_e_payment_tab(self):
        self.sp.payment_tab()
        for d in range(5):
            self.sp.select_dropdown(d, SP.PAY_DROP[d])
            for t in range(2):
                self.sp.toggle_buttons[t].click()
                self.sp.legend_validate(SP.PAY_LEG[t])
                self.sp.headers_validate(SP.PAY_HEAD)
                self.sp.table_unordered_validate(1, SP.PAY_TABLE)
                self.sp.copy_table_validate()
                for c in range(1, 4):
                    self.sp.test_sort(c)
                self.sp.scroll_top()

    def test_f_timing_tab(self):
        self.sp.timing_tab()
        for d in range(5):
            self.sp.select_dropdown(d, SP.TIME_DROP[d])
            for t in range(2):
                self.sp.toggle_buttons[t].click()
                self.sp.legend_validate(SP.TIME_LEG[t])
                self.sp.headers_validate(SP.TIME_STATIC_HEAD, SP.TIME_HEAD[d])
                self.sp.table_validate(1, SP.TIME_TABLE[d])
                self.sp.copy_table_validate()
                for c in range(7):
                    self.sp.test_sort(c)
                self.sp.scroll_top()

    def test_g_trip_type_tab(self):
        self.sp.trip_type_tab()
        self.sp.dropdown_validate(SP.TRIP_DROP[0])
        for d in range(2):
            self.sp.select_dropdown(d, SP.TRIP_DROP[d])
            for t in range(2):
                self.sp.toggle_buttons[t].click()
                self.sp.legend_validate(SP.TRIP_LEG[t])
                self.sp.headers_validate(SP.TRIP_HEAD[d])
                self.sp.table_validate(1, SP.TRIP_TABLE)
                self.sp.copy_table_validate()
                for c in range(1, 4):
                    self.sp.test_sort(c)
                self.sp.scroll_top()

    def test_h_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestShopperProfileCG(IscE2eTestCase):
    def setUp(self):
        super(TestShopperProfileCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sp = ShopperProfilePage(self.driver)

    def test_a_nav_sp(self):
        sp = ReportTypes.SHOPPER_PROFILE.value
        title = ReportTypes.PREFIX_CG.value + sp
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sp.title.text, sp + ': ' + title)

    def test_b_demo_tab(self):
        self.sp.demo_tab()
        for d in range(6):
            self.sp.select_dropdown(d, SP.DEMO_DROP[d])
            self.sp.table_validate(1, SP.DEMO_TABLE[d])
            for t, tab in enumerate(self.sp.tables()):
                self.sp.headers_validate(SP.DEMO_STATIC_HEAD, SP.DEMO_HEAD[d][t], table_idx=t)
                self.sp.copy_table_validate(t)
                for c in range(1, 4):
                    self.sp.test_sort(c, table_idx=t)
            self.sp.scroll_top()

    def test_c_metrics_tab(self):
        self.sp.basic_mets_tab()
        self.sp.headers_validate(SP.METRIC_HEAD)
        self.sp.table_validate(1, SP.METRIC_TABLE)
        self.sp.copy_table_validate()
        self.sp.test_sort(3)

    def test_d_top_stores_tab(self):
        self.sp.top_stores_tab()
        for d in range(3):
            self.sp.select_dropdown(d, SP.STORES_DROP[d])
            for t in range(2):
                self.sp.toggle_buttons[t].click()
                self.sp.legend_validate(SP.STORES_LEG[t])
                self.sp.headers_validate(SP.STORES_HEAD[t])
                self.sp.copy_table_validate()
                for c in range(4):
                    self.sp.test_sort(c)
                self.sp.scroll_top()

    def test_e_payment_tab(self):
        self.sp.payment_tab()
        for d in range(5):
            self.sp.select_dropdown(d, SP.PAY_DROP[d])
            for t in range(2):
                self.sp.toggle_buttons[t].click()
                self.sp.legend_validate(SP.PAY_LEG[t])
                self.sp.headers_validate(SP.PAY_HEAD)
                self.sp.table_unordered_validate(1, SP.PAY_TABLE)
                self.sp.copy_table_validate()
                for c in range(1, 4):
                    self.sp.test_sort(c)
                self.sp.scroll_top()

    def test_f_timing_tab(self):
        self.sp.timing_tab()
        for d in range(5):
            self.sp.select_dropdown(d, SP.TIME_DROP[d])
            for t in range(2):
                self.sp.toggle_buttons[t].click()
                self.sp.legend_validate(SP.TIME_LEG[t])
                self.sp.headers_validate(SP.TIME_STATIC_HEAD, SP.TIME_HEAD[d])
                self.sp.table_validate(1, SP.TIME_TABLE[d])
                self.sp.copy_table_validate()
                for c in range(7):
                    self.sp.test_sort(c)
                self.sp.scroll_top()

    def test_g_trip_type_tab(self):
        self.sp.trip_type_tab()
        self.sp.dropdown_validate(SP.TRIP_DROP[0])
        for d in range(2):
            self.sp.select_dropdown(d, SP.TRIP_DROP[d])
            for t in range(2):
                self.sp.toggle_buttons[t].click()
                self.sp.legend_validate(SP.TRIP_LEG[t])
                self.sp.headers_validate(SP.TRIP_HEAD[d])
                self.sp.table_validate(1, SP.TRIP_TABLE)
                self.sp.copy_table_validate()
                for c in range(1, 4):
                    self.sp.test_sort(c)
                self.sp.scroll_top()

    def test_h_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
