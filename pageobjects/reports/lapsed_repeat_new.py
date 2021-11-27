from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class LapsedRepeatNewPage(GenericReportPage):

    def __init__(self, driver):
        super(LapsedRepeatNewPage, self).__init__(driver)

    def total_comp_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.TOTAL_COMP.value)

    def comparison_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.COMPARISON.value)

    def lrn_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.LRN.value)

    def store_pref_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.STORE_PREF.value)

    def prod_pref_tab(self):
        self.tabs(4)
        self.is_active_tab(ReportTabs.PROD_PREF.value)
