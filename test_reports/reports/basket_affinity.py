from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.basket_affinity import BasketAffinityPage
from constants.enums import ReportTypes
from constants.reports.basket_affinity import BA


class TestBasketAffinity(IscE2eTestCase):
    def setUp(self):
        super(TestBasketAffinity, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ba = BasketAffinityPage(self.driver)

    def test_a_nav_ba(self):
        ba = ReportTypes.BASKET_AFFINITY.value
        title = ReportTypes.PREFIX.value + ba
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ba.title.text, ba + ': ' + title)

    def test_b_summary_tab(self):
        self.ba.summary_tab()
        self.ba.dropdown_validate(BA.SUMMARY_DROP[0], 1)
        for d in range(3):
            self.ba.select_dropdown(d, BA.SUMMARY_DROP[d], 1)
            self.ba.headers_validate(BA.SUMMARY_HEAD[d])
            self.ba.copy_table_validate()
            for c in range(7):
                self.ba.test_sort(c)
            self.ba.scroll_top()

    def test_c_retailer_preference_tab(self):
        self.ba.retailer_tab()
        self.ba.headers_validate(BA.RETAIL_HEAD)
        self.ba.copy_table_validate()
        for c in range(2):
            self.ba.test_sort(c)
        self.ba.scroll_top()

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestBasketAffinityCG(IscE2eTestCase):
    def setUp(self):
        super(TestBasketAffinityCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ba = BasketAffinityPage(self.driver)

    def test_a_nav_ba(self):
        ba = ReportTypes.BASKET_AFFINITY.value
        title = ReportTypes.PREFIX_CG.value + ba
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ba.title.text, ba + ': ' + title)

    def test_b_summary_tab(self):
        self.ba.summary_tab()
        self.ba.dropdown_validate(BA.SUMMARY_DROP[0], 1)
        for d in range(3):
            self.ba.select_dropdown(d, BA.SUMMARY_DROP[d], 1)
            self.ba.headers_validate(BA.SUMMARY_HEAD[d])
            self.ba.copy_table_validate()
            for c in range(7):
                self.ba.test_sort(c)
            self.ba.scroll_top()

    def test_c_retailer_preference_tab(self):
        self.ba.retailer_tab()
        self.ba.headers_validate(BA.RETAIL_HEAD)
        self.ba.copy_table_validate()
        for c in range(2):
            self.ba.test_sort(c)
        self.ba.scroll_top()

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
