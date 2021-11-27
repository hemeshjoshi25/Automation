from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.modules.people import PeoplePage
from constants.enums import PageTitles


class InsightsLogin(IscE2eTestCase):
    """Tests SetUp/Login and validates People Insights as landing page"""

    def setUp(self):
        super(InsightsLogin, self).setUp()
        # Initialize Page Objects for People Page
        self.people = PeoplePage(self.driver)

    def test_a_validate_login(self):
        """Validate landing page is People Insights"""
        self.assertEqual(self.people.title.text, PageTitles.PEOPLE.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
