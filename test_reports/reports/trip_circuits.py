from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.trip_circuits import TripCircuitsPage
from constants.enums import ReportTypes
from constants.reports.trip_circuits import TC


class TestTripCircuits(IscE2eTestCase):
    def setUp(self):
        super(TestTripCircuits, self).setUp()
        self.history = HistoryPage(self.driver)
        self.tc = TripCircuitsPage(self.driver)

    def test_a_nav_tc(self):
        tc = ReportTypes.TRIP_CIRCUITS.value
        title = ReportTypes.PREFIX.value + tc
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.tc.title.text, tc + ': ' + title)

    def test_b_summary_tab(self):
        self.tc.summary_tab()
        self.tc.card_titles_validate(TC.TC_CARDS)
        self.tc.download_diagram()

    def test_c_closed_store_tab(self):
        self.tc.closed_store_tab()
        self.tc.dropdown_validate(TC.STOP_DROP[0])
        self.tc.dropdown_validate(TC.MET_DROP[0], 1)
        for d in range(2):
            self.tc.select_dropdown(d, TC.STOP_DROP[d])
            for dd in range(5):
                self.tc.select_dropdown(dd, TC.MET_DROP[dd], 1)
                self.tc.legend_validate(TC.TC_LEG, TC.MET_DROP[dd])
                self.tc.headers_validate(TC.STORE_HEAD, form=TC.MET_DROP[dd].upper())
                for c in range(5):
                    self.tc.test_sort(c)
                self.tc.scroll_top()

    def test_d_closed_prod_tab(self):
        self.tc.closed_prod_tab()
        self.tc.dropdown_validate(TC.MET_DROP[0], 1)
        for d in range(4):
            self.tc.select_dropdown(d, TC.MET_DROP[d], 1)
            self.tc.legend_validate(TC.TC_LEG, TC.MET_DROP[d])
            self.tc.headers_validate(TC.PROD_HEAD, form=TC.MET_DROP[d].upper())
            for c in range(6):
                self.tc.test_sort(c)
            self.tc.scroll_top()

    def test_e_leaked_store_tab(self):
        self.tc.leaked_store_tab()
        self.tc.dropdown_validate(TC.PROD_DROP[0])
        self.tc.dropdown_validate(TC.MET_DROP[0], 1)
        for d in range(2):
            self.tc.select_dropdown(d, TC.PROD_DROP[d])
            for dd in range(5):
                self.tc.select_dropdown(dd, TC.MET_DROP[dd], 1)
                self.tc.legend_validate(TC.TC_LEG, TC.MET_DROP[dd])
                self.tc.headers_validate(TC.STORE_HEAD, form=TC.MET_DROP[dd].upper())
                for c in range(5):
                    self.tc.test_sort(c)
                self.tc.scroll_top()

    def test_f_leaked_prod_tab(self):
        self.tc.leaked_prod_tab()
        self.tc.dropdown_validate(TC.MET_DROP[0], 1)
        for d in range(4):
            self.tc.select_dropdown(d, TC.MET_DROP[d], 1)
            self.tc.legend_validate(TC.TC_LEG, TC.MET_DROP[d])
            self.tc.headers_validate(TC.PROD_HEAD, form=TC.MET_DROP[d].upper())
            for c in range(6):
                self.tc.test_sort(c)
            self.tc.scroll_top()

    def test_g_common_circuits_tab(self):
        self.tc.common_circuits_tab()
        self.tc.dropdown_validate(TC.COMMON_DROP[0])
        for d in range(2):
            self.tc.select_dropdown(d, TC.COMMON_DROP[d])
            self.tc.headers_validate(TC.COMMON_HEAD)
            for c in range(3):
                self.tc.test_sort(c)

    def test_h_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestTripCircuitsRV(IscE2eTestCase):
    def setUp(self):
        super(TestTripCircuitsRV, self).setUp()
        self.history = HistoryPage(self.driver)
        self.tc = TripCircuitsPage(self.driver)

    def test_a_nav_tc(self):
        tc = ReportTypes.TRIP_CIRCUITS.value
        title = ReportTypes.PREFIX_RV.value + tc
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.tc.title.text, tc + ': ' + title)

    def test_b_summary_tab(self):
        self.tc.summary_tab()
        self.tc.card_titles_validate(TC.TC_CARDS)
        self.tc.download_diagram()

    def test_c_closed_store_tab(self):
        self.tc.closed_store_tab()
        self.tc.dropdown_validate(TC.STOP_DROP[0])
        self.tc.dropdown_validate(TC.MET_DROP[0], 1)
        for d in range(2):
            self.tc.select_dropdown(d, TC.STOP_DROP[d])
            for dd in range(5):
                self.tc.select_dropdown(dd, TC.MET_DROP[dd], 1)
                self.tc.legend_validate(TC.TC_LEG, TC.MET_DROP[dd])
                self.tc.headers_validate(TC.STORE_HEAD_RV, form=TC.MET_DROP[dd].upper())
                for c in range(5):
                    self.tc.test_sort(c)
                self.tc.scroll_top()

    def test_d_closed_prod_tab(self):
        self.tc.closed_prod_tab()
        self.tc.dropdown_validate(TC.MET_DROP[0], 1)
        for d in range(4):
            self.tc.select_dropdown(d, TC.MET_DROP[d], 1)
            self.tc.legend_validate(TC.TC_LEG, TC.MET_DROP[d])
            self.tc.headers_validate(TC.PROD_HEAD_RV, form=TC.MET_DROP[d].upper())
            for c in range(6):
                self.tc.test_sort(c)
            self.tc.scroll_top()

    # Skip Leaked Circuits Tabs for Retailer View

    def test_e_common_circuits_tab(self):
        self.tc.common_circuits_tab()
        self.tc.dropdown_validate(TC.COMMON_DROP[0])
        self.tc.select_dropdown(0, TC.COMMON_DROP[0])
        self.tc.headers_validate(TC.COMMON_HEAD)
        for c in range(3):
            self.tc.test_sort(c)

    def test_f_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestTripCircuitsCG(IscE2eTestCase):
    def setUp(self):
        super(TestTripCircuitsCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.tc = TripCircuitsPage(self.driver)

    def test_a_nav_tc(self):
        tc = ReportTypes.TRIP_CIRCUITS.value
        title = ReportTypes.PREFIX_CG.value + tc
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.tc.title.text, tc + ': ' + title)

    def test_b_summary_tab(self):
        self.tc.summary_tab()
        self.tc.card_titles_validate(TC.TC_CARDS)
        self.tc.download_diagram()

    def test_c_closed_store_tab(self):
        self.tc.closed_store_tab()
        self.tc.dropdown_validate(TC.STOP_DROP[0])
        self.tc.dropdown_validate(TC.MET_DROP[0], 1)
        for d in range(2):
            self.tc.select_dropdown(d, TC.STOP_DROP[d])
            for dd in range(5):
                self.tc.select_dropdown(dd, TC.MET_DROP[dd], 1)
                self.tc.legend_validate(TC.TC_LEG, TC.MET_DROP[dd])
                self.tc.headers_validate(TC.STORE_HEAD, form=TC.MET_DROP[dd].upper())
                for c in range(5):
                    self.tc.test_sort(c)
                self.tc.scroll_top()

    def test_d_closed_prod_tab(self):
        self.tc.closed_prod_tab()
        self.tc.dropdown_validate(TC.MET_DROP[0], 1)
        for d in range(4):
            self.tc.select_dropdown(d, TC.MET_DROP[d], 1)
            self.tc.legend_validate(TC.TC_LEG, TC.MET_DROP[d])
            self.tc.headers_validate(TC.PROD_HEAD_CG, form=TC.MET_DROP[d].upper())
            for c in range(6):
                self.tc.test_sort(c)
            self.tc.scroll_top()

    def test_e_leaked_store_tab(self):
        self.tc.leaked_store_tab()
        self.tc.dropdown_validate(TC.PROD_DROP[0])
        self.tc.dropdown_validate(TC.MET_DROP[0], 1)
        for d in range(2):
            self.tc.select_dropdown(d, TC.PROD_DROP[d])
            for dd in range(5):
                self.tc.select_dropdown(dd, TC.MET_DROP[dd], 1)
                self.tc.legend_validate(TC.TC_LEG, TC.MET_DROP[dd])
                self.tc.headers_validate(TC.STORE_HEAD, form=TC.MET_DROP[dd].upper())
            for c in range(5):
                self.tc.test_sort(c)
            self.tc.scroll_top()

    def test_f_leaked_prod_tab(self):
        self.tc.leaked_prod_tab()
        self.tc.dropdown_validate(TC.MET_DROP[0], 1)
        for d in range(4):
            self.tc.select_dropdown(d, TC.MET_DROP[d], 1)
            self.tc.legend_validate(TC.TC_LEG, TC.MET_DROP[d])
            self.tc.headers_validate(TC.PROD_HEAD_CG, form=TC.MET_DROP[d].upper())
            for c in range(6):
                self.tc.test_sort(c)
            self.tc.scroll_top()

    def test_g_common_circuits_tab(self):
        self.tc.common_circuits_tab()
        self.tc.dropdown_validate(TC.COMMON_DROP[0])
        for d in range(2):
            self.tc.select_dropdown(d, TC.COMMON_DROP[d])
            self.tc.headers_validate(TC.COMMON_HEAD)
            for c in range(3):
                self.tc.test_sort(c)

    def test_h_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
