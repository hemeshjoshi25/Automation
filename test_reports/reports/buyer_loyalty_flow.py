from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.buyer_loyalty_flow import BuyerLoyaltyFlowPage
from constants.enums import ReportTypes
from constants.reports.buyer_loyalty_flow import BLF


class TestBuyerLoyaltyFlow(IscE2eTestCase):
    def setUp(self):
        super(TestBuyerLoyaltyFlow, self).setUp()
        self.history = HistoryPage(self.driver)
        self.blf = BuyerLoyaltyFlowPage(self.driver)

    def test_a_nav_blf(self):
        blf = ReportTypes.BUYER_LOYALTY_FLOW.value
        title = ReportTypes.PREFIX.value + blf
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.blf.title.text, blf + ': ' + title)

    def test_b_summary_tab(self):
        self.blf.summary_tab()
        self.blf.dropdown_validate(BLF.BUY_DROP[0])
        self.blf.dropdown_validate(BLF.MET_DROP[0], 2)
        for d in range(4):
            self.blf.select_dropdown(d, BLF.BUY_DROP[d])
            for dd in range(5):
                self.blf.select_dropdown(dd, BLF.MET_DROP[dd], 2)
                self.blf.highcharts_legend_validate(BLF.BLF_LEG)
                self.blf.headers_validate(BLF.SUM_HEAD, form=BLF.SUM_HEAD_FORM[dd].upper())
                self.blf.copy_table_validate()
                for c in range(6):
                    self.blf.test_sort(c)
                self.blf.scroll_top()

    def test_c_loyalty_tab(self):
        self.blf.loyalty_tab()
        self.blf.dropdown_validate(BLF.MET_DROP[0], 1)
        for d in range(5):
            self.blf.select_dropdown(d, BLF.MET_DROP[d], 1)
            self.blf.highcharts_legend_validate(BLF.LOYAL_LEG)
            self.blf.headers_validate(BLF.LOYAL_HEAD, form=BLF.FORM_HEAD[d].upper())
            self.blf.copy_table_validate()
            for c in range(9):
                self.blf.test_sort(c)
            self.blf.scroll_top()

    def test_d_comparison_tab(self):
        self.blf.comp_tab()
        self.blf.dropdown_validate(BLF.BUY_DROP[0])
        for d in range(4):
            self.blf.select_dropdown(d, BLF.BUY_DROP[d])
            self.blf.legend_validate(BLF.BLF_LEG)
            self.blf.headers_validate(BLF.COMP_HEAD)
            self.blf.copy_table_validate()
            for c in range(16):
                self.blf.test_sort(c)
            self.blf.scroll_top()

    def test_e_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestBuyerLoyaltyFlowCG(IscE2eTestCase):
    def setUp(self):
        super(TestBuyerLoyaltyFlowCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.blf = BuyerLoyaltyFlowPage(self.driver)

    def test_a_nav_blf(self):
        blf = ReportTypes.BUYER_LOYALTY_FLOW.value
        title = ReportTypes.PREFIX_CG.value + blf
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.blf.title.text, blf + ': ' + title)

    def test_b_summary_tab(self):
        self.blf.summary_tab()
        self.blf.dropdown_validate(BLF.BUY_DROP[0])
        self.blf.dropdown_validate(BLF.MET_DROP[0], 2)
        for d in range(4):
            self.blf.select_dropdown(d, BLF.BUY_DROP[d])
            for dd in range(5):
                self.blf.select_dropdown(dd, BLF.MET_DROP[dd], 2)
                self.blf.highcharts_legend_validate(BLF.BLF_LEG)
                self.blf.headers_validate(BLF.SUM_HEAD, form=BLF.SUM_HEAD_FORM[dd].upper())
                self.blf.copy_table_validate()
                for c in range(6):
                    self.blf.test_sort(c)
                self.blf.scroll_top()

    def test_c_loyalty_tab(self):
        self.blf.loyalty_tab()
        self.blf.dropdown_validate(BLF.MET_DROP[0], 1)
        for d in range(5):
            self.blf.select_dropdown(d, BLF.MET_DROP[d], 1)
            self.blf.highcharts_legend_validate(BLF.LOYAL_LEG)
            self.blf.headers_validate(BLF.LOYAL_HEAD, form=BLF.FORM_HEAD[d].upper())
            self.blf.copy_table_validate()
            for c in range(9):
                self.blf.test_sort(c)
            self.blf.scroll_top()

    def test_d_comparison_tab(self):
        self.blf.comp_tab()
        self.blf.dropdown_validate(BLF.BUY_DROP[0])
        for d in range(4):
            self.blf.select_dropdown(d, BLF.BUY_DROP[d])
            self.blf.legend_validate(BLF.BLF_LEG)
            self.blf.headers_validate(BLF.COMP_HEAD)
            # self.blf.copy_table_validate()
            for c in range(16):
                self.blf.test_sort(c)
            self.blf.scroll_top()

    def test_e_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
