from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.retailer_share_wallet import RetailerShareWalletPage
from constants.enums import ReportTypes
from constants.reports.retailer_share_wallet import RSOW


class TestRetailerShareWallet(IscE2eTestCase):
    def setUp(self):
        super(TestRetailerShareWallet, self).setUp()
        self.history = HistoryPage(self.driver)
        self.rsow = RetailerShareWalletPage(self.driver)

    def test_a_nav_rsow(self):
        rsow = ReportTypes.RETAILER_SHARE_WALLET.value
        title = ReportTypes.PREFIX.value + rsow
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.rsow.title.text, rsow + ': ' + title)

    def test_b_cat_tab(self):
        self.rsow.cat_tab()
        self.rsow.dropdown_validate(RSOW.RSOW_DROP[0])
        for d in range(5):
            self.rsow.select_dropdown(d, RSOW.RSOW_DROP[d])
            self.rsow.legend_validate([RSOW.RSOW_DROP[d]])
            self.rsow.headers_validate(RSOW.CAT_HEAD[d])
            self.rsow.copy_table_validate()
            for c in range(6):
                self.rsow.test_sort(c)
            self.rsow.scroll_top()

    def test_c_comp_tab(self):
        self.rsow.comp_tab()
        self.rsow.dropdown_validate(RSOW.RSOW_DROP[0], 1)
        for d in range(5):
            self.rsow.select_dropdown(d, RSOW.RSOW_DROP[d], 1)
            self.rsow.legend_validate([RSOW.RSOW_DROP[d]])
            self.rsow.headers_validate(RSOW.COMP_HEAD[d])
            self.rsow.copy_table_validate()
            for c in range(5):
                self.rsow.test_sort(c)
            self.rsow.scroll_top()

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestRetailerShareWalletCG(IscE2eTestCase):
    def setUp(self):
        super(TestRetailerShareWalletCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.rsow = RetailerShareWalletPage(self.driver)

    def test_a_nav_rsow(self):
        rsow = ReportTypes.RETAILER_SHARE_WALLET.value
        title = ReportTypes.PREFIX_CG.value + rsow
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.rsow.title.text, rsow + ': ' + title)

    def test_b_cat_tab(self):
        self.rsow.cat_tab()
        self.rsow.dropdown_validate(RSOW.RSOW_DROP[0])
        for d in range(5):
            self.rsow.select_dropdown(d, RSOW.RSOW_DROP[d])
            self.rsow.legend_validate([RSOW.RSOW_DROP[d]])
            self.rsow.headers_validate(RSOW.CAT_HEAD[d])
            self.rsow.copy_table_validate()
            for c in range(6):
                self.rsow.test_sort(c)
            self.rsow.scroll_top()

    def test_c_comp_tab(self):
        self.rsow.comp_tab()
        self.rsow.dropdown_validate(RSOW.RSOW_DROP[0], 1)
        for d in range(5):
            self.rsow.select_dropdown(d, RSOW.RSOW_DROP[d], 1)
            self.rsow.legend_validate([RSOW.RSOW_DROP[d]])
            self.rsow.headers_validate(RSOW.COMP_HEAD[d])
            self.rsow.copy_table_validate()
            for c in range(5):
                self.rsow.test_sort(c)
            self.rsow.scroll_top()

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
