from pageobjects.modules.labs import LabsPage
from utils.IscE2eTestCase import IscE2eTestCase
from constants.enums import PageTitles, ReportTypes


class LabsNav(IscE2eTestCase):
    """Tests Navigation to each report within Labs Module"""

    def setUp(self):
        super(LabsNav, self).setUp()
        # Initialize page objects for Labs Page
        self.labs = LabsPage(self.driver)
        # Navigate to Labs Module
        self.labs.nav_link.click()
        self.assertEqual(self.labs.title.text, PageTitles.LABS.value)
        self.labs.assert_intercom()

    def test_a_count_report(self):
        self.labs.count_report.click()
        self.labs.validate_nav(ReportTypes.COUNT_REPORT.value)

    def test_b_user_id_fetch(self):
        self.labs.user_id_fetch.click()
        self.labs.validate_nav(ReportTypes.USER_ID_FETCH.value)

    def test_c_promo_pg(self):
        self.labs.promo_pg.click()
        self.labs.validate_nav(ReportTypes.PROMO_PG.value)

    def test_d_survey_sample(self):
        self.labs.survey_sample.click()
        self.labs.validate_nav(ReportTypes.SURVEY_SAMPLE.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
