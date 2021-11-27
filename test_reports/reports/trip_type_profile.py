from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.trip_type_profile import TripTypeProfilePage
from constants.enums import ReportTypes
from constants.reports.trip_type_profile import TTP


class TestTripTypeProfile(IscE2eTestCase):
    def setUp(self):
        super(TestTripTypeProfile, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ttp = TripTypeProfilePage(self.driver)

    def test_a_nav_ttp(self):
        ttp = ReportTypes.TRIP_TYPE_PROFILE.value
        title = ReportTypes.PREFIX.value + ttp
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ttp.title.text, ttp + ': ' + title)

    def test_b_trip_type_tab(self):
        self.ttp.trip_type_tab()
        self.ttp.ttp_test(TTP.HEAD)

    def test_c_top_stores_tab(self):
        self.ttp.top_stores_tab()
        self.ttp.ttp_test(TTP.HEAD, 1)

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestTripTypeProfileRV(IscE2eTestCase):
    def setUp(self):
        super(TestTripTypeProfileRV, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ttp = TripTypeProfilePage(self.driver)

    def test_a_nav_ttp(self):
        ttp = ReportTypes.TRIP_TYPE_PROFILE.value
        title = ReportTypes.PREFIX_RV.value + ttp
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ttp.title.text, ttp + ': ' + title)

    def test_b_trip_type_tab(self):
        self.ttp.trip_type_tab()
        self.ttp.ttp_test(TTP.HEAD_RV)

    def test_c_top_stores_tab(self):
        self.ttp.top_stores_tab()
        self.ttp.ttp_test(TTP.HEAD, 1)

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestTripTypeProfileCG(IscE2eTestCase):
    def setUp(self):
        super(TestTripTypeProfileCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ttp = TripTypeProfilePage(self.driver)

    def test_a_nav_ttp(self):
        ttp = ReportTypes.TRIP_TYPE_PROFILE.value
        title = ReportTypes.PREFIX_CG.value + ttp
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ttp.title.text, ttp + ': ' + title)

    def test_b_trip_type_tab(self):
        self.ttp.trip_type_tab()
        self.ttp.ttp_test(TTP.HEAD)

    def test_c_top_stores_tab(self):
        self.ttp.top_stores_tab()
        self.ttp.ttp_test(TTP.HEAD, 1)

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
