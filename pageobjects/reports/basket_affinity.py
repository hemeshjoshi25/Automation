from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class BasketAffinityPage(GenericReportPage):

    def __init__(self, driver):
        super(BasketAffinityPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def retailer_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.RETAILER_PREF.value)
