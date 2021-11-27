from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.psychographics import PsychographicsPage
from constants.enums import ReportTypes
from constants.reports.psychographics import PSY


class TestPsychographics(IscE2eTestCase):
    def setUp(self):
        super(TestPsychographics, self).setUp()
        self.history = HistoryPage(self.driver)
        self.psy = PsychographicsPage(self.driver)

    def test_a_nav_psy(self):
        psy = ReportTypes.PSYCHOGRAPHICS.value
        title = ReportTypes.PREFIX.value + psy
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.psy.title.text, psy + ': ' + title)

    def test_b_advertising_tab(self):
        self.psy.advertising_tab()
        self.psy.psy_validate(PSY.ADV_HEAD, PSY.ADV_TABLE)

    def test_c_eating_tab(self):
        self.psy.eating_tab()
        self.psy.psy_validate(PSY.EAT_HEAD, PSY.EAT_TABLE)

    def test_d_health_tab(self):
        self.psy.health_tab()
        self.psy.psy_validate(PSY.HEALTH_HEAD, PSY.HEALTH_TABLE)

    def test_e_household_tab(self):
        self.psy.household_tab()
        self.psy.psy_validate(PSY.HH_HEAD, PSY.HH_TABLE)

    def test_f_shopping_tab(self):
        self.psy.shopping_tab()
        self.psy.psy_validate(PSY.SHOP_HEAD, PSY.SHOP_TABLE)

    def test_g_sports_tab(self):
        self.psy.sports_tab()
        self.psy.psy_validate(PSY.SPORTS_HEAD, PSY.SPORTS_TABLE)

    def test_h_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
