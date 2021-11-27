from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.decorators import retry_on_no_element, retry_on_stale_element, update_implicit_timeout
from constants.enums import Selectors, Attributes, PromptElements


class GenericPromptPage(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.find_element_by_css_selector(Selectors.REPORT_TITLE.value)

    @property
    def cancel_button(self):
        buttons = self.driver.find_elements_by_css_selector(Selectors.REPORT_BUTTON.value)
        cancel_btn = [b for b in buttons if b.text == PromptElements.CANCEL.value]
        if len(cancel_btn) != 1:
            raise ValueError('More than one cancel button on prompt page')
        return cancel_btn[0]

    @property
    def run_report_button(self):
        return self.driver.find_elements_by_css_selector(Selectors.REPORT_BUTTON.value)[1]

    @property
    def report_running(self):
        return self.driver.find_element_by_css_selector(Selectors.REPORT_RUNNING.value)

    @property
    def advanced_options(self):
        return self.driver.find_element_by_css_selector(Selectors.ADV_OPTIONS.value)

    @property
    def get_adv_filters(self):
        return self.driver.find_elements_by_css_selector(Selectors.ADV_FILTER.value)

    @property
    @retry_on_no_element
    @retry_on_stale_element
    def search_field(self):
        return self.driver.find_element_by_css_selector(Selectors.SEARCHBOX.value)

    def get_num_prompts(self, name):
        prompts = self.driver.find_elements_by_css_selector(Selectors.PROMPT.value)
        prompt = [p for p in prompts if p.text == name]
        return len(prompt)

    @property
    def prompt_locator(self):
        return (By.CSS_SELECTOR, Selectors.PROMPT.value)

    @retry_on_no_element
    @retry_on_stale_element
    def get_prompt(self, name, idx=None):
        num = self.get_num_prompts(name)
        prompts = self.driver.find_elements_by_css_selector(Selectors.PROMPT.value)
        prompt = [p for p in prompts if p.text == name]
        if idx is None:
            return prompt[num - 1]
        else:
            return prompt[idx]

    def get_folder(self, name):
        folders = self.driver.find_elements_by_css_selector(Selectors.FOLDER.value)
        folder = [f for f in folders if f.text == name]
        if len(folder) != 1:
            raise ValueError('More than one folder in get_folder')
        return folder[0]

    @property
    def get_all_inputs(self):
        return self.driver.find_elements_by_css_selector(Selectors.INPUT.value)

    @property
    def input_locator(self):
        return (By.CSS_SELECTOR, Selectors.INPUT.value)

    @update_implicit_timeout(30)
    def get_input(self, name):
        selections = self.get_all_inputs
        selection = [s for s in selections if s.text == name]
        if len(selection) != 1:
            raise ValueError(f'More than one input with name {name}')
        return selection[0]

    @update_implicit_timeout(30)
    def get_hierarchy_search_results(self, hierarchy_name, element_name):
        """Will return the clickable link of the hierarchy search result. If the result is a
        breadcrumb, the string you pass should put ' > ' in place of the arrows.
        e.g. for 'Household --> Laundry' search 'Household > Laundry'
        """
        # Some results take much longer than the rest of the app to load
        # Increase implicit wait for just this method by use of decorator
        results = self.driver.find_elements_by_class_name(Attributes.RESULT.value)
        for result in results:
            result_hierarchy_name = result.find_element_by_class_name(Selectors.HIERARCHY_NAME.value)
            if result_hierarchy_name.text == hierarchy_name:
                elements = result.find_elements_by_css_selector(Selectors.PROMPT_ELEMENT.value)
                for element in elements:
                    text = ' > '.join([e.text for e in element.find_elements_by_tag_name(Attributes.TAG_LI.value)])
                    if text == element_name:
                        return element.find_element_by_tag_name(Attributes.TAG_UL.value)

    @property
    def breadcrumbs(self):
        return self.driver.find_elements_by_css_selector(Selectors.BREADCRUMBS.value)

    @property
    def custom_date_fields(self):
        return self.driver.find_elements_by_css_selector(Selectors.CUSTOM_DATE.value)

    def clear_prompt(self, name, idx=None):
        prompt = self.get_prompt(name, idx)
        return prompt.find_element_by_css_selector(Selectors.CLEAR_PROMPT.value)

    @property
    def alert_text(self):
        return self.driver.find_element_by_css_selector(Selectors.ALERT_TEXT.value)

    @property
    def ranked_attributes(self):
        return self.driver.find_elements_by_css_selector(Selectors.RANK_ATTR.value)

    @property
    def ranked_attribute_up(self):
        return self.driver.find_elements_by_css_selector(Selectors.RANK_ATTR_UP.value)

    @property
    def ranked_attribute_down(self):
        return self.driver.find_elements_by_css_selector(Selectors.RANK_ATTR_DOWN.value)

    def try_click(self, element):
        try:
            element.click()
        except WebDriverException:
            self.driver.find_element_by_css_selector(Selectors.BODY.value).send_keys(Keys.DOWN)
            sleep(0.5)  # Wait for scroll
            element.click()

    def attribute_ranker(self, list, up_list, down_list):
        for l, li in enumerate(list):
            if self.ranked_attributes[l].text != li:
                raise Exception('Cannot find <{}> in attribute ranker, or attribute ranker is out of order'.format(li))
        for up in up_list:
            self.try_click(self.ranked_attribute_up[up])
            list[up], list[up - 1] = list[up - 1], list[up]
        for down in down_list:
            self.try_click(self.ranked_attribute_down[down])
            list[down], list[down + 1] = list[down + 1], list[down]
        for l, li in enumerate(list):
            if self.ranked_attributes[l].text != li:
                raise Exception('Cannot find <{}> in attribute ranker, or attribute ranker is out of order'.format(li))

    def get_dropdown_options(self):
        return self.driver.find_elements_by_css_selector(Selectors.DROPDOWN_OPTION.value)

    def dropdown_option(self, name):
        for do in self.get_dropdown_options():
            if do.text == name:
                return do
        raise Exception('Did not find <{}> in dropdown option'.format(name))

    @property
    def warning_modal(self):
        return self.driver.find_element_by_css_selector(Selectors.MODAL_WARNING.value)

    @property
    def modal_button(self):
        return self.driver.find_element_by_css_selector(Selectors.MODAL_BUTTON.value)

    def validate_prompt(self, name, idx=None):
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.input_locator))
        if Attributes.SELECTED.value in self.get_prompt(name, idx).get_attribute(Attributes.CLASS.value):
            return
        raise Exception('Prompt <{}> was not validated'.format(name))

    def bin_width(self):
        return self.driver.find_elements_by_css_selector(Selectors.BIN_WIDTH.value)

    def bin_lower(self):
        return self.driver.find_elements_by_css_selector(Selectors.BIN_LOWER.value)

    def bin_upper(self):
        return self.driver.find_elements_by_css_selector(Selectors.BIN_UPPER.value)

    def get_bin_input(self, bin):
        if bin.lower() == 'width':
            return self.bin_width()
        elif bin.lower() == 'lower':
            return self.bin_lower()
        elif bin.lower() == 'upper':
            return self.bin_upper()
        else:
            raise Exception('<{}> is not an expected bin'.format(bin))

    @property
    def bin_high(self):
        return self.driver.find_element_by_css_selector(Selectors.BIN_HIGH.value)

    @property
    def bin_med(self):
        return self.driver.find_element_by_css_selector(Selectors.BIN_MED.value)

    @property
    def bin_low(self):
        return self.driver.find_element_by_css_selector(Selectors.BIN_LOW.value)
