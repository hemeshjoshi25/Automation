from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class BrandSwitchingPage(GenericReportPage):

    def __init__(self, driver):
        super(BrandSwitchingPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def switching_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.SWITCHING.value)

    def gain_loss_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.GAIN_LOSS.value)

    def share_spend_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.SHARE_SPEND.value)

    def sub_headers_validate(self, headers, form, sub=None):
        for h, hdr in enumerate(self.headers()):
            if sub is None:
                sub = form
            if h == 4:
                self.assertEqual(hdr.text, headers[h].format(sub, sub))
            else:
                self.assertEqual(hdr.text, headers[h].format(form))
