from pageobjects.modules.instant_surveys import InstantSurveysPage
from utils.IscE2eTestCase import IscE2eTestCase
from constants.enums import PageTitles, ReportTypes


class SurveysNav(IscE2eTestCase):
    """Tests Navigation to each survey within Instant Surveys"""

    def setUp(self):
        super(SurveysNav, self).setUp()
        # Initialize page objects for Instant Survey Page
        self.surveys = InstantSurveysPage(self.driver)
        # Navigate to Instant Surveys
        self.surveys.nav_link.click()
        self.assertEqual(self.surveys.title.text, PageTitles.INSTANT_SURVEYS.value)
        self.surveys.assert_intercom()

    def test_a_leakage(self):
        self.surveys.leakage.click()
        self.surveys.validate_nav(ReportTypes.LEAKAGE.value)

    def test_b_lapsing_brand(self):
        self.surveys.lapsing_brand.click()
        self.surveys.validate_nav(ReportTypes.LAPSING_BRAND.value)

    def test_c_concept_screening(self):
        self.surveys.concept_screening.click()
        self.surveys.validate_nav(ReportTypes.CONCEPT_SCREENING.value)

    def test_d_quick_pulse(self):
        self.surveys.quick_pulse.click()
        self.surveys.validate_nav(ReportTypes.QUICK_PULSE.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
