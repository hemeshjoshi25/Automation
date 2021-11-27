from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class UserIDFetchPage(GenericReportPage):

    def __init__(self, driver):
        super(UserIDFetchPage, self).__init__(driver)

    def hh_count_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.HH_COUNT.value)

    def user_id_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.USER_ID.value)
