from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.event_analysis import EventAnalysisPage
from constants.enums import ReportTypes
from constants.reports.event_analysis import EA


class TestEventAnalysis(IscE2eTestCase):
    def setUp(self):
        super(TestEventAnalysis, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ea = EventAnalysisPage(self.driver)

    def test_a_nav_ea(self):
        ea = ReportTypes.EVENT_ANALYSIS.value
        title = ReportTypes.PREFIX.value + ea
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ea.title.text, ea + ': ' + title)

    def test_b_promo_tab(self):
        self.ea.promo_tab()
        self.ea.dropdown_validate(EA.PROMO_DROP[0])
        for d in range(2):
            self.ea.select_dropdown(d, EA.PROMO_DROP[d])
            self.ea.headers_validate(EA.PROMO_HEAD)
            self.ea.copy_table_validate()

    def test_c_conversion_tab(self):
        self.ea.conversion_tab()
        self.ea.tree_titles_validate(EA.TREE_TITLES)
        self.ea.download_diagram()

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestEventAnalysisCG(IscE2eTestCase):
    def setUp(self):
        super(TestEventAnalysisCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ea = EventAnalysisPage(self.driver)

    def test_a_nav_ea(self):
        ea = ReportTypes.EVENT_ANALYSIS.value
        title = ReportTypes.PREFIX_CG.value + ea
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ea.title.text, ea + ': ' + title)

    def test_b_promo_tab(self):
        self.ea.promo_tab()
        self.ea.dropdown_validate(EA.PROMO_DROP[0])
        for d in range(2):
            self.ea.select_dropdown(d, EA.PROMO_DROP[d])
            self.ea.headers_validate(EA.PROMO_HEAD)
            self.ea.copy_table_validate()

    def test_c_conversion_tab(self):
        self.ea.conversion_tab()
        self.ea.tree_titles_validate(EA.TREE_TITLES)
        self.ea.download_diagram()

    def test_d_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
