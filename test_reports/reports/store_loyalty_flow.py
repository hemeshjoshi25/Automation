from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.store_loyalty_flow import StoreLoyaltyFlowPage
from constants.enums import ReportTypes
from constants.reports.store_loyalty_flow import SLF


class TestStoreLoyaltyFlow(IscE2eTestCase):
    def setUp(self):
        super(TestStoreLoyaltyFlow, self).setUp()
        self.history = HistoryPage(self.driver)
        self.slf = StoreLoyaltyFlowPage(self.driver)

    def test_a_nav_slf(self):
        slf = ReportTypes.STORE_LOYALTY_FLOW.value
        title = ReportTypes.PREFIX.value + slf
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.slf.title.text, slf + ': ' + title)

    def test_b_summary_tab(self):
        self.slf.summary_tab()
        self.slf.dropdown_validate(SLF.BUY_SEG_DROP[0])
        self.slf.dropdown_validate(SLF.MET_DROP[0], 1)
        for d in range(2):
            self.slf.select_dropdown(d, SLF.BUY_SEG_DROP[d])
            self.slf.highcharts_legend_validate(SLF.SUM_LEG[d])
            for dd in range(4):
                self.slf.select_dropdown(dd, SLF.MET_DROP[dd], 1)
                self.slf.headers_validate(SLF.SUM_HEAD, form=SLF.MET_DROP[dd].upper())
                self.slf.copy_table_validate()
                for c in range(6):
                    self.slf.test_sort(c)
                self.slf.scroll_top()

    def test_c_benchmarks_tab(self):
        self.slf.benchmarks_tab()
        self.slf.dropdown_validate(SLF.BUY_SEG_DROP[0])
        self.slf.dropdown_validate(SLF.BENCH_DROP[0], 1)
        for d in range(2):
            self.slf.select_dropdown(d, SLF.BUY_SEG_DROP[d])
            for dd in range(4):
                self.slf.select_dropdown(dd, SLF.BENCH_DROP[dd], 1)
                self.slf.legend_validate(SLF.BENCH_LEG, SLF.BENCH_FORM[dd])
                self.slf.headers_validate(SLF.BENCH_HEAD, form=SLF.BENCH_FORM[dd].upper())
                for c in range(7):
                    self.slf.test_sort(c)
                self.slf.scroll_top()

    def test_d_store_pref_tab(self):
        self.slf.store_pref_tab()
        self.slf.dropdown_validate(SLF.STORE_DROP[0])
        for d in range(5):
            self.slf.select_dropdown(d, SLF.STORE_DROP[d])
            self.slf.legend_validate(SLF.STORE_LEG)
            self.slf.headers_validate(SLF.STORE_HEAD)
            self.slf.copy_table_validate()
            for c in range(5):
                self.slf.test_sort(c)
            self.slf.scroll_top()

    def test_e_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestStoreLoyaltyFlowCG(IscE2eTestCase):
    def setUp(self):
        super(TestStoreLoyaltyFlowCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.slf = StoreLoyaltyFlowPage(self.driver)

    def test_a_nav_slf(self):
        slf = ReportTypes.STORE_LOYALTY_FLOW.value
        title = ReportTypes.PREFIX_CG.value + slf
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.slf.title.text, slf + ': ' + title)

    def test_b_summary_tab(self):
        self.slf.summary_tab()
        self.slf.dropdown_validate(SLF.BUY_SEG_DROP[0])
        self.slf.dropdown_validate(SLF.MET_DROP[0], 1)
        for d in range(2):
            self.slf.select_dropdown(d, SLF.BUY_SEG_DROP[d])
            self.slf.highcharts_legend_validate(SLF.SUM_LEG[d])
            for dd in range(4):
                self.slf.select_dropdown(dd, SLF.MET_DROP[dd], 1)
                self.slf.headers_validate(SLF.SUM_HEAD, form=SLF.MET_DROP[dd].upper())
                self.slf.copy_table_validate()
                for c in range(6):
                    self.slf.test_sort(c)
                self.slf.scroll_top()

    def test_c_benchmarks_tab(self):
        self.slf.benchmarks_tab()
        self.slf.dropdown_validate(SLF.BUY_SEG_DROP[0])
        self.slf.dropdown_validate(SLF.BENCH_DROP[0], 1)
        for d in range(2):
            self.slf.select_dropdown(d, SLF.BUY_SEG_DROP[d])
            for dd in range(4):
                self.slf.select_dropdown(dd, SLF.BENCH_DROP[dd], 1)
                self.slf.legend_validate(SLF.BENCH_LEG, SLF.BENCH_FORM[dd])
                self.slf.headers_validate(SLF.BENCH_HEAD, form=SLF.BENCH_FORM[dd].upper())
                for c in range(7):
                    self.slf.test_sort(c)
                self.slf.scroll_top()

    def test_d_store_pref_tab(self):
        self.slf.store_pref_tab()
        self.slf.dropdown_validate(SLF.STORE_DROP[0])
        for d in range(5):
            self.slf.select_dropdown(d, SLF.STORE_DROP[d])
            self.slf.legend_validate(SLF.STORE_LEG)
            self.slf.headers_validate(SLF.STORE_HEAD)
            self.slf.copy_table_validate()
            for c in range(5):
                self.slf.test_sort(c)
            self.slf.scroll_top()

    def test_e_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
