from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class PepsiShopperCircuitsPage(GenericReportPage):

    def __init__(self, driver):
        super(PepsiShopperCircuitsPage, self).__init__(driver)

    def retailer_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.RETAIL_CIRCUITS.value)

    def channel_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.CHAN_CIRCUITS.value)

    def pepsi_edibles_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.PEP_EDIBLES.value)

    def total_edibles_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.TOTAL_EDIBLES.value)

    def demo_tab(self):
        self.tabs(4)
        self.is_active_tab(ReportTabs.DEMO.value)

    def sub_trips_tab(self):
        self.tabs(5)
        self.is_active_tab(ReportTabs.SUB_TRIPS.value)
