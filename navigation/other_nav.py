from pageobjects.history import HistoryPage
from pageobjects.modules.surveys import SurveysPage
from pageobjects.modules.groups import GroupsPage
from pageobjects.modules.adv_groups import AdvGroupsPage
from pageobjects.modules.settings import SettingsPage
from utils.IscE2eTestCase import IscE2eTestCase
from constants.enums import PageTitles


class OtherNav(IscE2eTestCase):
    """Tests Navigation to History, Surveys, Groups, and Settings"""

    def setUp(self):
        super(OtherNav, self).setUp()
        # Initialize page objects
        self.history = HistoryPage(self.driver)
        self.surveys = SurveysPage(self.driver)
        self.groups = GroupsPage(self.driver)
        self.adv_groups = AdvGroupsPage(self.driver)
        self.settings = SettingsPage(self.driver)

    def test_a_history_nav(self):
        self.history.nav_link.click()
        self.assertEqual(self.history.title.text, PageTitles.HISTORY.value)

    def test_b_surveys_nav(self):
        self.surveys.nav_link.click()
        self.assertEqual(self.surveys.title.text, PageTitles.SURVEYS.value)

    def test_c_groups_nav(self):
        self.groups.nav_link.click()
        self.assertEqual(self.groups.title.text,
                         PageTitles.PEOPLE_GROUPS.value)
        self.groups.trip_groups.click()
        self.assertEqual(self.groups.title.text, PageTitles.TRIP_GROUPS.value)

    def test_d_adv_groups_nav(self):
        self.adv_groups.nav_link.click()
        self.assertEqual(self.groups.title.text,
                         PageTitles.PROD_GROUPS.value)
        self.adv_groups.store_groups.click()
        self.assertEqual(self.groups.title.text, PageTitles.STORE_GROUPS.value)

    def test_d_settings_nav(self):
        self.settings.nav_link.click()
        self.assertEqual(self.settings.title.text, PageTitles.SETTINGS.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
