from pageobjects.modules.module import GenericModulePage
from constants.enums import NavLinks


class SurveysPage(GenericModulePage):

    def __init__(self, driver):
        super(SurveysPage, self).__init__(driver)

    @property
    def nav_link(self):
        """Returns link to 'Surveys' history page"""
        return self.module_nav_link(NavLinks.SURVEYS.value)
