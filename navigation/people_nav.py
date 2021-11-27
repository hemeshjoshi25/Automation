from pageobjects.modules.people import PeoplePage
from utils.IscE2eTestCase import IscE2eTestCase
from constants.enums import PageTitles, ReportTypes


class PeopleNav(IscE2eTestCase):
    """Tests Navigation to each report within People Insights"""

    def setUp(self):
        super(PeopleNav, self).setUp()
        # Initialize page objects for People Page
        self.people = PeoplePage(self.driver)
        # Navigate to People Insights
        self.people.nav_link.click()
        self.assertEqual(self.people.title.text, PageTitles.PEOPLE.value)
        self.people.assert_intercom()

    def test_a_shopper_profile(self):
        self.people.shopper_profile.click()
        self.people.validate_nav(ReportTypes.SHOPPER_PROFILE.value)

    def test_b_basket_affinity(self):
        self.people.basket_affinity.click()
        self.people.validate_nav(ReportTypes.BASKET_AFFINITY.value)

    def test_c_household_affinity(self):
        self.people.household_affinity.click()
        self.people.validate_nav(ReportTypes.HOUSEHOLD_AFFINITY.value)

    def test_d_cross_purchase(self):
        self.people.cross_purchase.click()
        self.people.validate_nav(ReportTypes.CROSS_PURCHASE.value)

    def test_e_psychographics(self):
        self.people.psychographics.click()
        self.people.validate_nav(ReportTypes.PSYCHOGRAPHICS.value)

    def test_f_media_consumption(self):
        self.people.media_consumption.click()
        self.people.validate_nav(ReportTypes.MEDIA_CONSUMPTION.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
