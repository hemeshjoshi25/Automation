from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.cross_purchase import CrossPurchasePage
from constants.enums import ReportTypes
from constants.reports.cross_purchase import CP


class TestCrossPurchase(IscE2eTestCase):
    def setUp(self):
        super(TestCrossPurchase, self).setUp()
        self.history = HistoryPage(self.driver)
        self.cp = CrossPurchasePage(self.driver)

    def test_a_nav_cp(self):
        cp = ReportTypes.CROSS_PURCHASE.value
        title = ReportTypes.PREFIX.value + cp
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.cp.title.text, cp + ': ' + title)

    def test_b_buyer_overlap_tab(self):
        self.cp.buyer_overlap_tab()
        self.cp.dropdown_validate(CP.BUY_MET_DROP[0], 2)
        for d in range(3):
            self.cp.select_dropdown(d, CP.BUY_MET_DROP[d], 2)
            self.cp.legend_validate(CP.BUY_LEG, self.cp.dropdown_selectors(0).text)
            self.cp.headers_validate(CP.BUY_HEAD, CP.BUY_MET_DROP[d].upper(), 1)
            self.cp.copy_table_validate()
            for c in range(6):
                self.cp.test_sort(c)
            self.cp.scroll_top()

    def test_c_product_matrix(self):
        self.cp.prod_matrix_tab()
        self.cp.dropdown_validate(CP.PROD_MET_DROP[0])
        for d in range(10):
            self.cp.select_dropdown(d, CP.PROD_MET_DROP[d])
            self.cp.assertEqual(self.cp.headers()[0].text, CP.PROD_HEAD)
            self.cp.table_validate(1, CP.PROD_TABLE)
            self.cp.copy_table_validate()

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestCrossPurchaseCG(IscE2eTestCase):
    def setUp(self):
        super(TestCrossPurchaseCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.cp = CrossPurchasePage(self.driver)

    def test_a_nav_cp(self):
        cp = ReportTypes.CROSS_PURCHASE.value
        title = ReportTypes.PREFIX_CG.value + cp
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.cp.title.text, cp + ': ' + title)

    def test_b_buyer_overlap_tab(self):
        self.cp.buyer_overlap_tab()
        self.cp.dropdown_validate(CP.BUY_MET_DROP[0], 2)
        for d in range(3):
            self.cp.select_dropdown(d, CP.BUY_MET_DROP[d], 2)
            self.cp.legend_validate(CP.BUY_LEG, self.cp.dropdown_selectors(0).text)
            self.cp.headers_validate(CP.BUY_HEAD, CP.BUY_MET_DROP[d].upper(), 1)
            self.cp.copy_table_validate()
            for c in range(6):
                self.cp.test_sort(c)
            self.cp.scroll_top()

    def test_c_product_matrix(self):
        self.cp.prod_matrix_tab()
        self.cp.dropdown_validate(CP.PROD_MET_DROP[0])
        for d in range(10):
            self.cp.select_dropdown(d, CP.PROD_MET_DROP[d])
            self.cp.assertEqual(self.cp.headers()[0].text, CP.PROD_HEAD)
            self.cp.table_validate(1, CP.PROD_TABLE)
            self.cp.copy_table_validate()

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
