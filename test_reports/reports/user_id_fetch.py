from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.user_id_fetch import UserIDFetchPage
from constants.enums import ReportTypes
from constants.reports.user_id_fetch import UIDF


class TestUserIDFetch(IscE2eTestCase):
    def setUp(self):
        super(TestUserIDFetch, self).setUp()
        self.history = HistoryPage(self.driver)
        self.uidf = UserIDFetchPage(self.driver)

    def test_a_nav_uidf(self):
        uidf = ReportTypes.USER_ID_FETCH.value
        title = ReportTypes.PREFIX.value + uidf
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.uidf.title.text, uidf + ': ' + title)

    def test_b_hh_count_tab(self):
        self.uidf.hh_count_tab()
        self.uidf.headers_validate(UIDF.HH_HEAD)

    def test_c_user_id_tab(self):
        self.uidf.user_id_tab()
        self.uidf.headers_validate(UIDF.ID_HEAD)

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
