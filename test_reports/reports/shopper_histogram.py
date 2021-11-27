from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.shopper_histogram import ShopperHistogramPage
from constants.enums import ReportTypes
from constants.reports.shopper_histogram import SH


class TestShopperHistogram(IscE2eTestCase):
    def setUp(self):
        super(TestShopperHistogram, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sh = ShopperHistogramPage(self.driver)

    def test_a_nav_sh(self):
        sh = ReportTypes.SHOPPER_HISTOGRAM.value
        title = ReportTypes.PREFIX.value + sh
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sh.title.text, sh + ': ' + title)

    def test_b_sh(self):
        self.sh.dropdown_validate(SH.MET_DROP[0])
        for d in range(9):
            self.sh.select_dropdown(d, SH.MET_DROP[d])
            if d < 6:
                self.sh.headers_validate(SH.STATIC_HEAD[0], SH.MET_DROP[d].upper())
                self.sh.copy_table_validate()
            else:
                self.sh.headers_validate(SH.STATIC_HEAD[1], SH.MET_DROP[d].upper())
                self.sh.copy_table_validate()
            for c in range(4):
                self.sh.test_sort(c)
            self.sh.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestShopperHistogramRV(IscE2eTestCase):
    def setUp(self):
        super(TestShopperHistogramRV, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sh = ShopperHistogramPage(self.driver)

    def test_a_nav_sh(self):
        sh = ReportTypes.SHOPPER_HISTOGRAM.value
        title = ReportTypes.PREFIX_RV.value + sh
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sh.title.text, sh + ': ' + title)

    def test_b_sh(self):
        self.sh.dropdown_validate(SH.MET_DROP_RV[0])
        for d in range(7):
            self.sh.select_dropdown(d, SH.MET_DROP_RV[d])
            if d < 5:
                self.sh.headers_validate(SH.STATIC_HEAD[0], SH.MET_DROP_RV[d].upper(), 0)
            else:
                self.sh.headers_validate(SH.STATIC_HEAD[1], SH.MET_DROP_RV[d].upper(), 0)
            for c in range(4):
                self.sh.test_sort(c)
            self.sh.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestShopperHistogramCG(IscE2eTestCase):
    def setUp(self):
        super(TestShopperHistogramCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sh = ShopperHistogramPage(self.driver)

    def test_a_nav_sh(self):
        sh = ReportTypes.SHOPPER_HISTOGRAM.value
        title = ReportTypes.PREFIX_CG.value + sh
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sh.title.text, sh + ': ' + title)

    def test_b_sh(self):
        self.sh.dropdown_validate(SH.MET_DROP[0])
        for d in range(9):
            self.sh.select_dropdown(d, SH.MET_DROP[d])
            if d < 6:
                self.sh.headers_validate(SH.STATIC_HEAD[0], SH.MET_DROP[d].upper())
                self.sh.copy_table_validate()
            else:
                self.sh.headers_validate(SH.STATIC_HEAD[1], SH.MET_DROP[d].upper())
                self.sh.copy_table_validate()
            for c in range(4):
                self.sh.test_sort(c)
            self.sh.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
