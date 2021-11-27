from selenium.webdriver.common.by import By
from utils.decorators import retry_on_stale_element, update_implicit_timeout
from pageobjects.modules.groups import GroupsPage
from constants.enums import NavLinks, Selectors


class AdvGroupsPage(GroupsPage):

    def __init__(self, driver):
        super(AdvGroupsPage, self).__init__(driver)

    @property
    def nav_link(self):
        return self.module_nav_link(NavLinks.ADV_GROUPS.value)

    @property
    def product_groups(self):
        return self.driver.find_elements_by_css_selector(Selectors.GROUPS_TOGGLE.value)[0]

    @property
    def store_groups(self):
        return self.driver.find_elements_by_css_selector(Selectors.GROUPS_TOGGLE.value)[1]

    @property
    def combo_box(self):
        return self.driver.find_element_by_css_selector(Selectors.COMBO_BOX.value)

    def list_options(self):
        return self.driver.find_elements_by_css_selector(Selectors.PG_LIST_OPTIONS.value)

    @update_implicit_timeout(15)
    def get_list_option(self, name):
        for op in self.list_options():
            if op.text.lower() == name.lower():
                return op
        raise Exception('Option <{}> not found, search manually'.format(name))

    def all_prompt_blocks(self):
        return self.driver.find_elements_by_xpath(Selectors.PROMPT_BLOCK.value)

    @retry_on_stale_element
    def get_prompt_block(self, name):
        for block in self.all_prompt_blocks():
            if block.text == name:
                return block
        raise Exception('Prompt Block <{}> not found, search manually'.format(name))

    @property
    def closed_condition(self):
        return self.driver.find_elements_by_xpath(Selectors.CLOSED_CONDITION.value)

    @property
    def modal_folder_input(self):
        return self.driver.find_elements_by_css_selector(Selectors.PG_MODAL_INPUT.value)[0]

    @property
    def modal_pg_input(self):
        return self.driver.find_elements_by_css_selector(Selectors.PG_MODAL_INPUT.value)[1]

    @property
    def modal_save_btn(self):
        return self.driver.find_elements_by_css_selector(Selectors.PG_MODAL_SAVE.value)[1]

    @property
    def modal_save_locator(self):
        return (By.CSS_SELECTOR, Selectors.PG_MODAL_SAVE.value)

    @property
    def rename_save_btn(self):
        return self.driver.find_element_by_css_selector(Selectors.PG_MODAL_SAVE.value)

    @property
    def folder_title(self):
        return self.driver.find_elements_by_css_selector(Selectors.GROUPS_TITLE.value)[1]

    def get_rows(self, name):
        rows = []
        for row in self.get_all_rows:
            if row.find_element_by_css_selector(Selectors.ROW_NAME.value).text == name:
                rows.append(row)
        if rows == []:
            raise Exception('<{}> not found, please create one'.format(name))
        return rows

    def get_row_options(self, name):
        row = self.get_rows(name)[0]
        return row.find_element_by_css_selector(Selectors.MEATBALLS.value)

    @property
    @retry_on_stale_element
    def all_row_options(self):
        return self.driver.find_elements_by_xpath(Selectors.GROUPS_FOLDER_OPTIONS.value)

    @property
    def row_options_locator(self):
        return (By.XPATH, Selectors.GROUPS_FOLDER_OPTIONS.value)

    @property
    def option_add(self):
        return self.all_row_options[0]

    @property
    def option_rename(self):
        return self.all_row_options[1]

    @property
    def option_share(self):
        return self.all_row_options[2]

    def get_row(self, name):
        for row in self.get_all_rows:
            if row.find_element_by_css_selector(Selectors.ROW_NAME.value).text == name:
                return row.find_element_by_css_selector(Selectors.FOLDER_NAME.value)
        raise Exception('<{}> not found, please create one'.format(name))

    def get_pg_row(self, name):
        for row in self.driver.find_elements_by_css_selector(Selectors.ROW_COLUMN.value):
            if row.text == name:
                return row
        raise Exception('<{}> not found, search manually'.format(name))

    def num_rows(self, name):
        num_rows = 0
        rows = self.get_rows(name)
        for row in rows:
            num_rows += 1
        return num_rows
