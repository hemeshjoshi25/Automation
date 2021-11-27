from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class BuyerLoyaltyFlowPage(GenericReportPage):

    def __init__(self, driver):
        super(BuyerLoyaltyFlowPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def loyalty_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.LOYALTY_SHIFT.value)

    def comp_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.COMPARISON.value)
