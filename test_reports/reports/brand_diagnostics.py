from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.brand_diagnostics import BrandDiagnosticsPage
from constants.enums import ReportTypes
from constants.reports.brand_diagnostics import BD


class TestBrandDiagnostics(IscE2eTestCase):
    def setUp(self):
        super(TestBrandDiagnostics, self).setUp()
        self.history = HistoryPage(self.driver)
        self.bd = BrandDiagnosticsPage(self.driver)

    def test_a_nav_bd(self):
        bd = ReportTypes.BRAND_DIAGNOSTICS.value
        title = ReportTypes.PREFIX.value + bd
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.bd.title.text, bd + ': ' + title)

    def test_b_kpi_tab(self):
        self.bd.kpi_tab()
        self.bd.dropdown_validate(BD.KPI_DROP[0])
        for d in range(9):
            self.bd.select_dropdown(d, BD.KPI_DROP[d])
            if 2 < d < 6:
                self.bd.legend_validate([BD.KPI_LEG[d]])
                self.bd.headers_validate(BD.KPI_ALT_HEAD[d])
            else:
                self.bd.legend_validate([BD.KPI_DROP[d]])
                self.bd.headers_validate(BD.KPI_STATIC_HEAD, BD.KPI_DROP[d].upper(), 1)
            self.bd.copy_table_validate()
            for c in range(len(self.bd.headers())):
                self.bd.test_sort(c)
            self.bd.scroll_top()

    def test_c_brand_tree_tab(self):
        self.bd.brand_tree_tab()
        self.bd.tree_titles_validate(BD.TREE_TITLES)

    def test_d_pen_grid_tab(self):
        self.bd.pen_grid_tab()
        self.bd.card_titles_validate(BD.CARD_TITLES)

    def test_e_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestBrandDiagnosticsCG(IscE2eTestCase):
    def setUp(self):
        super(TestBrandDiagnosticsCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.bd = BrandDiagnosticsPage(self.driver)

    def test_a_nav_bd(self):
        bd = ReportTypes.BRAND_DIAGNOSTICS.value
        title = ReportTypes.PREFIX_CG.value + bd
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.bd.title.text, bd + ': ' + title)

    def test_b_kpi_tab(self):
        self.bd.kpi_tab()
        self.bd.dropdown_validate(BD.KPI_DROP[0])
        for d in range(9):
            self.bd.select_dropdown(d, BD.KPI_DROP[d])
            if 2 < d < 6:
                self.bd.legend_validate([BD.KPI_LEG[d]])
                self.bd.headers_validate(BD.KPI_ALT_HEAD[d])
            else:
                self.bd.legend_validate([BD.KPI_DROP[d]])
                self.bd.headers_validate(BD.KPI_STATIC_HEAD, BD.KPI_DROP[d].upper(), 1)
            self.bd.copy_table_validate()
            for c in range(len(self.bd.headers())):
                self.bd.test_sort(c)
            self.bd.scroll_top()

    def test_c_brand_tree_tab(self):
        self.bd.brand_tree_tab()
        self.bd.tree_titles_validate(BD.TREE_TITLES)

    def test_d_pen_grid_tab(self):
        self.bd.pen_grid_tab()
        self.bd.card_titles_validate(BD.CARD_TITLES)

    def test_e_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
