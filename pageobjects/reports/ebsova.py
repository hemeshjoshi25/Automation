from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class EBSOVAPage(GenericReportPage):

    def __init__(self, driver):
        super(EBSOVAPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def sov_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.SOV.value)

    def cat_churn_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.CAT_CHURN.value)

    def cat_exp_con_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.CAT_EXP_CON.value)

    def brand_shift_tab(self):
        self.tabs(4)
        self.is_active_tab(ReportTabs.BRAND_SHIFTING.value)
