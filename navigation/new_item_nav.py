from pageobjects.modules.new_item import NewItemPage
from utils.IscE2eTestCase import IscE2eTestCase
from constants.enums import PageTitles, ReportTypes


class NewItemNav(IscE2eTestCase):
    """Tests Navigation to each report within New Item Insights"""

    def setUp(self):
        super(NewItemNav, self).setUp()
        # Initialize page objects for New Item Page
        self.new_item = NewItemPage(self.driver)
        # Navigate to New Item Insights
        self.new_item.nav_link.click()
        self.assertEqual(self.new_item.title.text, PageTitles.NEW_ITEM.value)
        self.new_item.assert_intercom()

    def test_a_new_item_tracker(self):
        self.new_item.new_item_tracker.click()
        self.new_item.validate_nav(ReportTypes.NEW_ITEM_TRACKER.value)

    def test_b_new_item_sova(self):
        self.new_item.new_item_sova.click()
        self.new_item.validate_nav(ReportTypes.NEW_ITEM_SOVA.value)
        # Set to Pass
        self.__class__.test_result = 'pass'
