from pageobjects.report import GenericReportPage
from constants.enums import ReportTabs


class MomentsOfTruthPage(GenericReportPage):

    def __init__(self, driver):
        super(MomentsOfTruthPage, self).__init__(driver)

    def summary_tab(self):
        self.tabs(0)
        self.is_active_tab(ReportTabs.SUMMARY.value)

    def comp_mot_tab(self):
        self.tabs(1)
        self.is_active_tab(ReportTabs.COMP_MOT.value)

    def ex_survey_tab(self):
        self.tabs(2)
        self.is_active_tab(ReportTabs.EX_SURVEY.value)

    def comp_survey_tab(self):
        self.tabs(3)
        self.is_active_tab(ReportTabs.COMP_SURVEY.value)
