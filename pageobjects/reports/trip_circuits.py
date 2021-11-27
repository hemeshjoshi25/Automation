from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class TripCircuitsPage(GenericReportPage):

    def __init__(self, driver):
        super(TripCircuitsPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def closed_store_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.CLOSED_STORE.value)

    def closed_prod_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.CLOSED_PROD.value)

    def leaked_store_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.LEAKED_STORE.value)

    def leaked_prod_tab(self):
        self.tabs(4)
        self.is_active_tab(ReportTabs.LEAKED_PROD.value)

    def common_circuits_tab(self):
        self.tabs(5)
        self.is_active_tab(ReportTabs.COMMON_CIRCUITS.value)
