from pageobjects.modules.promo import PromoPage
from utils.IscE2eTestCase import IscE2eTestCase
from constants.enums import PageTitles, ReportTypes


class PromoNav(IscE2eTestCase):
    """Tests Navigation to each report within Promo Insights"""

    def setUp(self):
        super(PromoNav, self).setUp()
        # Initialize page objects for Promo Page
        self.promo = PromoPage(self.driver)
        # Navigate to Promo Insights
        self.promo.nav_link.click()
        self.assertEqual(self.promo.title.text, PageTitles.PROMO.value)
        self.promo.assert_intercom()

    def test_a_promotion_scorecard(self):
        self.promo.promotion_scorecard.click()
        self.promo.validate_nav(ReportTypes.PROMOTION_SCORECARD.value)

    def test_b_event_analysis(self):
        self.promo.event_analysis.click()
        self.promo.validate_nav(ReportTypes.EVENT_ANALYSIS.value)

    def test_c_retailer_circular_analysis(self):
        self.promo.retailer_circular_analysis.click()
        self.promo.validate_nav(ReportTypes.RETAILER_CIRCULAR_ANALYSIS.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
