from pageobjects.modules.module import GenericModulePage
from constants.enums import NavLinks


class ToolsPage(GenericModulePage):

    @property
    def nav_link(self):
        return self.module_nav_link(NavLinks.TOOLS_MOD.value)

    @property
    def product_hierarchy(self):
        return self.report_nav_link(NavLinks.PRODUCT_HIERARCHY.value)

    @property
    def store_hierarchy(self):
        return self.report_nav_link(NavLinks.STORE_HIERARCHY.value)

    @property
    def pepsi_shopper_circuits(self):
        return self.report_nav_link(NavLinks.PEPSI_SHOPPER_CIRCUITS.value)
