from pageobjects.modules.module import GenericModulePage
from constants.enums import NavLinks


class NewItemPage(GenericModulePage):

    @property
    def nav_link(self):
        return self.module_nav_link(NavLinks.NEW_ITEM_MOD.value)

    @property
    def new_item_tracker(self):
        return self.report_nav_link(NavLinks.NEW_ITEM_TRACKER.value)

    @property
    def new_item_sova(self):
        return self.report_nav_link(NavLinks.NEW_ITEM_SOVA.value)
