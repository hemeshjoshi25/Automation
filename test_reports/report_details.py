from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from constants.enums import PageTitles, ReportTypes, PromptElements
from constants.prompt_selections import STH


class ReportDetails(IscE2eTestCase):

    def setUp(self):
        super(ReportDetails, self).setUp()
        # Initialize page objects for History Page
        self.history = HistoryPage(self.driver)

    def test_a_nav_history(self):
        """Navigate to history page"""
        self.history.nav_link.click()
        self.assertEqual(self.history.title.text, PageTitles.HISTORY.value)

    def test_b_open_details(self):
        """Open most recent E2E Store Hierarchy details modal"""
        report = ReportTypes.PREFIX.value + ReportTypes.STORE_HIERARCHY.value
        self.history.search.send_keys(report)
        self.history.get_row_options(report).click()
        # Wait for row options to display
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.history.row_options_locator))
        self.history.option_details.click()
        # Wait for details modal to open
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.history.details_title_locator))

    def test_c_validate_details(self):
        """Validate report details"""
        self.assertEqual(self.history.details_prompts[0].text, PromptElements.STORE_CHANNEL.value.upper())
        self.assertEqual(self.history.details_answers[0].text, STH.STORE_LEV.value + ': ' + STH.STORE.value)

    def test_d_close_modal(self):
        """Close details modal"""
        self.history.modal_close.click()
        self.assertEqual(self.history.title.text, PageTitles.HISTORY.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
