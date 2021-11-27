from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs
from constants.reports.shopper_profile import SP


class ShopperProfilePage(GenericReportPage):

    def __init__(self, driver):
        super(ShopperProfilePage, self).__init__(driver)

    def demo_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.DEMO.value)
        self.dropdown_validate(SP.DEMO_DROP[0])

    def basic_mets_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.BASIC_METS.value)

    def top_stores_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.TOP_STORES.value)
        self.dropdown_validate(SP.STORES_DROP[0])

    def payment_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.PAY_METHODS.value)
        self.dropdown_validate(SP.PAY_DROP[0])

    def timing_tab(self):
        self.tabs(4)
        self.is_active_tab(ReportTabs.TIMING.value)
        self.dropdown_validate(SP.TIME_DROP[0])

    def trip_type_tab(self):
        self.tabs(5)
        self.is_active_tab(ReportTabs.TRIP_TYPE.value)
        self.dropdown_validate(SP.TRIP_DROP[0])
