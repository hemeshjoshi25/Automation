from pageobjects.modules.module import GenericModulePage
from constants.enums import NavLinks


class ShopperPage(GenericModulePage):
    def __init__(self, driver):
        self.driver = driver

    @property
    def nav_link(self):
        return self.module_nav_link(NavLinks.SHOPPER_MOD.value)

    @property
    def shopper_metrics(self):
        return self.report_nav_link(NavLinks.SHOPPER_METRICS.value)

    @property
    def leakage_tree(self):
        return self.report_nav_link(NavLinks.LEAKAGE_TREE.value)

    @property
    def shopper_histogram(self):
        return self.report_nav_link(NavLinks.SHOPPER_HISTOGRAM.value)

    @property
    def trip_type_profile(self):
        return self.report_nav_link(NavLinks.TRIP_TYPE_PROFILE.value)

    @property
    def lapsed_repeat_new(self):
        return self.report_nav_link(NavLinks.LAPSED_REPEAT_NEW.value)

    @property
    def trip_circuits(self):
        return self.report_nav_link(NavLinks.TRIP_CIRCUITS.value)

    @property
    def promotion_effectiveness(self):
        return self.report_nav_link(NavLinks.PROMO_EFFECTIVENESS.value)

    @property
    def retailer_share_wallet(self):
        return self.report_nav_link(NavLinks.RETAILER_SOW.value)

    @property
    def store_diagnostics(self):
        return self.report_nav_link(NavLinks.STORE_DIAGNOSTICS.value)

    @property
    def store_loyalty_flow(self):
        return self.report_nav_link(NavLinks.STORE_LOYALTY_FLOW.value)
