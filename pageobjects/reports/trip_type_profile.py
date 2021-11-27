from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs
from constants.reports.trip_type_profile import TTP


class TripTypeProfilePage(GenericReportPage):

    def __init__(self, driver):
        super(TripTypeProfilePage, self).__init__(driver)

    def trip_type_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.TRIP_TYPE_DIST.value)

    def top_stores_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.TOP_STORES.value)

    def ttp_test(self, header, idx=0):
        self.dropdown_validate(TTP.MET_DROP[0])
        for d in range(5):
            self.select_dropdown(d, TTP.MET_DROP[d])
            self.headers_validate(TTP.TTP_HEAD, header[idx], form=TTP.MET_DROP[d].upper())
            self.copy_table_validate()
            for c in range(6):
                self.test_sort(c)
            self.scroll_top()
