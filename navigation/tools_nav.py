from pageobjects.modules.tools import ToolsPage
from utils.IscE2eTestCase import IscE2eTestCase
from constants.enums import PageTitles, ReportTypes


class ToolsNav(IscE2eTestCase):
    """Tests Navigation to each report within Tools Module"""

    def setUp(self):
        super(ToolsNav, self).setUp()
        # Initialize page objects for Tools Page
        self.tools = ToolsPage(self.driver)
        # Navigate to Tools Module
        self.tools.nav_link.click()
        self.assertEqual(self.tools.title.text, PageTitles.TOOLS.value)
        self.tools.assert_intercom

    def test_a_product_hierarchy(self):
        self.tools.product_hierarchy.click()
        self.tools.validate_nav(ReportTypes.PRODUCT_HIERARCHY.value)

    def test_b_store_hierarchy(self):
        self.tools.store_hierarchy.click()
        self.tools.validate_nav(ReportTypes.STORE_HIERARCHY.value)

    def test_c_pepsi_shopper_circuits(self):
        self.tools.pepsi_shopper_circuits.click()
        self.tools.validate_nav(ReportTypes.PEPSI_SHOPPER_CIRCUITS.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
