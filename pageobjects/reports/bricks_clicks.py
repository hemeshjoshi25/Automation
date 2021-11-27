from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class BricksClicksPage(GenericReportPage):

    def __init__(self, driver):
        super(BricksClicksPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def channel_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.CHAN_SHIFT.value)

    def brand_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.BRAND_SHIFT.value)
