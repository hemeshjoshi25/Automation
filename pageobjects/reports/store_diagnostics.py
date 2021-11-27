from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class StoreDiagnosticsPage(GenericReportPage):

    def __init__(self, driver):
        super(StoreDiagnosticsPage, self).__init__(driver)

    def kpi_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.KPI.value)

    def pen_grid_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.PEN_GRID.value)
