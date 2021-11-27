from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.leakage_tree import LeakageTreePage
from constants.enums import ReportTypes
from constants.reports.leakage_tree import LT


class TestLeakageTree(IscE2eTestCase):
    def setUp(self):
        super(TestLeakageTree, self).setUp()
        self.history = HistoryPage(self.driver)
        self.lt = LeakageTreePage(self.driver)

    def test_a_nav_lt(self):
        lt = ReportTypes.LEAKAGE_TREE.value
        title = ReportTypes.PREFIX.value + lt
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.lt.title.text, lt + ': ' + title)

    def test_b_tree_tab(self):
        self.lt.tree_tab()
        self.lt.tree_titles_validate(LT.TREE_TITLES)
        self.lt.download_diagram()

    def test_c_shopped_tab(self):
        self.lt.shopped_tab()
        self.lt.dropdown_validate(LT.STORE_SHOP_DROP[0], 0)
        self.lt.dropdown_validate(LT.METRIC_DROP[0], 1)
        for d in range(2):
            self.lt.select_dropdown(d, LT.STORE_SHOP_DROP[d])
            for dd in range(7):
                self.lt.select_dropdown(dd, LT.METRIC_DROP[dd], 1)
                self.lt.legend_validate([LT.METRIC_DROP[dd]])
                if dd < 3:
                    self.lt.headers_validate(LT.SHOPPER_STATIC_HEAD[dd], form=LT.SHOPPER_HEAD[dd])
                else:
                    self.lt.headers_validate(LT.SHOPPER_STATIC_HEAD[0], form=LT.SHOPPER_HEAD[dd])
                for c in range(4):
                    self.lt.test_sort(c)
                self.lt.scroll_top()

    def test_d_products_tab(self):
        self.lt.top_prod_tab()
        self.lt.dropdown_validate(LT.PROD_SHOP_DROP[0], 0)
        self.lt.dropdown_validate(LT.PROD_LEV_DROP[0], 2)
        for d in range(2):
            self.lt.select_dropdown(d, LT.PROD_SHOP_DROP[d])
            for dd in range(3):
                self.lt.select_dropdown(dd, LT.PROD_LEV_DROP[dd], 2)
                self.lt.headers_validate(LT.PROD_HEAD)
                for c in range(5):
                    self.lt.test_sort(c)
                self.lt.scroll_top()

    def test_e_benchmark_tab(self):
        self.lt.benchmark_tab()
        self.lt.headers_validate(LT.BENCH_HEAD)
        for c in range(6):
            self.lt.test_sort(c)
        self.lt.scroll_top()

    def test_f_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestLeakageTreeRV(IscE2eTestCase):
    def setUp(self):
        super(TestLeakageTreeRV, self).setUp()
        self.history = HistoryPage(self.driver)
        self.lt = LeakageTreePage(self.driver)

    def test_a_nav_lt(self):
        lt = ReportTypes.LEAKAGE_TREE.value
        title = ReportTypes.PREFIX_RV.value + lt
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.lt.title.text, lt + ': ' + title)

    def test_b_tree_tab(self):
        self.lt.tree_tab()
        self.lt.tree_titles_validate(LT.TREE_TITLES_RV)
        self.lt.download_diagram()

    def test_c_shopped_tab(self):
        self.lt.shopped_tab()
        self.lt.dropdown_validate(LT.STORE_SHOP_DROP[0], 0)
        self.lt.dropdown_validate(LT.METRIC_DROP_RV[0], 1)
        for d in range(2):
            self.lt.select_dropdown(d, LT.STORE_SHOP_DROP[d])
            for dd in range(6):
                self.lt.select_dropdown(dd, LT.METRIC_DROP_RV[dd], 1)
                self.lt.legend_validate([LT.METRIC_DROP_RV[dd]])
                if dd < 3:
                    self.lt.headers_validate(LT.SHOPPER_STATIC_HEAD[dd], form=LT.SHOPPER_HEAD_RV[dd])
                else:
                    self.lt.headers_validate(LT.SHOPPER_STATIC_HEAD[0], form=LT.SHOPPER_HEAD_RV[dd])
                for c in range(4):
                    self.lt.test_sort(c)
                self.lt.scroll_top()

    def test_d_products_tab(self):
        self.lt.top_prod_tab()
        self.lt.dropdown_validate(LT.PROD_SHOP_DROP_RV[0], 0)
        self.lt.dropdown_validate(LT.PROD_LEV_DROP_RV[0], 2)
        for s in range(2):
            self.lt.select_dropdown(s, LT.PROD_SHOP_DROP_RV[s])
            self.lt.headers_validate(LT.PROD_HEAD_RV)
            for c in range(4):
                self.lt.test_sort(c)
            self.lt.scroll_top()

    def test_e_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestLeakageTreeCG(IscE2eTestCase):
    def setUp(self):
        super(TestLeakageTreeCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.lt = LeakageTreePage(self.driver)

    def test_a_nav_lt(self):
        lt = ReportTypes.LEAKAGE_TREE.value
        title = ReportTypes.PREFIX_CG.value + lt
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.lt.title.text, lt + ': ' + title)

    def test_b_tree_tab(self):
        self.lt.tree_tab()
        self.lt.tree_titles_validate(LT.TREE_TITLES_CG)
        self.lt.download_diagram()

    def test_c_shopped_tab(self):
        self.lt.shopped_tab()
        self.lt.dropdown_validate(LT.STORE_SHOP_DROP[0], 0)
        self.lt.dropdown_validate(LT.METRIC_DROP[0], 1)
        for d in range(2):
            self.lt.select_dropdown(d, LT.STORE_SHOP_DROP[d])
            for dd in range(7):
                self.lt.select_dropdown(dd, LT.METRIC_DROP[dd], 1)
                self.lt.legend_validate([LT.METRIC_DROP[dd]])
                if dd < 3:
                    self.lt.headers_validate(LT.SHOPPER_STATIC_HEAD[dd], form=LT.SHOPPER_HEAD[dd])
                else:
                    self.lt.headers_validate(LT.SHOPPER_STATIC_HEAD[0], form=LT.SHOPPER_HEAD[dd])
                for c in range(4):
                    self.lt.test_sort(c)
                self.lt.scroll_top()

    def test_d_products_tab(self):
        self.lt.top_prod_tab()
        self.lt.dropdown_validate(LT.PROD_SHOP_DROP[0], 0)
        self.lt.dropdown_validate(LT.PROD_LEV_DROP[0], 2)
        for d in range(2):
            self.lt.select_dropdown(d, LT.PROD_SHOP_DROP[d])
            for dd in range(3):
                self.lt.select_dropdown(dd, LT.PROD_LEV_DROP[dd], 2)
                self.lt.headers_validate(LT.PROD_HEAD)
                for c in range(5):
                    self.lt.test_sort(c)
                self.lt.scroll_top()

    def test_e_benchmark_tab(self):
        self.lt.benchmark_tab()
        self.lt.headers_validate(LT.BENCH_HEAD)
        for c in range(6):
            self.lt.test_sort(c)
        self.lt.scroll_top()

    def test_f_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
