from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.store_diagnostics import StoreDiagnosticsPage
from constants.enums import ReportTypes
from constants.reports.store_diagnostics import SD


class TestStoreDiagnostics(IscE2eTestCase):
    def setUp(self):
        super(TestStoreDiagnostics, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sd = StoreDiagnosticsPage(self.driver)

    def test_a_nav_sd(self):
        sd = ReportTypes.STORE_DIAGNOSTICS.value
        title = ReportTypes.PREFIX.value + sd
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sd.title.text, sd + ': ' + title)

    def test_b_kpi_tab(self):
        self.sd.kpi_tab()
        self.sd.dropdown_validate(SD.KPI_DROP[0])
        for d in range(18):
            self.sd.select_dropdown(d, SD.KPI_DROP[d])
            if d == 3:
                self.sd.legend_validate(SD.KPI_LEG)
                self.sd.headers_validate(SD.KPI_HH_HEAD)
            elif d == 6 or 7 < d < 15:
                self.sd.legend_validate([SD.KPI_DROP[d]])
                self.sd.headers_validate(SD.KPI_STATIC_HEAD[1], SD.KPI_DROP[d].upper(), 1)
            else:
                self.sd.legend_validate([SD.KPI_DROP[d]])
                self.sd.headers_validate(SD.KPI_STATIC_HEAD[0], SD.KPI_DROP[d].upper(), 1)
            self.sd.copy_table_validate()
            for c in range(6):
                self.sd.test_sort(c)
            self.sd.scroll_top()

    def test_c_pen_grid_tab(self):
        self.sd.pen_grid_tab()
        self.sd.card_titles_validate(SD.CARDS)

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestStoreDiagnosticsCG(IscE2eTestCase):
    def setUp(self):
        super(TestStoreDiagnosticsCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.sd = StoreDiagnosticsPage(self.driver)

    def test_a_nav_sd(self):
        sd = ReportTypes.STORE_DIAGNOSTICS.value
        title = ReportTypes.PREFIX_CG.value + sd
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.sd.title.text, sd + ': ' + title)

    def test_b_kpi_tab(self):
        self.sd.kpi_tab()
        self.sd.dropdown_validate(SD.KPI_DROP[0])
        for d in range(18):
            self.sd.select_dropdown(d, SD.KPI_DROP[d])
            if d == 3:
                self.sd.legend_validate(SD.KPI_LEG)
                self.sd.headers_validate(SD.KPI_HH_HEAD)
            elif d == 6 or 7 < d < 15:
                self.sd.legend_validate([SD.KPI_DROP[d]])
                self.sd.headers_validate(SD.KPI_STATIC_HEAD[1], SD.KPI_DROP[d].upper(), 1)
            else:
                self.sd.legend_validate([SD.KPI_DROP[d]])
                self.sd.headers_validate(SD.KPI_STATIC_HEAD[0], SD.KPI_DROP[d].upper(), 1)
            self.sd.copy_table_validate()
            for c in range(6):
                self.sd.test_sort(c)
            self.sd.scroll_top()

    def test_c_pen_grid_tab(self):
        self.sd.pen_grid_tab()
        self.sd.card_titles_validate(SD.CARDS_CG)

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
