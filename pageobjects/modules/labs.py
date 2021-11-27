from pageobjects.modules.module import GenericModulePage
from constants.enums import NavLinks


class LabsPage(GenericModulePage):

    @property
    def nav_link(self):
        return self.module_nav_link(NavLinks.LABS_MOD.value)

    @property
    def count_report(self):
        return self.report_nav_link(NavLinks.COUNT_REPORT.value)

    @property
    def user_id_fetch(self):
        return self.report_nav_link(NavLinks.USER_ID_FETCH.value)

    @property
    def promo_pg(self):
        return self.report_nav_link(NavLinks.PROMO_PG.value)

    @property
    def survey_sample(self):
        return self.report_nav_link(NavLinks.SURVEY_SAMPLE.value)

    @property
    def high_med_low(self):
        return self.report_nav_link(NavLinks.HIGH_MED_LOW.value)
