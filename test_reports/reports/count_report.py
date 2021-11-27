from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.count_report import CountReportPage
from constants.enums import ReportTypes
from constants.reports.count_report import CR


class TestCountReport(IscE2eTestCase):
    def setUp(self):
        super(TestCountReport, self).setUp()
        self.history = HistoryPage(self.driver)
        self.cr = CountReportPage(self.driver)

    def test_a_nav_cr(self):
        cr = ReportTypes.COUNT_REPORT.value
        title = ReportTypes.PREFIX.value + cr
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.cr.title.text, cr + ': ' + title)

    def test_b_cr_tab(self):
        self.cr.dropdown_validate(CR.PROJ_DROP[0])
        self.cr.dropdown_validate(CR.MET_DROP[0], 1)
        for d in range(3):
            self.cr.select_dropdown(d, CR.MET_DROP[d], 1)
            self.cr.headers_validate(CR.CR_HEAD, form=CR.CR_FORM[d])
            for c in range(7):
                self.cr.test_sort(c)

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestCountReportCG(IscE2eTestCase):
    def setUp(self):
        super(TestCountReportCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.cr = CountReportPage(self.driver)

    def test_a_nav_cr(self):
        cr = ReportTypes.COUNT_REPORT.value
        title = ReportTypes.PREFIX_CG.value + cr
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.cr.title.text, cr + ': ' + title)

    def test_b_cr_tab(self):
        self.cr.dropdown_validate(CR.PROJ_DROP[0])
        self.cr.dropdown_validate(CR.MET_DROP[0], 1)
        for d in range(3):
            self.cr.select_dropdown(d, CR.MET_DROP[d], 1)
            self.cr.headers_validate(CR.CR_HEAD, form=CR.CR_FORM[d])
            for c in range(7):
                self.cr.test_sort(c)

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
