from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.store_hierarchy import StoreHierarchyPage
from constants.enums import ReportTypes
from constants.reports.store_hierarchy import STH


class TestStoreHierarchy(IscE2eTestCase):
    def setUp(self):
        super(TestStoreHierarchy, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sth = StoreHierarchyPage(self.driver)

    def test_a_nav_sth(self):
        sth = ReportTypes.STORE_HIERARCHY.value
        title = ReportTypes.PREFIX.value + sth
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sth.title.text, sth + ': ' + title)

    def test_b_sth_tab(self):
        self.sth.headers_validate(STH.STH_HEAD)
        for c in range(5):
            self.sth.test_sort(c)

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
