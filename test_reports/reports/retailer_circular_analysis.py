from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.retailer_circular_analysis import RetailerCircularAnalysisPage
from constants.enums import ReportTypes
from constants.reports.retailer_circular_analysis import RCA


class TestRetailerCircularAnalysis(IscE2eTestCase):
    def setUp(self):
        super(TestRetailerCircularAnalysis, self).setUp()
        self.history = HistoryPage(self.driver)
        self.rca = RetailerCircularAnalysisPage(self.driver)

    def test_a_nav_rca(self):
        rca = ReportTypes.RETAILER_CIRCULAR_ANALYSIS.value
        title = ReportTypes.PREFIX.value + rca
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.rca.title.text, rca + ': ' + title)

    def test_b_rca(self):
        self.rca.dropdown_validate(RCA.MET_DROP[0])
        for d in range(22):
            self.rca.select_dropdown(d, RCA.MET_DROP[d])
            self.rca.headers_validate(RCA.RCA_HEAD)
            for c in range(8):
                self.rca.test_sort(c)

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
