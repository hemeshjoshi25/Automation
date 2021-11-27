from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.bricks_clicks import BricksClicksPage
from constants.enums import ReportTypes
from constants.reports.bricks_clicks import BC


class TestBricksClicks(IscE2eTestCase):
    def setUp(self):
        super(TestBricksClicks, self).setUp()
        self.history = HistoryPage(self.driver)
        self.bc = BricksClicksPage(self.driver)

    def test_a_nav_bc(self):
        bc = ReportTypes.BRICKS_AND_CLICKS.value
        title = ReportTypes.PREFIX.value + bc
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.bc.title.text, bc + ': ' + title)

    def test_b_summary_tab(self):
        self.bc.summary_tab()
        self.bc.tree_titles_validate(BC.TREE_TITLES)
        self.bc.download_diagram()

    def test_c_channel_tab(self):
        self.bc.channel_tab()
        self.bc.dropdown_validate(BC.BUYER_DROP[0])
        for d in range(2):
            self.bc.select_dropdown(d, BC.BUYER_DROP[d])
            for t in range(3):
                self.bc.toggle_buttons[t].click()
                self.bc.legend_validate(BC.CHAN_LEG, BC.MET_TOG[t])
                self.bc.headers_validate(BC.CHAN_HEAD, form=BC.MET_TOG[t].upper())
                self.bc.copy_table_validate()
                for c in range(6):
                    self.bc.test_sort(c)
                self.bc.scroll_top()

    def test_d_brand_tab(self):
        self.bc.brand_tab()
        self.bc.dropdown_validate(BC.BUYER_DROP[0])
        for d in range(2):
            self.bc.select_dropdown(d, BC.BUYER_DROP[d])
            for t in range(3):
                self.bc.toggle_buttons[t].click()
                self.bc.legend_validate(BC.BRAND_LEG, BC.MET_TOG[t])
                self.bc.headers_validate(BC.BRAND_HEAD, form=BC.MET_TOG[t].upper())
                for c in range(7):
                    self.bc.test_sort(c)
                self.bc.scroll_top()

    def test_e_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestBricksClicksCG(IscE2eTestCase):
    def setUp(self):
        super(TestBricksClicksCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.bc = BricksClicksPage(self.driver)

    def test_a_nav_bc(self):
        bc = ReportTypes.BRICKS_AND_CLICKS.value
        title = ReportTypes.PREFIX_CG.value + bc
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.bc.title.text, bc + ': ' + title)

    def test_b_summary_tab(self):
        self.bc.summary_tab()
        self.bc.tree_titles_validate(BC.TREE_TITLES_CG)
        self.bc.download_diagram()

    def test_c_channel_tab(self):
        self.bc.channel_tab()
        self.bc.dropdown_validate(BC.BUYER_DROP_CG[0])
        for d in range(2):
            self.bc.select_dropdown(d, BC.BUYER_DROP_CG[d])
            for t in range(3):
                self.bc.toggle_buttons[t].click()
                self.bc.legend_validate(BC.CHAN_LEG, BC.MET_TOG[t])
                self.bc.headers_validate(BC.CHAN_HEAD, form=BC.MET_TOG[t].upper())
                self.bc.copy_table_validate()
                for c in range(6):
                    self.bc.test_sort(c)
                self.bc.scroll_top()

    def test_d_brand_tab(self):
        self.bc.brand_tab()
        self.bc.dropdown_validate(BC.BUYER_DROP_CG[0])
        for d in range(2):
            self.bc.select_dropdown(d, BC.BUYER_DROP_CG[d])
            for t in range(3):
                self.bc.toggle_buttons[t].click()
                self.bc.legend_validate(BC.BRAND_LEG, BC.MET_TOG[t])
                self.bc.headers_validate(BC.BRAND_HEAD_CG, form=BC.MET_TOG[t].upper())
                for c in range(7):
                    self.bc.test_sort(c)
                self.bc.scroll_top()

    def test_e_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
