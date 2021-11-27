from pageobjects.modules.module import GenericModulePage
from constants.enums import NavLinks


class PeoplePage(GenericModulePage):

    @property
    def nav_link(self):
        return self.module_nav_link(NavLinks.PEOPLE_INSIGHTS.value)

    @property
    def shopper_profile(self):
        return self.report_nav_link(NavLinks.SHOPPER_PROFILE.value)

    @property
    def basket_affinity(self):
        return self.report_nav_link(NavLinks.BASKET_AFFINITY.value)

    @property
    def household_affinity(self):
        return self.report_nav_link(NavLinks.HOUSEHOLD_AFFINITY.value)

    @property
    def cross_purchase(self):
        return self.report_nav_link(NavLinks.CROSS_PURCHASE.value)

    @property
    def psychographics(self):
        return self.report_nav_link(NavLinks.PSYCHOGRAHPICS.value)

    @property
    def media_consumption(self):
        return self.report_nav_link(NavLinks.MEDIA_CONSUMPTION.value)
