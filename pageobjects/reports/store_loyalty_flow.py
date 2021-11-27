from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class StoreLoyaltyFlowPage(GenericReportPage):

    def __init__(self, driver):
        super(StoreLoyaltyFlowPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def benchmarks_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.BENCHMARKS.value)

    def store_pref_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.STORE_PREF.value)
