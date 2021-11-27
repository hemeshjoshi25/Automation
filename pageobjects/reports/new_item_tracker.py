from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class NewItemTrackerPage(GenericReportPage):

    def __init__(self, driver):
        super(NewItemTrackerPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def trial_repeat_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.TRIAL_REPEAT.value)

    def repeat_drivers_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.REPEAT_DRIVERS.value)

    def retailer_drivers_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.RETAILER_DRIVERS.value)

    def top_items_tab(self):
        self.tabs(4)
        self.is_active_tab(ReportTabs.TOP_ITEMS.value)
