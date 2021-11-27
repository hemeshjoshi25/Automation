from utils.IscE2eTestCase import IscE2eTestCase
from pageobjects.history import HistoryPage
from pageobjects.reports.pepsi_shopper_circuits import PepsiShopperCircuitsPage
from constants.enums import ReportTypes
from constants.reports.pepsi_shopper_circuits import PSC


class TestPepsiShopperCircuits(IscE2eTestCase):
    def setUp(self):
        super(TestPepsiShopperCircuits, self).setUp()
        self.history = HistoryPage(self.driver)
        self.psc = PepsiShopperCircuitsPage(self.driver)

    def test_a_nav_psc(self):
        psc = ReportTypes.PEPSI_SHOPPER_CIRCUITS.value
        title = ReportTypes.PREFIX.value + psc
        self.history.nav_link.click()
        self.history.open_most_recent(title)
        self.assertEqual(self.psc.title.text, psc + ': ' + title)

    def test_b_retailer_tab(self):
        self.psc.retailer_tab()
        self.psc.dropdown_validate(PSC.CIRCUITS_DROP[0])
        for d in range(2):
            self.psc.select_dropdown(d, PSC.CIRCUITS_DROP[d])
            self.psc.headers_validate(PSC.RET_HEAD)

    def test_c_channel_tab(self):
        self.psc.channel_tab()
        self.psc.dropdown_validate(PSC.CIRCUITS_DROP[0])
        for d in range(2):
            self.psc.select_dropdown(d, PSC.CIRCUITS_DROP[d])
            self.psc.headers_validate(PSC.CHAN_HEAD)

    def test_d_pepsi_edibles_tab(self):
        self.psc.pepsi_edibles_tab()
        self.psc.dropdown_validate(PSC.MET_DROP[0])
        for d in range(3):
            self.psc.select_dropdown(d, PSC.MET_DROP[d])
            for t in range(3):
                self.psc.toggle_buttons[t].click()
                self.psc.assertEqual(self.psc.headers()[0].text, PSC.PEP_HEAD)

    def test_e_total_edibles_tab(self):
        self.psc.total_edibles_tab()
        self.psc.dropdown_validate(PSC.MET_DROP[0])
        for d in range(3):
            self.psc.select_dropdown(d, PSC.MET_DROP[d])
            for t in range(3):
                self.psc.toggle_buttons[t].click()
                self.psc.assertEqual(self.psc.headers()[0].text, PSC.PEP_HEAD)

    def test_f_demo_tab(self):
        self.psc.demo_tab()
        self.psc.dropdown_validate(PSC.MET_DROP[0])
        for d in range(3):
            self.psc.select_dropdown(d, PSC.MET_DROP[d])
            for t in range(3):
                self.psc.toggle_buttons[t].click()
                self.psc.assertEqual(self.psc.headers()[0].text, PSC.DEMO_HEAD)

    def test_g_sub_trips_tab(self):
        self.psc.sub_trips_tab()
        self.psc.dropdown_validate(PSC.CIRCUITS_DROP[0])
        for d in range(2):
            self.psc.select_dropdown(d, PSC.CIRCUITS_DROP[d])
            self.psc.headers_validate(PSC.SUB_HEAD)

    def test_h_set_pass(self):
        # Set to Pass
        self.__class__.test_result = 'pass'
