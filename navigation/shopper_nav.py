from pageobjects.modules.shopper import ShopperPage
from utils.IscE2eTestCase import IscE2eTestCase
from constants.enums import PageTitles, ReportTypes


class ShopperNav(IscE2eTestCase):
    """Tests Navigation to each report within Shopper Insights"""

    def setUp(self):
        super(ShopperNav, self).setUp()
        # Initialize page objects for Shopper Page
        self.shopper = ShopperPage(self.driver)
        # Navigate to Shopper Insights
        self.shopper.nav_link.click()
        self.assertEqual(self.shopper.title.text, PageTitles.SHOPPER.value)
        self.shopper.assert_intercom()

    def test_a_shopper_metrics(self):
        self.shopper.shopper_metrics.click()
        self.shopper.validate_nav(ReportTypes.SHOPPER_METRICS.value)

    def test_b_leakage_tree(self):
        self.shopper.leakage_tree.click()
        self.shopper.validate_nav(ReportTypes.LEAKAGE_TREE.value)

    def test_c_shopper_histogram(self):
        self.shopper.shopper_histogram.click()
        self.shopper.validate_nav(ReportTypes.SHOPPER_HISTOGRAM.value)

    def test_d_trip_type_profile(self):
        self.shopper.trip_type_profile.click()
        self.shopper.validate_nav(ReportTypes.TRIP_TYPE_PROFILE.value)

    def test_e_lapsed_repeat_new(self):
        self.shopper.lapsed_repeat_new.click()
        self.shopper.validate_nav(ReportTypes.LAPSED_REPEAT_NEW.value)

    def test_f_trip_circuits(self):
        self.shopper.trip_circuits.click()
        self.shopper.validate_nav(ReportTypes.TRIP_CIRCUITS.value)

    def test_g_promo_effectiveness(self):
        self.shopper.promotion_effectiveness.click()
        self.shopper.validate_nav(ReportTypes.PROMOTION_EFFECTIVENESS.value)

    def test_h_retailer_share_wallet(self):
        self.shopper.retailer_share_wallet.click()
        self.shopper.validate_nav(ReportTypes.RETAILER_SHARE_WALLET.value)

    def test_i_store_diagnostics(self):
        self.shopper.store_diagnostics.click()
        self.shopper.validate_nav(ReportTypes.STORE_DIAGNOSTICS.value)

    def test_j_store_loyalty_flow(self):
        self.shopper.store_loyalty_flow.click()
        self.shopper.validate_nav(ReportTypes.STORE_LOYALTY_FLOW.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
