from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.share_explorer import ShareExplorerPage
from constants.enums import ReportTypes
from constants.reports.share_explorer import SE


class TestShareExplorer(IscE2eTestCase):
    def setUp(self):
        super(TestShareExplorer, self).setUp()
        self.history = HistoryPage(self.driver)
        self.se = ShareExplorerPage(self.driver)

    def test_a_nav_se(self):
        se = ReportTypes.SHARE_EXPLORER.value
        title = ReportTypes.PREFIX.value + se
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.se.title.text, se + ': ' + title)

    def test_b_se_tab(self):
        self.se.dropdown_validate(SE.SE_DROP[0])
        for d in range(3):
            self.se.select_dropdown(d, SE.SE_DROP[d])
            for t in range(2):
                self.se.toggle_buttons[t].click()
                self.se.headers_validate(SE.SE_HEAD)
                self.se.copy_table_validate()
                for c in range(6):
                    self.se.test_sort(c)
                self.se.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestShareExplorerCG(IscE2eTestCase):
    def setUp(self):
        super(TestShareExplorerCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.se = ShareExplorerPage(self.driver)

    def test_a_nav_se(self):
        se = ReportTypes.SHARE_EXPLORER.value
        title = ReportTypes.PREFIX_CG.value + se
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.se.title.text, se + ': ' + title)

    def test_b_se_tab(self):
        self.se.dropdown_validate(SE.SE_DROP[0])
        for d in range(3):
            self.se.select_dropdown(d, SE.SE_DROP[d])
            for t in range(2):
                self.se.toggle_buttons[t].click()
                self.se.headers_validate(SE.SE_HEAD)
                self.se.copy_table_validate()
                for c in range(6):
                    self.se.test_sort(c)
                self.se.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
