from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs
from constants.reports.media_consumption import MC


class MediaConsumptionPage(GenericReportPage):

    def __init__(self, driver):
        super(MediaConsumptionPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def watch_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.WATCHING.value)

    def listen_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.LISTENING.value)

    def read_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.READING.value)

    def social_tab(self):
        self.tabs(4)
        self.is_active_tab(ReportTabs.SOCIAL_MEDIA.value)

    def media_validate(self, form, table):
        self.table_validate(1, table)
        for t, tab in enumerate(self.tables()):
            self.headers_validate(MC.MC_HEAD, table_idx=t, form=form[t])
            self.copy_table_validate(t)
            for c in range(1, 4):
                self.test_sort(c, table_idx=t)
        self.scroll_top()
