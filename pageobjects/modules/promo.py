from pageobjects.modules.module import GenericModulePage
from constants.enums import NavLinks


class PromoPage(GenericModulePage):

    @property
    def nav_link(self):
        return self.module_nav_link(NavLinks.PROMO_INSIGHTS.value)

    @property
    def promotion_scorecard(self):
        return self.report_nav_link(NavLinks.PROMO_SCORECARD.value)

    @property
    def event_analysis(self):
        return self.report_nav_link(NavLinks.EVENT_ANALYSIS.value)

    @property
    def retailer_circular_analysis(self):
        return self.report_nav_link(NavLinks.RETAILER_CIRCULAR_ANALYSIS.value)
