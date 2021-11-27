from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.trended_metrics import TrendedMetricsPage
from constants.enums import ReportTypes
from constants.reports.trended_metrics import TM


class TestTrendedMetrics(IscE2eTestCase):
    def setUp(self):
        super(TestTrendedMetrics, self).setUp()
        self.history = HistoryPage(self.driver)
        self.tm = TrendedMetricsPage(self.driver)

    def test_a_nav_tm(self):
        tm = ReportTypes.TRENDED_METRICS.value
        title = ReportTypes.PREFIX.value + tm
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.tm.title.text, tm + ': ' + title)

    def test_b_tm_tab(self):
        self.tm.dropdown_validate(TM.TM_DROP[0])
        for d in range(5):
            self.tm.select_dropdown(d, TM.TM_DROP[d])
            self.tm.assertEqual(self.tm.headers()[0].text, TM.TM_HEAD[0])

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestTrendedMetricsCG(IscE2eTestCase):
    def setUp(self):
        super(TestTrendedMetricsCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.tm = TrendedMetricsPage(self.driver)

    def test_a_nav_tm(self):
        tm = ReportTypes.TRENDED_METRICS.value
        title = ReportTypes.PREFIX_CG.value + tm
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.tm.title.text, tm + ': ' + title)

    def test_b_tm_tab(self):
        self.tm.dropdown_validate(TM.TM_DROP[0])
        for d in range(5):
            self.tm.select_dropdown(d, TM.TM_DROP[d])
            self.tm.assertEqual(self.tm.headers()[0].text, TM.TM_HEAD[0])

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
