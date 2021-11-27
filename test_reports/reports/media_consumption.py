from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.media_consumption import MediaConsumptionPage
from constants.enums import ReportTypes
from constants.reports.media_consumption import MC


class TestMediaConsumption(IscE2eTestCase):
    def setUp(self):
        super(TestMediaConsumption, self).setUp()
        self.history = HistoryPage(self.driver)
        self.mc = MediaConsumptionPage(self.driver)

    def test_a_nav_mc(self):
        mc = ReportTypes.MEDIA_CONSUMPTION.value
        title = ReportTypes.PREFIX.value + mc
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.mc.title.text, mc + ': ' + title)

    def test_b_summary_tab(self):
        self.mc.summary_tab()
        self.mc.media_validate(MC.SUMMARY_HEAD, MC.SUMMARY_TABLE)

    def test_c_watching_tab(self):
        self.mc.watch_tab()
        self.mc.media_validate(MC.WATCH_HEAD, MC.WATCH_TABLE)

    def test_d_listening_tab(self):
        self.mc.listen_tab()
        self.mc.media_validate(MC.LISTEN_HEAD, MC.LISTEN_TABLE)

    def test_e_reading_tab(self):
        self.mc.read_tab()
        self.mc.media_validate(MC.READ_HEAD, MC.READ_TABLE)

    def test_f_social_media_tab(self):
        self.mc.social_tab()
        self.mc.media_validate(MC.SOCIAL_HEAD, MC.SOCIAL_TABLE)

    def test_g_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
