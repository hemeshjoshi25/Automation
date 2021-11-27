from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.ebsova import EBSOVAPage
from constants.enums import ReportTypes
from constants.reports.ebsova import EBSOVA


class TestEBSOVA(IscE2eTestCase):
    def setUp(self):
        super(TestEBSOVA, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ebsova = EBSOVAPage(self.driver)

    def test_a_nav_ebsova(self):
        ebsova = ReportTypes.EBSOVA.value
        title = ReportTypes.PREFIX.value + ebsova
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ebsova.title.text, ebsova + ': ' + title)

    def test_b_summary_tab(self):
        self.ebsova.summary_tab()
        self.ebsova.dropdown_validate(EBSOVA.SUMMARY_DROP[0])
        for d in range(2):
            self.ebsova.select_dropdown(d, EBSOVA.SUMMARY_DROP[d])
            self.ebsova.tree_titles_validate(EBSOVA.TREE_TITLES, EBSOVA.SUMMARY_DROP[d])
            self.ebsova.download_diagram()

    def test_c_sov_tab(self):
        self.ebsova.sov_tab()
        for t in range(2):
            self.ebsova.toggle_buttons[t].click()
            self.ebsova.legend_validate(EBSOVA.SOV_LEG, EBSOVA.SUMMARY_DROP[t])
            self.ebsova.download_diagram()
            self.ebsova.headers_validate(EBSOVA.SOV_HEAD, form=EBSOVA.SUMMARY_DROP[t].upper())
            self.ebsova.copy_table_validate()
            for c in range(2):
                self.ebsova.test_sort(c)
            self.ebsova.scroll_top()

    def test_d_cat_churn_tab(self):
        self.ebsova.cat_churn_tab()
        self.ebsova.dropdown_validate(EBSOVA.CAT_DROP[0])
        for d in range(3):
            self.ebsova.select_dropdown(d, EBSOVA.CAT_DROP[d])
            for t in range(2):
                self.ebsova.toggle_buttons[t].click()
                self.ebsova.legend_validate(EBSOVA.CAT_LEG)
                self.ebsova.download_diagram()
                self.ebsova.headers_validate(
                    EBSOVA.CAT_HEAD, EBSOVA.CAT_DROP[d].upper(), form=EBSOVA.SUMMARY_DROP[t].upper())
                self.ebsova.copy_table_validate()
                for c in range(8):
                    self.ebsova.test_sort(c)
                self.ebsova.scroll_top()

    def test_e_cat_exp_con_tab(self):
        self.ebsova.cat_exp_con_tab()
        self.ebsova.dropdown_validate(EBSOVA.CAT_DROP[0])
        for d in range(3):
            self.ebsova.select_dropdown(d, EBSOVA.CAT_DROP[d])
            for t in range(2):
                self.ebsova.toggle_buttons[t].click()
                self.ebsova.legend_validate(EBSOVA.EXP_CON_LEG)
                self.ebsova.download_diagram()
                self.ebsova.headers_validate(
                    EBSOVA.CAT_HEAD, EBSOVA.CAT_DROP[d].upper(), form=EBSOVA.SUMMARY_DROP[t].upper())
                self.ebsova.copy_table_validate()
                for c in range(8):
                    self.ebsova.test_sort(c)
                self.ebsova.scroll_top()

    def test_f_brand_shift_tab(self):
        self.ebsova.brand_shift_tab()
        self.ebsova.dropdown_validate(EBSOVA.SHIFT_DROP[0])
        for d in range(4):
            self.ebsova.select_dropdown(d, EBSOVA.SHIFT_DROP[d])
            for t in range(2):
                self.ebsova.toggle_buttons[t].click()
                self.ebsova.legend_validate(EBSOVA.SHIFT_LEG)
                self.ebsova.download_diagram()
                self.ebsova.headers_validate(
                    EBSOVA.CAT_HEAD, EBSOVA.SHIFT_FORM[d].upper(), form=EBSOVA.SUMMARY_DROP[t].upper())
                for c in range(8):
                    self.ebsova.test_sort(c)
                self.ebsova.scroll_top()

    def test_g_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestEBSOVACG(IscE2eTestCase):
    def setUp(self):
        super(TestEBSOVACG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ebsova = EBSOVAPage(self.driver)

    def test_a_nav_ebsova(self):
        ebsova = ReportTypes.EBSOVA.value
        title = ReportTypes.PREFIX_CG.value + ebsova
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ebsova.title.text, ebsova + ': ' + title)

    def test_b_summary_tab(self):
        self.ebsova.summary_tab()
        self.ebsova.dropdown_validate(EBSOVA.SUMMARY_DROP[0])
        for d in range(2):
            self.ebsova.select_dropdown(d, EBSOVA.SUMMARY_DROP[d])
            self.ebsova.tree_titles_validate(EBSOVA.TREE_TITLES, EBSOVA.SUMMARY_DROP[d])
            self.ebsova.download_diagram()

    def test_c_sov_tab(self):
        self.ebsova.sov_tab()
        for t in range(2):
            self.ebsova.toggle_buttons[t].click()
            self.ebsova.legend_validate(EBSOVA.SOV_LEG, EBSOVA.SUMMARY_DROP[t])
            self.ebsova.download_diagram()
            self.ebsova.headers_validate(EBSOVA.SOV_HEAD, form=EBSOVA.SUMMARY_DROP[t].upper())
            self.ebsova.copy_table_validate()
            for c in range(2):
                self.ebsova.test_sort(c)
            self.ebsova.scroll_top()

    def test_d_cat_churn_tab(self):
        self.ebsova.cat_churn_tab()
        self.ebsova.dropdown_validate(EBSOVA.CAT_DROP[0])
        for d in range(3):
            self.ebsova.select_dropdown(d, EBSOVA.CAT_DROP[d])
            for t in range(2):
                self.ebsova.toggle_buttons[t].click()
                self.ebsova.legend_validate(EBSOVA.CAT_LEG_CG)
                self.ebsova.download_diagram()
                self.ebsova.headers_validate(
                    EBSOVA.CAT_HEAD_CG, EBSOVA.CAT_DROP[d].upper(), form=EBSOVA.SUMMARY_DROP[t].upper())
                self.ebsova.copy_table_validate()
                for c in range(8):
                    self.ebsova.test_sort(c)
                self.ebsova.scroll_top()

    def test_e_cat_exp_con_tab(self):
        self.ebsova.cat_exp_con_tab()
        self.ebsova.dropdown_validate(EBSOVA.CAT_DROP[0])
        for d in range(3):
            self.ebsova.select_dropdown(d, EBSOVA.CAT_DROP[d])
            for t in range(2):
                self.ebsova.toggle_buttons[t].click()
                self.ebsova.legend_validate(EBSOVA.EXP_CON_LEG_CG)
                self.ebsova.download_diagram()
                self.ebsova.headers_validate(
                    EBSOVA.CAT_HEAD_CG, EBSOVA.CAT_DROP[d].upper(), form=EBSOVA.SUMMARY_DROP[t].upper())
                self.ebsova.copy_table_validate()
                for c in range(8):
                    self.ebsova.test_sort(c)
                self.ebsova.scroll_top()

    def test_f_brand_shift_tab(self):
        self.ebsova.brand_shift_tab()
        self.ebsova.dropdown_validate(EBSOVA.SHIFT_DROP[0])
        for d in range(4):
            self.ebsova.select_dropdown(d, EBSOVA.SHIFT_DROP[d])
            for t in range(2):
                self.ebsova.toggle_buttons[t].click()
                self.ebsova.legend_validate(EBSOVA.SHIFT_LEG)
                self.ebsova.headers_validate(
                    EBSOVA.CAT_HEAD_CG, EBSOVA.SHIFT_FORM[d].upper(), form=EBSOVA.SUMMARY_DROP[t].upper())
                for c in range(8):
                    self.ebsova.test_sort(c)
                self.ebsova.scroll_top()

    def test_g_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
