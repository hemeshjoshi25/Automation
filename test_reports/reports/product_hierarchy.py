from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.product_hierarchy import ProductHierarchyPage
from constants.enums import ReportTypes
from constants.reports.product_hierarchy import PH


class TestProductHierarchy(IscE2eTestCase):
    def setUp(self):
        super(TestProductHierarchy, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ph = ProductHierarchyPage(self.driver)

    def test_a_nav_ph(self):
        ph = ReportTypes.PRODUCT_HIERARCHY.value
        title = ReportTypes.PREFIX.value + ph
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ph.title.text, ph + ': ' + title)

    def test_b_ph(self):
        self.ph.headers_validate(PH.PH_HEAD)
        for c in range(7):
            self.ph.test_sort(c)

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
