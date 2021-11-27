from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.people_scorecard import PeopleScorecardPage
from constants.enums import ReportTypes
from constants.reports.people_scorecard import PS


class TestPeopleScorecard(IscE2eTestCase):
    def setUp(self):
        super(TestPeopleScorecard, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ps = PeopleScorecardPage(self.driver)

    def test_a_nav_ps(self):
        ps = ReportTypes.PEOPLE_SCORECARD.value
        title = ReportTypes.PREFIX.value + ps
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ps.title.text, ps + ': ' + title)

    def test_b_ps_tab(self):
        self.ps.dropdown_validate(PS.PS_DROP[0])
        for d in range(5):
            self.ps.select_dropdown(d, PS.PS_DROP[d])
            for h in range(2):
                self.ps.assertEqual(self.ps.headers()[h].text, PS.PS_HEAD[h])

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'


class TestPeopleScorecardCG(IscE2eTestCase):
    def setUp(self):
        super(TestPeopleScorecardCG, self).setUp()
        self.history = HistoryPage(self.driver)
        self.ps = PeopleScorecardPage(self.driver)

    def test_a_nav_ps(self):
        ps = ReportTypes.PEOPLE_SCORECARD.value
        title = ReportTypes.PREFIX_CG.value + ps
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.ps.title.text, ps + ': ' + title)

    def test_b_ps_tab(self):
        self.ps.dropdown_validate(PS.PS_DROP[0])
        for d in range(5):
            self.ps.select_dropdown(d, PS.PS_DROP[d])
            for h in range(2):
                self.ps.assertEqual(self.ps.headers()[h].text, PS.PS_HEAD[h])

    def test_c_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
