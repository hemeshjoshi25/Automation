from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class EventAnalysisPage(GenericReportPage):

    def __init__(self, driver):
        super(EventAnalysisPage, self).__init__(driver)

    def promo_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.PROMO_SUMMARY.value)

    def conversion_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.CONVERSION.value)
