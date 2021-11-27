from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.brand_switching import BrandSwitchingPage
from constants.enums import ReportTypes
from constants.reports.brand_switching import BS


class TestBrandSwitching(IscE2eTestCase):
    def setUp(self):
        super(TestBrandSwitching, self).setUp()
        self.history = HistoryPage(self.driver)
        self.bs = BrandSwitchingPage(self.driver)

    def test_a_nav_bs(self):
        bs = ReportTypes.BRAND_SWITCHING.value
        title = ReportTypes.PREFIX.value + bs
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.bs.title.text, bs + ': ' + title)

    def test_b_summary_tab(self):
        self.bs.summary_tab()
        self.bs.card_titles_validate(BS.CARD_TITLES)
        self.bs.download_diagram()

    def test_c_switching_tab(self):
        self.bs.switching_tab()
        self.bs.dropdown_validate(BS.PROD_DROP[0])
        self.bs.dropdown_validate(BS.MET_DROP[0], 1)
        for d in range(4):
            self.bs.select_dropdown(d, BS.PROD_DROP[d])
            for dd in range(6):
                self.bs.select_dropdown(dd, BS.MET_DROP[dd], 1)
                if dd == 3:
                    self.bs.legend_validate(BS.SWITCH_LEG[1], BS.MET_DROP[dd])
                else:
                    self.bs.legend_validate(BS.SWITCH_LEG[0], BS.MET_DROP[dd])
                if dd > 2:
                    self.bs.sub_headers_validate(
                        BS.SWITCH_HEAD_ETC[dd - 3], BS.MET_DROP[dd].upper(), BS.MET_DROP[dd - 3].upper())
                else:
                    self.bs.sub_headers_validate(BS.SWITCH_HEAD, BS.MET_DROP[dd].upper())
                for c in range(6):
                    self.bs.test_sort(c)
                self.bs.scroll_top()

    def test_d_gain_loss_tab(self):
        self.bs.gain_loss_tab()
        self.bs.legend_validate(BS.GRID_LEG)
        self.bs.headers_validate(BS.GRID_HEAD)
        for c in range(6):
            self.bs.test_sort(c)
        self.bs.scroll_top()

    def test_e_share_spend_tab(self):
        self.bs.share_spend_tab()
        self.bs.dropdown_validate(BS.SHARE_DROP[0])
        for d in range(5):
            self.bs.select_dropdown(d, BS.SHARE_DROP[d])
            self.bs.legend_validate([BS.SHARE_DROP[d]])
            self.bs.headers_validate(BS.SHARE_HEAD)
            for c in range(7):
                self.bs.test_sort(c)
            self.bs.scroll_top()

    def test_f_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestBrandSwitchingCG(IscE2eTestCase):
    def setUp(self):
        super(TestBrandSwitchingCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.bs = BrandSwitchingPage(self.driver)

    def test_a_nav_bs(self):
        bs = ReportTypes.BRAND_SWITCHING.value
        title = ReportTypes.PREFIX_CG.value + bs
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.bs.title.text, bs + ': ' + title)

    def test_b_summary_tab(self):
        self.bs.summary_tab()
        self.bs.card_titles_validate(BS.CARD_TITLES_CG)
        self.bs.download_diagram()

    def test_c_switching_tab(self):
        self.bs.switching_tab()
        self.bs.dropdown_validate(BS.PROD_DROP[0])
        self.bs.dropdown_validate(BS.MET_DROP[0], 1)
        for d in range(3):
            self.bs.select_dropdown(d, BS.PROD_DROP[d])
            for dd in range(6):
                self.bs.select_dropdown(dd, BS.MET_DROP[dd], 1)
                if dd == 3:
                    self.bs.legend_validate(BS.SWITCH_LEG_CG[1], BS.MET_DROP[dd])
                else:
                    self.bs.legend_validate(BS.SWITCH_LEG_CG[0], BS.MET_DROP[dd])
                if dd > 2:
                    self.bs.sub_headers_validate(
                        BS.SWITCH_HEAD_ETC_CG[dd - 3], BS.MET_DROP[dd].upper(), BS.MET_DROP[dd - 3].upper())
                else:
                    self.bs.sub_headers_validate(BS.SWITCH_HEAD_CG, BS.MET_DROP[dd].upper())
                for c in range(6):
                    self.bs.test_sort(c)
                self.bs.scroll_top()

    def test_d_gain_loss_tab(self):
        self.bs.gain_loss_tab()
        self.bs.legend_validate(BS.GRID_LEG)
        self.bs.headers_validate(BS.GRID_HEAD_CG)
        for c in range(6):
            self.bs.test_sort(c)
        self.bs.scroll_top()

    def test_e_share_spend_tab(self):
        self.bs.share_spend_tab()
        self.bs.dropdown_validate(BS.SHARE_DROP_CG[0])
        for d in range(5):
            self.bs.select_dropdown(d, BS.SHARE_DROP_CG[d])
            self.bs.legend_validate([BS.SHARE_DROP_CG[d]])
            self.bs.headers_validate(BS.SHARE_HEAD_CG)
            for c in range(7):
                self.bs.test_sort(c)
            self.bs.scroll_top()

    def test_f_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
