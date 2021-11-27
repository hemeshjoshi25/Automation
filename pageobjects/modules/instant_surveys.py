from pageobjects.modules.module import GenericModulePage
from constants.enums import NavLinks, Selectors


class InstantSurveysPage(GenericModulePage):

    @property
    def nav_link(self):
        return self.module_nav_link(NavLinks.INSTANT_SURVEYS.value)

    def survey_nav_link(self, slug):
        return self.driver.find_element_by_css_selector(Selectors.SURVEY_NAV_LINK.value.format(slug))

    @property
    def leakage(self):
        return self.survey_nav_link(NavLinks.LEAKAGE.value)

    @property
    def lapsing_brand(self):
        return self.survey_nav_link(NavLinks.LAPSING_BRAND.value)

    @property
    def concept_screening(self):
        return self.survey_nav_link(NavLinks.CONCEPT_SCREENING.value)

    @property
    def quick_pulse(self):
        return self.survey_nav_link(NavLinks.QUICK_PULSE.value)
