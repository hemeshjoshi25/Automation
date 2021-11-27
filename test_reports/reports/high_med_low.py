from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.high_med_low import HighMedLowPage
from constants.enums import ReportTypes
from constants.reports.high_med_low import HML


class TestHighMedLow(IscE2eTestCase):
    def setUp(self):
        super(TestHighMedLow, self).setUp()
        self.history = HistoryPage(self.driver)
        self.hml = HighMedLowPage(self.driver)

    def test_a_nav_hml(self):
        hml = ReportTypes.HIGH_MED_LOW.value
        title = ReportTypes.PREFIX.value + hml
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.hml.title.text, hml + ': ' + title)

    def test_b_summary_tab(self):
        self.hml.summary_tab()
        self.hml.card_titles_validate(HML.CARD_TITLES)
        self.hml.download_diagram()

    def test_c_demo_tab(self):
        self.hml.demo_tab()
        self.hml.dropdown_validate(HML.MET_DROP[0])
        for d in range(3):
            self.hml.select_dropdown(d, HML.MET_DROP[d])
            for t in range(2):
                self.hml.toggle_buttons[t].click()
                self.hml.headers_validate(HML.DEMO_HEAD[t], form=HML.MET_DROP[d].upper())
                for c in range(1, 6):
                    self.hml.test_sort(c)
                self.hml.scroll_top()

    def test_d_top_prod_tab(self):
        self.hml.top_prod_tab()
        self.hml.dropdown_validate(HML.PROD_DROP[0])
        for d in range(4):
            self.hml.select_dropdown(d, HML.PROD_DROP[d])
            for t in range(2):
                self.hml.toggle_buttons[t].click()
                if d == 3:
                    self.hml.highcharts_legend_validate(HML.TOP_LEG[1])
                    self.hml.headers_validate(HML.PROD_SHARE_HEAD[t])
                else:
                    self.hml.highcharts_legend_validate(HML.TOP_LEG[0], HML.PROD_DROP[d])
                    self.hml.headers_validate(HML.PROD_HEAD[t], form=HML.PROD_DROP[d].upper())
                self.hml.copy_table_validate()
                for c in range(6):
                    self.hml.test_sort(c)
                self.hml.scroll_top()

    def test_e_top_stores_tab(self):
        self.hml.top_stores_tab()
        self.hml.dropdown_validate(HML.MET_DROP[0])
        for d in range(3):
            self.hml.select_dropdown(d, HML.MET_DROP[d])
            for t in range(2):
                self.hml.toggle_buttons[t].click()
                self.hml.highcharts_legend_validate(HML.TOP_LEG[0], HML.PROD_DROP[d])
                self.hml.headers_validate(HML.STORE_HEAD[t], form=HML.MET_DROP[d].upper())
                self.hml.copy_table_validate()
                for c in range(6):
                    self.hml.test_sort(c)
                self.hml.scroll_top()

    def test_f_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestHighMedLowCG(IscE2eTestCase):
    def setUp(self):
        super(TestHighMedLowCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.hml = HighMedLowPage(self.driver)

    def test_a_nav_hml(self):
        hml = ReportTypes.HIGH_MED_LOW.value
        title = ReportTypes.PREFIX_CG.value + hml
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.hml.title.text, hml + ': ' + title)

    def test_b_summary_tab(self):
        self.hml.summary_tab()
        self.hml.card_titles_validate(HML.CARD_TITLES_CG)
        self.hml.download_diagram()

    def test_c_demo_tab(self):
        self.hml.demo_tab()
        self.hml.dropdown_validate(HML.MET_DROP[0])
        for d in range(3):
            self.hml.select_dropdown(d, HML.MET_DROP[d])
            for t in range(2):
                self.hml.toggle_buttons[t].click()
                self.hml.headers_validate(HML.DEMO_HEAD[t], form=HML.MET_DROP[d].upper())
                for c in range(1, 6):
                    self.hml.test_sort(c)
                self.hml.scroll_top()

    def test_d_top_prod_tab(self):
        self.hml.top_prod_tab()
        self.hml.dropdown_validate(HML.PROD_DROP[0])
        for d in range(4):
            self.hml.select_dropdown(d, HML.PROD_DROP[d])
            for t in range(2):
                self.hml.toggle_buttons[t].click()
                if d == 3:
                    self.hml.highcharts_legend_validate(HML.TOP_LEG[1])
                    self.hml.headers_validate(HML.PROD_SHARE_HEAD[t])
                else:
                    self.hml.highcharts_legend_validate(HML.TOP_LEG[0], HML.PROD_DROP[d])
                    self.hml.headers_validate(HML.PROD_HEAD[t], form=HML.PROD_DROP[d].upper())
                self.hml.copy_table_validate()
                for c in range(6):
                    self.hml.test_sort(c)
                self.hml.scroll_top()

    def test_e_top_stores_tab(self):
        self.hml.top_stores_tab()
        self.hml.dropdown_validate(HML.MET_DROP[0])
        for d in range(3):
            self.hml.select_dropdown(d, HML.MET_DROP[d])
            for t in range(2):
                self.hml.toggle_buttons[t].click()
                self.hml.highcharts_legend_validate(HML.TOP_LEG[0], HML.PROD_DROP[d])
                self.hml.headers_validate(HML.STORE_HEAD[t], form=HML.MET_DROP[d].upper())
                self.hml.copy_table_validate()
                for c in range(6):
                    self.hml.test_sort(c)
                self.hml.scroll_top()

    def test_f_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
