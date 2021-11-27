from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class LeakageTreePage(GenericReportPage):

    def __init__(self, driver):
        super(LeakageTreePage, self).__init__(driver)

    def tree_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.TREE_DIAGRAM.value)

    def shopped_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.STORES_SHOPPED.value)

    def top_prod_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.TOP_PRODUCTS.value)

    def benchmark_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.BENCHMARK.value)
