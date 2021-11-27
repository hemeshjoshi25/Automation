from pageobjects.modules.module import GenericModulePage
from constants.enums import NavLinks


class BrandPage(GenericModulePage):

    @property
    def nav_link(self):
        return self.module_nav_link(NavLinks.BRAND_MOD.value)

    @property
    def brand_diagnostics(self):
        return self.report_nav_link(NavLinks.BRAND_DIAGNOSTICS.value)

    @property
    def data_explorer(self):
        return self.report_nav_link(NavLinks.DATA_EXPLORER.value)

    @property
    def share_explorer(self):
        return self.report_nav_link(NavLinks.SHARE_EXPLORER.value)

    @property
    def moments_of_truth(self):
        return self.report_nav_link(NavLinks.MOMENTS_OF_TRUTH.value)

    @property
    def bricks_clicks(self):
        return self.report_nav_link(NavLinks.BRICKS_CLICKS.value)

    @property
    def buyer_loyalty_flow(self):
        return self.report_nav_link(NavLinks.BUYER_LOYALTY_FLOW.value)

    @property
    def brand_switching(self):
        return self.report_nav_link(NavLinks.BRAND_SWITCHING.value)

    @property
    def ebsova(self):
        return self.report_nav_link(NavLinks.EBSOVA.value)

    @property
    def people_scorecard(self):
        return self.report_nav_link(NavLinks.PEOPLE_SCORECARD.value)

    @property
    def trended_metrics(self):
        return self.report_nav_link(NavLinks.TRENDED_METRICS.value)
