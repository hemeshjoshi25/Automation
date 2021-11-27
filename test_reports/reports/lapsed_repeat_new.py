from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.lapsed_repeat_new import LapsedRepeatNewPage
from constants.enums import ReportTypes
from constants.reports.lapsed_repeat_new import LRN


class TestLapsedRepeatNew(IscE2eTestCase):
    def setUp(self):
        super(TestLapsedRepeatNew, self).setUp()
        self.history = HistoryPage(self.driver)
        self.lrn = LapsedRepeatNewPage(self.driver)

    def test_a_nav_lrn(self):
        lrn = ReportTypes.LAPSED_REPEAT_NEW.value
        title = ReportTypes.PREFIX.value + lrn
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.lrn.title.text, lrn + ': ' + title)

    def test_b_total_comp_tab(self):
        self.lrn.total_comp_tab()
        for t in range(4):
            self.lrn.toggle_buttons[t].click()
            self.lrn.legend_validate(LRN.LRN_LEG, LRN.LRN_TOG[t])
            self.lrn.headers_validate(LRN.TOTAL_COMP_HEAD, form=LRN.LRN_TOG[t].upper())
            self.lrn.copy_table_validate()
            for c in range(4):
                self.lrn.test_sort(c)
            self.lrn.scroll_top()

    def test_c_comparison_tab(self):
        self.lrn.comparison_tab()
        for t in range(4):
            self.lrn.toggle_buttons[t].click()
            self.lrn.legend_validate(LRN.LRN_LEG, LRN.LRN_TOG[t])
            self.lrn.headers_validate(LRN.COMPARE_HEAD, form=LRN.LRN_TOG[t].upper())
            self.lrn.copy_table_validate()
            for c in range(5):
                self.lrn.test_sort(c)
            self.lrn.scroll_top()

    def test_d_lrn_tab(self):
        self.lrn.lrn_tab()
        for d in range(3):
            self.lrn.select_dropdown(d, LRN.LRN_DROP[d])
            self.lrn.card_titles_validate(LRN.LRN_CARDS, LRN.LRN_DROP[d])

    def test_e_store_pref(self):
        self.lrn.store_pref_tab()
        self.lrn.dropdown_validate(LRN.LRN_TOG[0], 1)
        for d in range(4):
            self.lrn.select_dropdown(d, LRN.LRN_TOG[d], 1)
            if d == 0:
                self.lrn.headers_validate(LRN.STORE_HEAD[0], form=LRN.LRN_TOG[d].upper())
                self.lrn.copy_table_validate()
            else:
                self.lrn.headers_validate(LRN.STORE_HEAD[1], form=LRN.LRN_TOG[d].upper())
                self.lrn.copy_table_validate()
            for c in range(6):
                self.lrn.test_sort(c)

    def test_f_prod_pref(self):
        self.lrn.prod_pref_tab()
        self.lrn.dropdown_validate(LRN.PROD_DROP[0], 1)
        for d in range(4):
            self.lrn.select_dropdown(d, LRN.PROD_DROP[d], 1)
            if d == 0:
                self.lrn.headers_validate(LRN.PROD_HEAD[0], form=LRN.PROD_DROP[d].upper())
            else:
                self.lrn.headers_validate(LRN.PROD_HEAD[1], form=LRN.PROD_DROP[d].upper())
            for c in range(6):
                self.lrn.test_sort(c)

    def test_g_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestLapsedRepeatNewRV(IscE2eTestCase):
    def setUp(self):
        super(TestLapsedRepeatNewRV, self).setUp()
        self.history = HistoryPage(self.driver)
        self.lrn = LapsedRepeatNewPage(self.driver)

    def test_a_nav_lrn(self):
        lrn = ReportTypes.LAPSED_REPEAT_NEW.value
        title = ReportTypes.PREFIX_RV.value + lrn
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.lrn.title.text, lrn + ': ' + title)

    def test_b_total_comp_tab(self):
        self.lrn.total_comp_tab()
        for t in range(4):
            self.lrn.toggle_buttons[t].click()
            self.lrn.legend_validate(LRN.LRN_LEG, LRN.LRN_TOG_RV[t])
            self.lrn.headers_validate(LRN.TOTAL_COMP_HEAD, form=LRN.LRN_TOG_RV[t].upper())
            self.lrn.copy_table_validate()
            for c in range(4):
                self.lrn.test_sort(c)
            self.lrn.scroll_top()

    def test_c_comparison_tab(self):
        self.lrn.comparison_tab()
        for t in range(4):
            self.lrn.toggle_buttons[t].click()
            self.lrn.legend_validate(LRN.LRN_LEG, LRN.LRN_TOG_RV[t])
            self.lrn.headers_validate(LRN.COMPARE_HEAD_RV, form=LRN.LRN_TOG_RV[t].upper())
            self.lrn.copy_table_validate()
            for c in range(5):
                self.lrn.test_sort(c)
            self.lrn.scroll_top()

    def test_d_lrn_tab(self):
        self.lrn.lrn_tab()
        for d in range(3):
            self.lrn.select_dropdown(d, LRN.LRN_DROP[d])
            self.lrn.card_titles_validate(LRN.LRN_CARDS_RV, LRN.LRN_DROP[d])

    def test_e_store_pref(self):
        self.lrn.store_pref_tab()
        self.lrn.dropdown_validate(LRN.LRN_TOG_RV[0], 1)
        for d in range(4):
            self.lrn.select_dropdown(d, LRN.LRN_TOG_RV[d], 1)
            if d == 0:
                self.lrn.headers_validate(LRN.STORE_HEAD_RV[0], form=LRN.LRN_TOG_RV[d].upper())
                self.lrn.copy_table_validate()
            else:
                self.lrn.headers_validate(LRN.STORE_HEAD_RV[1], form=LRN.LRN_TOG_RV[d].upper())
                self.lrn.copy_table_validate()
            for c in range(6):
                self.lrn.test_sort(c)

    def test_f_prod_pref(self):
        self.lrn.prod_pref_tab()
        self.lrn.dropdown_validate(LRN.PROD_DROP[0], 1)
        for d in range(4):
            self.lrn.select_dropdown(d, LRN.PROD_DROP[d], 1)
            if d == 0:
                self.lrn.headers_validate(LRN.PROD_HEAD_RV[0], form=LRN.PROD_DROP[d].upper())
            else:
                self.lrn.headers_validate(LRN.PROD_HEAD_RV[1], form=LRN.PROD_DROP[d].upper())
            for c in range(6):
                self.lrn.test_sort(c)

    def test_g_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestLapsedRepeatNewCG(IscE2eTestCase):
    def setUp(self):
        super(TestLapsedRepeatNewCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.lrn = LapsedRepeatNewPage(self.driver)

    def test_a_nav_lrn(self):
        lrn = ReportTypes.LAPSED_REPEAT_NEW.value
        title = ReportTypes.PREFIX_CG.value + lrn
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.lrn.title.text, lrn + ': ' + title)

    def test_b_total_comp_tab(self):
        self.lrn.total_comp_tab()
        for t in range(4):
            self.lrn.toggle_buttons[t].click()
            self.lrn.legend_validate(LRN.LRN_LEG, LRN.LRN_TOG[t])
            self.lrn.headers_validate(LRN.TOTAL_COMP_HEAD, form=LRN.LRN_TOG[t].upper())
            self.lrn.copy_table_validate()
            for c in range(4):
                self.lrn.test_sort(c)
            self.lrn.scroll_top()

    def test_c_comparison_tab(self):
        self.lrn.comparison_tab()
        for t in range(4):
            self.lrn.toggle_buttons[t].click()
            self.lrn.legend_validate(LRN.LRN_LEG, LRN.LRN_TOG[t])
            self.lrn.headers_validate(LRN.COMPARE_HEAD_CG, form=LRN.LRN_TOG[t].upper())
            self.lrn.copy_table_validate()
            for c in range(5):
                self.lrn.test_sort(c)
            self.lrn.scroll_top()

    def test_d_lrn_tab(self):
        self.lrn.lrn_tab()
        for d in range(3):
            self.lrn.select_dropdown(d, LRN.LRN_DROP[d])
            self.lrn.card_titles_validate(LRN.LRN_CARDS, LRN.LRN_DROP[d])

    def test_e_store_pref(self):
        self.lrn.store_pref_tab()
        self.lrn.dropdown_validate(LRN.LRN_TOG[0], 1)
        for d in range(4):
            self.lrn.select_dropdown(d, LRN.LRN_TOG[d], 1)
            if d == 0:
                self.lrn.headers_validate(LRN.STORE_HEAD[0], form=LRN.LRN_TOG[d].upper())
                self.lrn.copy_table_validate()
            else:
                self.lrn.headers_validate(LRN.STORE_HEAD[1], form=LRN.LRN_TOG[d].upper())
                self.lrn.copy_table_validate()
            for c in range(6):
                self.lrn.test_sort(c)

    def test_f_prod_pref(self):
        self.lrn.prod_pref_tab()
        self.lrn.dropdown_validate(LRN.PROD_DROP[0], 1)
        for d in range(4):
            self.lrn.select_dropdown(d, LRN.PROD_DROP[d], 1)
            if d == 0:
                self.lrn.headers_validate(LRN.PROD_HEAD_CG[0], form=LRN.PROD_DROP[d].upper())
            else:
                self.lrn.headers_validate(LRN.PROD_HEAD_CG[1], form=LRN.PROD_DROP[d].upper())
            for c in range(6):
                self.lrn.test_sort(c)

    def test_g_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
