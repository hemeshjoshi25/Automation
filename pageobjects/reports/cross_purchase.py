from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class CrossPurchasePage(GenericReportPage):

    def __init__(self, driver):
        super(CrossPurchasePage, self).__init__(driver)

    def buyer_overlap_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.BUYER_OVERLAP.value)

    def prod_matrix_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.PROD_MATRIX.value)
