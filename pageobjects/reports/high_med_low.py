from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class HighMedLowPage(GenericReportPage):

    def __init__(self, driver):
        super(HighMedLowPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def demo_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.DEMO.value)

    def top_prod_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.TOP_PRODUCTS.value)

    def top_stores_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.TOP_STORES.value)
