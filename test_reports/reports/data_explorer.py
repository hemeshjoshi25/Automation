from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.data_explorer import DataExplorerPage
from constants.enums import ReportTypes
from constants.reports.data_explorer import DE


class TestDataExplorer(IscE2eTestCase):
    def setUp(self):
        super(TestDataExplorer, self).setUp()
        self.history = HistoryPage(self.driver)
        self.de = DataExplorerPage(self.driver)

    def test_a_nav_de(self):
        de = ReportTypes.DATA_EXPLORER.value
        title = ReportTypes.PREFIX.value + de
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.de.title.text, de + ': ' + title)

    def test_b_de_tab(self):
        self.de.dropdown_validate(DE.MET_DROP[0])
        for d in range(3):
            self.de.select_dropdown(d, DE.MET_DROP[d])
            self.de.headers_validate(DE.DE_HEAD[d])
            self.de.copy_table_validate()
            for c in range(len(self.de.headers())):
                self.de.test_sort(c)
            self.de.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestDataExplorerCG(IscE2eTestCase):
    def setUp(self):
        super(TestDataExplorerCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.de = DataExplorerPage(self.driver)

    def test_a_nav_de(self):
        de = ReportTypes.DATA_EXPLORER.value
        title = ReportTypes.PREFIX_CG.value + de
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.de.title.text, de + ': ' + title)

    def test_b_de_tab(self):
        self.de.dropdown_validate(DE.MET_DROP[0])
        for d in range(3):
            self.de.select_dropdown(d, DE.MET_DROP[d])
            self.de.headers_validate(DE.DE_HEAD[d])
            self.de.copy_table_validate()
            for c in range(len(self.de.headers())):
                self.de.test_sort(c)
            self.de.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
