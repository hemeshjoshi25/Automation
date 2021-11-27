from pageobjects.modules.brand import BrandPage
from utils.IscE2eTestCase import IscE2eTestCase
from constants.enums import PageTitles, ReportTypes


class BrandNav(IscE2eTestCase):
    """Tests Navigation to each report within Brand Insights"""

    def setUp(self):
        super(BrandNav, self).setUp()
        # Initialize page objects for Brand Page
        self.brand = BrandPage(self.driver)
        # Navigate to Brand Insights
        self.brand.nav_link.click()
        self.assertEqual(self.brand.title.text, PageTitles.BRAND.value)
        self.brand.assert_intercom()

    def test_a_brand_diagnostics(self):
        self.brand.brand_diagnostics.click()
        self.brand.validate_nav(ReportTypes.BRAND_DIAGNOSTICS.value)

    def test_b_data_explorer(self):
        self.brand.data_explorer.click()
        self.brand.validate_nav(ReportTypes.DATA_EXPLORER.value)

    def test_c_share_explorer(self):
        self.brand.share_explorer.click()
        self.brand.validate_nav(ReportTypes.SHARE_EXPLORER.value)

    def test_d_moments_of_truth(self):
        self.brand.moments_of_truth.click()
        self.brand.validate_nav(ReportTypes.MOMENTS_OF_TRUTH.value)

    def test_e_bricks_clicks(self):
        self.brand.bricks_clicks.click()
        self.brand.validate_nav(ReportTypes.BRICKS_AND_CLICKS.value)

    def test_f_buyer_loyalty_flow(self):
        self.brand.buyer_loyalty_flow.click()
        self.brand.validate_nav(ReportTypes.BUYER_LOYALTY_FLOW.value)

    def test_g_brand_switching(self):
        self.brand.brand_switching.click()
        self.brand.validate_nav(ReportTypes.BRAND_SWITCHING.value)

    def test_h_ebsova(self):
        self.brand.ebsova.click()
        self.brand.validate_nav(ReportTypes.EBSOVA.value)

    def test_i_people_scorecard(self):
        self.brand.people_scorecard.click()
        self.brand.validate_nav(ReportTypes.PEOPLE_SCORECARD.value)

    def test_j_trended_metrics(self):
        self.brand.trended_metrics.click()
        self.brand.validate_nav(ReportTypes.TRENDED_METRICS.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
