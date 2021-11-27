from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class RetailerShareWalletPage(GenericReportPage):

    def __init__(self, driver):
        super(RetailerShareWalletPage, self).__init__(driver)

    def cat_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.CAT_SUMMARY.value)

    def comp_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.COMP_SUMMARY.value)
