from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.promotion_effectiveness import PromotionEffectivenessPage
from constants.enums import ReportTypes
from constants.reports.promotion_effectiveness import PE


class TestPromotionEffectiveness(IscE2eTestCase):
    def setUp(self):
        super(TestPromotionEffectiveness, self).setUp()
        self.history = HistoryPage(self.driver)
        self.pe = PromotionEffectivenessPage(self.driver)

    def test_a_nav_pe(self):
        pe = ReportTypes.PROMOTION_EFFECTIVENESS.value
        title = ReportTypes.PREFIX.value + pe
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.pe.title.text, pe + ': ' + title)

    def test_b_promo_tab(self):
        self.pe.promo_tab()
        self.pe.dropdown_validate(PE.PROMO_DROP[0])
        for d in range(2):
            self.pe.select_dropdown(d, PE.PROMO_DROP[d])
            self.pe.legend_validate(PE.PROMO_LEG[d])
            for t in range(4):
                self.pe.toggle_buttons[t].click()
                self.pe.headers_validate(PE.PROMO_STATIC_HEAD, PE.PROMO_HEAD[t], 2)
                self.pe.copy_table_validate()

    def test_c_conversion_tab(self):
        self.pe.conversion_tab()
        self.pe.tree_titles_validate(PE.CONV_TREE)

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestPromotionEffectivenessCG(IscE2eTestCase):
    def setUp(self):
        super(TestPromotionEffectivenessCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.pe = PromotionEffectivenessPage(self.driver)

    def test_a_nav_pe(self):
        pe = ReportTypes.PROMOTION_EFFECTIVENESS.value
        title = ReportTypes.PREFIX_CG.value + pe
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.pe.title.text, pe + ': ' + title)

    def test_b_promo_tab(self):
        self.pe.promo_tab()
        self.pe.dropdown_validate(PE.PROMO_DROP[0])
        for d in range(2):
            self.pe.select_dropdown(d, PE.PROMO_DROP[d])
            self.pe.legend_validate(PE.PROMO_LEG[d])
            for t in range(4):
                self.pe.toggle_buttons[t].click()
                self.pe.headers_validate(PE.PROMO_STATIC_HEAD, PE.PROMO_HEAD[t], 2)
                self.pe.copy_table_validate()

    def test_c_conversion_tab(self):
        self.pe.conversion_tab()
        self.pe.tree_titles_validate(PE.CONV_TREE)

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
