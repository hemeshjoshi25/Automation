from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.modules.module import GenericModulePage
from utils.decorators import retry_on_stale_element
from constants.enums import NavLinks, Selectors, Attributes


class GroupsPage(GenericModulePage):

    def __init__(self, driver):
        super(GroupsPage, self).__init__(driver)
        self.custom_filters = PGCustomFilters(driver)

    @property
    def nav_link(self):
        return self.module_nav_link(NavLinks.PG_MOD.value)

    @property
    def title(self):
        return self.driver.find_element_by_css_selector(Selectors.GROUPS_TITLE.value)

    @property
    def title_locator(self):
        return (By.CSS_SELECTOR, Selectors.GROUPS_TITLE.value)

    @property
    def people_groups(self):
        return self.driver.find_elements_by_css_selector(Selectors.GROUPS_TOGGLE.value)[0]

    @property
    def trip_groups(self):
        return self.driver.find_elements_by_css_selector(Selectors.GROUPS_TOGGLE.value)[1]

    @property
    def create(self):
        return self.driver.find_element_by_css_selector(Selectors.CREATE_GROUP_BTN.value)

    @property
    def report_header(self):
        return self.driver.find_element_by_css_selector(Selectors.REPORT_HEADER.value)

    @property
    def next_button(self):
        return self.driver.find_element_by_css_selector(Selectors.GROUPS_NEXT_BTN.value)

    @property
    def name_msg(self):
        return self.driver.find_element_by_css_selector(Selectors.GROUPS_NAME_MSG.value)

    @property
    @retry_on_stale_element
    def search_box(self):
        return self.driver.find_element_by_css_selector(Selectors.SEARCHBOX.value)

    @property
    def search_box_locator(self):
        return (By.CSS_SELECTOR, Selectors.SEARCHBOX.value)

    @property
    def get_all_rows(self):
        return self.driver.find_elements_by_css_selector(Selectors.ROW.value)

    @property
    def row_locator(self):
        return (By.CSS_SELECTOR, Selectors.ROW.value)

    @staticmethod
    def is_folder(report):
        icon_class = report.find_element_by_tag_name(Attributes.TAG_I.value).get_attribute(Attributes.CLASS.value)
        return icon_class == Selectors.ICON_CLASS.value

    def get_row_title(self, row):
        return row.find_element_by_css_selector(Selectors.ROW_NAME.value).text

    @retry_on_stale_element
    def get_rows(self, name):
        rows = []
        for row in self.get_all_rows:
            if self.is_folder(row):
                continue
            elif self.get_row_title(row) == name:
                rows.append(row)
        if rows == []:
            raise Exception('No group found, please create one')
        return rows

    @retry_on_stale_element
    def get_row_options(self, name):
        row = self.get_rows(name)[0]
        return row.find_element_by_css_selector(Selectors.MEATBALLS.value)

    @property
    def all_row_options(self):
        return self.driver.find_elements_by_xpath(Selectors.GROUPS_ROW_OPTIONS.value)

    @property
    def row_options_locator(self):
        return (By.XPATH, Selectors.GROUPS_ROW_OPTIONS.value)

    @property
    def option_details(self):
        return self.all_row_options[0]

    @property
    def option_rename(self):
        return self.all_row_options[1]

    @property
    def option_pg_share(self):
        return self.all_row_options[5]

    @property
    def option_tg_share(self):
        return self.all_row_options[4]

    @property
    @retry_on_stale_element
    def option_delete(self):
        return self.driver.find_element_by_css_selector(Selectors.ROW_DELETE.value)

    @property
    def confirm_delete(self):
        return self.driver.find_element_by_css_selector(Selectors.CONFIRM_DELETE.value)

    @property
    def delete_button_locator(self):
        return (By.CSS_SELECTOR, Selectors.CONFIRM_DELETE.value)

    def select_rows(self, name):
        rows = self.get_rows(name)
        for row in rows:
            row.find_element_by_css_selector(Selectors.CHECKBOX.value).click()
        if rows == []:
            raise Exception('<{}> not found, please create one'.format(name))

    @property
    def modal_title(self):
        return self.driver.find_element_by_css_selector(Selectors.MODAL_TITLE.value)

    @property
    def modal_title_locator(self):
        return (By.CSS_SELECTOR, Selectors.MODAL_TITLE.value)

    @property
    def modal_input(self):
        return self.driver.find_element_by_css_selector(Selectors.PG_MODAL_INPUT.value)

    @property
    def modal_save_btn(self):
        return self.driver.find_element_by_css_selector(Selectors.RENAME_SAVE.value)

    @property
    def custom_filter_textbox(self):
        return self.driver.find_element_by_css_selector(Selectors.METRIC_TEXTBOX.value)

    @property
    def empty_search_message(self):
        return self.driver.find_element_by_css_selector(Selectors.EMPTY_SEARCH.value)

    @property
    def share_title(self):
        return self.driver.find_element_by_css_selector(Selectors.SHARE_TITLE.value)

    @property
    def share_title_locator(self):
        return (By.CSS_SELECTOR, Selectors.SHARE_TITLE.value)

    @property
    def share_input(self):
        return self.driver.find_element_by_css_selector(Selectors.SHARE_INPUT.value)

    @property
    def share_input_locator(self):
        return (By.CSS_SELECTOR, Selectors.SHARE_INPUT.value)

    def get_share_users(self):
        return self.driver.find_elements_by_css_selector(Selectors.SHARE_USER.value)

    @property
    def share_user_locator(self):
        return (By.CSS_SELECTOR, Selectors.SHARE_USER.value)

    def share_user(self, user):
        for u in self.get_share_users():
            if u.text == user:
                WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, Selectors.SHARE_CHECK.value)))
                return u.find_element_by_css_selector(Selectors.SHARE_CHECK.value)
        raise Exception('Cannot find <{}> in list of sharable users'.format(user))

    @property
    def share_button(self):
        return self.driver.find_element_by_css_selector(Selectors.SHARE_BUTTON.value)

    @property
    def share_button_locator(self):
        return (By.CSS_SELECTOR, Selectors.SHARE_BUTTON.value)

    def get_share_toggles(self):
        return self.driver.find_elements_by_css_selector(Selectors.GROUPS_SHARE.value)

    @property
    def shared_with(self):
        return self.get_share_toggles()[2]

    @property
    def details_title(self):
        return self.driver.find_element_by_css_selector(Selectors.DETAILS_TITLE.value)

    @property
    def details_title_locator(self):
        return (By.CSS_SELECTOR, Selectors.DETAILS_TITLE.value)

    @property
    def details_description(self):
        return self.driver.find_element_by_css_selector(Selectors.DETAILS_DESCRIPTION.value)

    @property
    def details_prompts(self):
        return self.driver.find_elements_by_css_selector(Selectors.DETAILS_PROMPT.value)

    @property
    def details_answers(self):
        return self.driver.find_elements_by_css_selector(Selectors.DETAILS_ANSWERS.value)

    def validate_details_prompts(self, prompts):
        for dp, prompt in enumerate(self.details_prompts):
            if prompt.text == (prompts[dp]).upper():
                continue
            else:
                raise Exception('<{}> does not equal <{}>, please check prompts manually'.format(
                    prompt.text, prompts[dp]))

    def validate_details_answers(self, answers):
        for da, answer in enumerate(self.details_answers):
            if answer.text == (answers[da]):
                continue
            else:
                raise Exception('<{}> does not equal <{}>, please check answers manually'.format(
                    answer.text, answers[da]))

    @property
    def modal_close(self):
        return self.driver.find_element_by_css_selector(Selectors.MODAL_CLOSE.value)

    @property
    def filter_dropdown(self):
        return self.driver.find_element_by_css_selector(Selectors.FILTER_DROPDOWN.value)

    @property
    def close_message(self):
        return self.driver.find_element_by_css_selector(Selectors.CLOSE_MESSAGE.value)


class PGCustomFilters:

    TOTAL_TRIP_COUNT = 0
    LARGEST_BSKT_SIZE = 1
    TOTAL_ITEM_SPEND = 2
    TOTAL_ITEM_UNITS = 3
    UNIQUE_RETAILERS_SHOPPED = 4
    UNIQUE_BANNERS_SHOPPED = 5

    def __init__(self, driver):
        self.driver = driver

    @property
    def options_list(self):
        return self.driver.find_elements_by_css_selector(Selectors.OPTION_LIST.value)

    @property
    def total_trip_count(self):
        return self.options_list[PGCustomFilters.TOTAL_TRIP_COUNT]

    @property
    def largest_bsket_size(self):
        return self.options_list[PGCustomFilters.LARGEST_BSKT_SIZE]

    @property
    def total_item_spend(self):
        return self.options_list[PGCustomFilters.TOTAL_ITEM_SPEND]

    @property
    def total_item_units(self):
        return self.options_list[PGCustomFilters.TOTAL_ITEM_UNITS]

    @property
    def unique_retailers_shopped(self):
        return self.options_list[PGCustomFilters.UNIQUE_RETAILERS_SHOPPED]

    @property
    def unique_banners_shopped(self):
        return self.options_list[PGCustomFilters.UNIQUE_BANNERS_SHOPPED]
