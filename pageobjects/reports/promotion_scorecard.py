from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class PromotionScorecardPage(GenericReportPage):

    def __init__(self, driver):
        super(PromotionScorecardPage, self).__init__(driver)

    def promo_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.PROMO_DETAILS.value)

    def increment_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.INCREMENTALITY.value)

    def increment_detail_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.INCREMENT_DETAIL.value)

    def brand_switch_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.BRAND_SWITCH_SUM.value)

    def brand_detail_tab(self):
        self.tabs(4)
        self.is_active_tab(ReportTabs.BRAND_SWITCH_DETAIL.value)

    def store_switch_tab(self):
        self.tabs(5)
        self.is_active_tab(ReportTabs.STORE_SWITCH.value)
