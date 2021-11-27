from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.new_item_sova import NewItemSOVAPage
from constants.enums import ReportTypes
from constants.reports.new_item_sova import NISOVA


class TestNewItemSOVA(IscE2eTestCase):
    def setUp(self):
        super(TestNewItemSOVA, self).setUp()
        self.history = HistoryPage(self.driver)
        self.nisova = NewItemSOVAPage(self.driver)

    def test_a_nav_nisova(self):
        nisova = ReportTypes.NEW_ITEM_SOVA.value
        title = ReportTypes.PREFIX.value + nisova
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.nisova.title.text, nisova + ': ' + title)

    def test_b_summary_tab(self):
        self.nisova.summary_tab()
        self.nisova.dropdown_validate(NISOVA.NI_1)
        self.nisova.headers_validate(NISOVA.SUM_HEAD)
        self.nisova.copy_table_validate()
        for c in range(3):
            self.nisova.test_sort(c)
        self.nisova.scroll_top()

    def test_c_shifting_tab(self):
        self.nisova.shifting_tab()
        self.nisova.dropdown_validate(NISOVA.NI_1)
        self.nisova.dropdown_validate(NISOVA.SHIFT_DROP[0], 1)
        for d in range(3):
            self.nisova.select_dropdown(d, NISOVA.SHIFT_DROP[d], 1)
            self.nisova.headers_validate(NISOVA.SHIFT_HEAD)
            for c in range(5):
                self.nisova.test_sort(c)
            self.nisova.scroll_top()

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestNewItemSOVACG(IscE2eTestCase):
    def setUp(self):
        super(TestNewItemSOVACG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.nisova = NewItemSOVAPage(self.driver)

    def test_a_nav_nisova(self):
        nisova = ReportTypes.NEW_ITEM_SOVA.value
        title = ReportTypes.PREFIX_CG.value + nisova
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.nisova.title.text, nisova + ': ' + title)

    def test_b_summary_tab(self):
        self.nisova.summary_tab()
        self.nisova.dropdown_validate(NISOVA.NI_1)
        self.nisova.headers_validate(NISOVA.SUM_HEAD)
        self.nisova.copy_table_validate()
        for c in range(3):
            self.nisova.test_sort(c)
        self.nisova.scroll_top()

    def test_c_shifting_tab(self):
        self.nisova.shifting_tab()
        self.nisova.dropdown_validate(NISOVA.NI_1)
        self.nisova.dropdown_validate(NISOVA.SHIFT_DROP[0], 1)
        for d in range(3):
            self.nisova.select_dropdown(d, NISOVA.SHIFT_DROP[d], 1)
            self.nisova.headers_validate(NISOVA.SHIFT_HEAD)
            for c in range(5):
                self.nisova.test_sort(c)
            self.nisova.scroll_top()

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
