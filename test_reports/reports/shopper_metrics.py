from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.shopper_metrics import ShopperMetricsPage
from constants.enums import ReportTypes
from constants.reports.shopper_metrics import SM


class TestShopperMetrics(IscE2eTestCase):
    def setUp(self):
        super(TestShopperMetrics, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sm = ShopperMetricsPage(self.driver)

    def test_a_nav_sm(self):
        sm = ReportTypes.SHOPPER_METRICS.value
        title = ReportTypes.PREFIX.value + sm
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sm.title.text, sm + ': ' + title)

    def test_b_basic_metrics(self):
        self.sm.dropdown_validate(SM.MET_DROP[0])
        for d in range(11):
            self.sm.select_dropdown(d, SM.MET_DROP[d])
            self.sm.legend_validate([SM.MET_DROP[d]])
            self.sm.headers_validate(SM.MET_HEAD)
            for c in range(7):
                self.sm.test_sort(c)
            self.sm.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestShopperMetricsRV(IscE2eTestCase):
    def setUp(self):
        super(TestShopperMetricsRV, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sm = ShopperMetricsPage(self.driver)

    def test_a_nav_sm(self):
        sm = ReportTypes.SHOPPER_METRICS.value
        title = ReportTypes.PREFIX_RV.value + sm
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sm.title.text, sm + ': ' + title)

    def test_b_basic_metrics(self):
        self.sm.dropdown_validate(SM.MET_DROP_RV[0])
        for d in range(10):
            self.sm.select_dropdown(d, SM.MET_DROP_RV[d])
            self.sm.legend_validate([SM.MET_DROP_RV[d]])
            self.sm.headers_validate(SM.MET_HEAD_RV)
            for c in range(7):
                self.sm.test_sort(c)
            self.sm.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestShopperMetricsCG(IscE2eTestCase):
    def setUp(self):
        super(TestShopperMetricsCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sm = ShopperMetricsPage(self.driver)

    def test_a_nav_sm(self):
        sm = ReportTypes.SHOPPER_METRICS.value
        title = ReportTypes.PREFIX_CG.value + sm
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sm.title.text, sm + ': ' + title)

    def test_b_basic_metrics(self):
        self.sm.dropdown_validate(SM.MET_DROP[0])
        for d in range(11):
            self.sm.select_dropdown(d, SM.MET_DROP[d])
            self.sm.legend_validate([SM.MET_DROP[d]])
            self.sm.headers_validate(SM.MET_HEAD)
            for c in range(7):
                self.sm.test_sort(c)
            self.sm.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
