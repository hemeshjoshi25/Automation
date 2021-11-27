from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.household_affinity import HouseholdAffinityPage
from constants.enums import ReportTypes
from constants.reports.household_affinity import HA


class TestHouseholdAffinity(IscE2eTestCase):
    def setUp(self):
        super(TestHouseholdAffinity, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ha = HouseholdAffinityPage(self.driver)

    def test_a_nav_ha(self):
        ha = ReportTypes.HOUSEHOLD_AFFINITY.value
        title = ReportTypes.PREFIX.value + ha
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ha.title.text, ha + ': ' + title)

    def test_b_main_tab(self):
        self.ha.dropdown_validate(HA.HH_DROP[0])
        for d in range(3):
            self.ha.select_dropdown(d, HA.HH_DROP[d])
            self.ha.headers_validate(HA.HH_HEAD[d])
            for c in range(7):
                self.ha.test_sort(c)
            self.ha.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestHouseholdAffinityCG(IscE2eTestCase):
    def setUp(self):
        super(TestHouseholdAffinityCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ha = HouseholdAffinityPage(self.driver)

    def test_a_nav_ha(self):
        ha = ReportTypes.HOUSEHOLD_AFFINITY.value
        title = ReportTypes.PREFIX_CG.value + ha
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ha.title.text, ha + ': ' + title)

    def test_b_main_tab(self):
        self.ha.dropdown_validate(HA.HH_DROP[0])
        for d in range(3):
            self.ha.select_dropdown(d, HA.HH_DROP[d])
            self.ha.headers_validate(HA.HH_HEAD[d])
            for c in range(7):
                self.ha.test_sort(c)
            self.ha.scroll_top()

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
