from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.report import GenericReportPage
from pageobjects.modules.settings import SettingsPage
from constants.enums import ReportTypes, Attributes, PageTitles


class ReadOnly(IscE2eTestCase):
    """Tests that public/private sharing links work"""

    def setUp(self):
        super(ReadOnly, self).setUp()
        # Initialize page objects
        self.history = HistoryPage(self.driver)
        self.report = GenericReportPage(self.driver)
        self.settings = SettingsPage(self.driver)

    def test_a_open_report(self):
        """Open the most recent [E2E] report"""
        self.history.nav_link.click()
        self.history.search.send_keys(ReportTypes.PREFIX.value)
        self.history.open_most_recent(Attributes.ANY.value)

    def test_b_click_share(self):
        """Open share/export modal"""
        self.report.share.click()
        # Wait for modal to open
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(
            (self.history.modal_title_locator), PageTitles.SHARE_MODAL.value))
        # Check for modal title
        self.assertEqual(self.report.modal_title.text, PageTitles.SHARE_MODAL.value)

    def test_c_private_share_link(self):
        """Get the private share URL"""
        self.report.ensure_private_share()
        self.__class__.pri_share_url = self.report.share_link.get_attribute(Attributes.VALUE.value)

    def test_d_public_share_link(self):
        """Get the public share URL"""
        self.report.ensure_public_share()
        self.__class__.pub_share_url = self.report.share_link.get_attribute(Attributes.VALUE.value)

    def test_e_logout(self):
        """Logout of account to check public share"""
        self.report.close_share_modal.click()
        # Wait for modal to close
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            self.settings.nav_link_locator))
        self.settings.nav_link.click()
        self.settings.logout.click()
        # Check for login button
        self.assertIsNotNone(self.login.login)

    def test_f_validate(self):
        """Check public and private URLs"""
        self.driver.get(self.__class__.pri_share_url)
        # Check for login button
        self.assertIsNotNone(self.login.login)
        self.driver.get(self.__class__.pub_share_url)
        # Check for read-only message
        self.assertIsNotNone(self.report.read_only_message)
        # Set to Pass
        self.__class__.test_result = 'pass'
