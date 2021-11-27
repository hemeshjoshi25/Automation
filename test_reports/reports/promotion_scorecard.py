from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.promotion_scorecard import PromotionScorecardPage
from constants.enums import ReportTypes
from constants.reports.promotion_scorecard import PROS


class TestPromotionScorecard(IscE2eTestCase):
    def setUp(self):
        super(TestPromotionScorecard, self).setUp()
        self.history = HistoryPage(self.driver)
        self.pros = PromotionScorecardPage(self.driver)

    def test_a_nav_pros(self):
        pros = ReportTypes.PROMOTION_SCORECARD.value
        title = ReportTypes.PREFIX.value + pros
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.pros.title.text, pros + ': ' + title)

    def test_b_promo_tab(self):
        self.pros.promo_tab()
        self.pros.headers_validate(PROS.PROMO_HEAD)
        for c in range(4):
            self.pros.test_sort(c)
        self.pros.test_sort(6)

    def test_c_increment_tab(self):
        self.pros.increment_tab()
        self.pros.dropdown_validate(PROS.INCREMENT_DROP[0])
        for d in range(6):
            self.pros.select_dropdown(d, PROS.INCREMENT_DROP[d])
            for dd in range(2):
                self.pros.select_dropdown(dd, PROS.MET_DROP[dd], 2)
                self.pros.legend_validate(PROS.INCREMENT_LEG[d])
                self.pros.headers_validate(PROS.INCREMENT_HEAD, form=PROS.MET_FORMAT[dd])
                for c in range(4):
                    self.pros.test_sort(c)
                for c in range(5, 10):
                    self.pros.test_sort(c)
                self.pros.scroll_top()

    def test_d_increment_detail_tab(self):
        self.pros.increment_detail_tab()
        for t in range(2):
            self.pros.toggle_buttons[t].click()
            self.pros.headers_validate(PROS.DETAIL_HEAD[t])
            for c in range(4):
                self.pros.test_sort(c)
            for c in range(5, 10):
                self.pros.test_sort(c)

    def test_e_brand_switch_tab(self):
        self.pros.brand_switch_tab()
        self.pros.headers_validate(PROS.SWITCH_HEAD)
        for c in range(4):
            self.pros.test_sort(c)

    def test_f_brand_detail_tab(self):
        self.pros.brand_detail_tab()
        self.pros.dropdown_validate(PROS.SWITCH_DETAIL_DROP[0], 1)
        for d in range(3):
            self.pros.select_dropdown(d, PROS.SWITCH_DETAIL_DROP[d], 1)
            self.pros.headers_validate(PROS.SWITCH_DETAIL_HEAD, form=PROS.SWITCH_DETAIL_DROP[d].upper())
            self.pros.copy_table_validate()
            for c in range(4):
                self.pros.test_sort(c)
            for c in range(5, 7):
                self.pros.test_sort(c)

    def test_g_store_switch_tab(self):
        self.pros.store_switch_tab()
        self.pros.dropdown_validate(PROS.SWITCH_DETAIL_DROP[0], 1)
        for d in range(3):
            self.pros.select_dropdown(d, PROS.SWITCH_DETAIL_DROP[d], 1)
            self.pros.headers_validate(PROS.STORE_HEAD, form=PROS.SWITCH_DETAIL_DROP[d].upper())
            self.pros.copy_table_validate()
            for c in range(4):
                self.pros.test_sort(c)
            for c in range(5, 7):
                self.pros.test_sort(c)

    def test_h_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
