from pageobjects.report import GenericReportPage
from constants.reports.psychographics import PSY
from constants.enums import ReportTabs


class PsychographicsPage(GenericReportPage):

    def __init__(self, driver):
        super(PsychographicsPage, self).__init__(driver)

    def advertising_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.ADVERTISING.value)

    def eating_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.EATING.value)

    def health_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.HEALTH_SUS.value)

    def household_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.HH.value)

    def shopping_tab(self):
        self.tabs(4)
        self.is_active_tab(ReportTabs.SHOPPING.value)

    def sports_tab(self):
        self.tabs(5)
        self.is_active_tab(ReportTabs.SPORTS.value)

    def psy_validate(self, form, table):
        self.table_validate(1, table)
        for t, tab in enumerate(self.tables()):
            self.headers_validate(PSY.PSY_HEAD, table_idx=t, form=form[t])
            self.copy_table_validate(t)
            for c in range(1, 4):
                self.test_sort(c, table_idx=t)
        self.scroll_top()
