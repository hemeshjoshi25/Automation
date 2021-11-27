from time import sleep
import clipboard
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from utils.decorators import retry_on_no_element, retry_on_stale_element
from utils.parse_args import parse_args
from pageobjects.table import GenericReportTable
from constants.enums import Selectors


class GenericReportPage(GenericReportTable):

    def __init__(self, driver):
        super(GenericReportPage, self).__init__(driver)
        self.driver = driver
        _, self.target, _, _, _ = parse_args()

    # Returns report page title element
    @property
    def title(self):
        return self.driver.find_element_by_css_selector(Selectors.REPORT_TITLE.value)

    # Returns modal title element
    @property
    def modal_title(self):
        return self.driver.find_element_by_css_selector(Selectors.MODAL_TITLE.value)

    # Returns a report tab element
        # idx = index of tab to return
    @retry_on_stale_element
    def tabs(self, idx=0):
        try:
            self.driver.find_elements_by_css_selector(Selectors.TAB.value)[idx].click()
        except WebDriverException:
            self.driver.find_elements_by_css_selector(Selectors.TAB.value)[idx].click()

    @property
    def tab_page_locator(self):
        return (By.CSS_SELECTOR, Selectors.TAB_PAGE.value)

    # Validates the active tab is the one expected
        # name = title of active tab
    @retry_on_stale_element
    def is_active_tab(self, name):
        WebDriverWait(self.driver, 300).until(EC.presence_of_element_located(self.tab_page_locator))
        if self.driver.find_element_by_css_selector(Selectors.ACTIVE_TAB.value).text == name:
            return
        raise Exception('<{}> is not the active tab'.format(name))

    # Returns all Dropdown Selector Elements
        # idx = index of dropdown to return
    def dropdown_selectors(self, idx=None):
        dds = self.driver.find_elements_by_css_selector(Selectors.DROPDOWN_SELECTOR.value)
        if idx is None:
            return dds
        else:
            return dds[idx]

    @property
    def dropdown_locator(self):
        return (By.CSS_SELECTOR, Selectors.DROPDOWN_SELECTOR.value)

    # Returns all option elements from open dropdown
        # idx = index of dropdown option to return
    def dropdown_options(self, idx=None):
        ops = []
        for o in self.driver.find_elements_by_css_selector(Selectors.DROPDOWN_OPTION.value):
            if o.text == '':
                continue
            else:
                ops.append(o)
        if idx is None:
            return ops
        else:
            return ops[idx]

    # Validates a dropdown has the correct option selected:
        # name = Text of expected selection
        # idx = Index of Dropdown, defaults to 0
    @retry_on_stale_element
    def dropdown_validate(self, name, idx=0):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(self.dropdown_locator))
        if self.dropdown_selectors(idx).text == name:
            return
        raise Exception('Dropdown did not select <{}> as expected. <{}> is currently selected'.format(
            name, self.dropdown_selectors(idx).text))

    # Try/Except function for clicking on a blocked element
        # element = clickable element that is currently blocked
    def wait_for_hover(self, element):
        try:
            element.click()
        # Exception for something blocking element
        except WebDriverException:
            ActionChains(self.driver).move_to_element(element).perform()
            sleep(1)  # Wait for until block is gone
            element.click()

    # Select an option from a dropdown:
        # option_idx = Index of option to select
        # drop_idx = Index of dropdown to select from
    @retry_on_no_element
    @retry_on_stale_element
    def select_dropdown(self, option_idx, name, drop_idx=0):
        self.wait_for_hover(self.dropdown_selectors(drop_idx))
        self.wait_for_hover(self.dropdown_options(option_idx))
        self.dropdown_validate(name, drop_idx)

    # Returns all toggle button elements
    @property
    def toggle_buttons(self):
        return self.driver.find_elements_by_css_selector(Selectors.TOGGLE_BTN.value)

    # Returns all legend label elements
    @property
    def legend_labels(self):
        return self.driver.find_elements_by_css_selector(Selectors.LEGEND_LABEL.value)

    # Returns all legend label elements (highcharts)
    @property
    def highcharts_legend_labels(self):
        return self.driver.find_elements_by_css_selector(Selectors.HIGH_LEGEND_LABEL.value)

    # Formats legend labels to be correctly formatted
        # legend = list of expected legend label values
        # form = text to be formatted into the legend labels
    def format_legend(self, legend, form):
        leg = []
        for l in legend:
            leg.append(l.format(form))
        return leg

    # Validates that legend label text is as expected
        # legend = list of expected legend label values
        # form = format text if legend label needs to be formatted
    @retry_on_stale_element
    def legend_validate(self, legend, form=None):
        if form is not None:
            legend = self.format_legend(legend, form)
        for leg in self.legend_labels:
            if leg.text not in legend:
                raise Exception('<{}> is not an expected legend value'.format(leg.text))

    # Validates that legend label text is as expected (highchartss)
        # legend = list of expected legend label values
        # form = format text if legend label needs to be formatted
    @retry_on_stale_element
    def highcharts_legend_validate(self, legend, form=None):
        if form is not None:
            legend = self.format_legend(legend, form)
        for leg in self.highcharts_legend_labels:
            if leg.text not in legend:
                raise Exception('<{}> is not an expected legend value'.format(leg.text))

    # Returns all chart label elements
    @property
    def chart_labels(self):
        return self.driver.find_elements_by_css_selector(Selectors.CHART_LEGEND.value)

    # Validates that chart label text is as expected
        # legend = list of expected legend label values
    @retry_on_stale_element
    def chart_legend_validate(self, legend):
        for l, leg in enumerate(legend):
            if leg is None:
                continue
            if self.chart_labels[l].text not in legend:
                raise Exception('Chart Label <{}> does not equal <{}> as expected'.format(
                    self.chart_labels[l].text, leg))

    # Returns all tree title elements
    def tree_titles(self):
        return self.driver.find_elements_by_xpath(Selectors.TREE_TITLES.value)

    # Validates that the titles of a tree are as expected
        # titles = list of expected tree title values
        # form = format text if tree title needs to be formatted
    def tree_titles_validate(self, titles, form=None):
        for t, title in enumerate(self.tree_titles()):
            if title.text != titles[t].format(form):
                raise Exception('Tree Title <{}> does not equal <{}> as expected'.format(
                    titles[t].format(form), title.text))

    # Returns all card title elements
    def card_titles(self):
        return self.driver.find_elements_by_xpath(Selectors.CARD_TITLES.value)

    # Validates that the titles of a card are as expected
        # titles = list of expected card title values
    def card_titles_validate(self, titles, form=None):
        for t, title in enumerate(self.card_titles()):
            if title.text != titles[t].format(form):
                raise Exception('Card Title <{}> does not equal <{}> as expected'.format(
                    title.text, titles[t].format(form)))

    # Returns the copy table button element
    @property
    def copy_table(self):
        return self.driver.find_elements_by_css_selector(Selectors.COPY_TABLE.value)

    # Clicks on the copy table button
        # table_idx = index of table to copy
    def copy_table_click(self, table_idx=0):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, Selectors.COPY_TABLE.value), 'Copy Table'))
        try:
            self.copy_table[table_idx].click()
        except WebDriverException:
            self.scroll_down()
        if self.copy_table[table_idx].text != 'Copied to Clipboard':
            self.scroll_down()
            self.copy_table[table_idx].click()

    # Formats and returns a list of properly formatted cells from the clipboard
    def format_clipboard(self):
        clip = clipboard.paste().rstrip().split('\n')
        table = []
        for c in clip:
            table.append(c.lstrip().split('\t'))
        cells = []
        for r, row in enumerate(table):
            if r == 0:
                continue  # Skip header row
            else:
                for cell in row:
                    cells.append(cell.rstrip())
        return cells

    # Clicks copy table button and validates clipboard matches table
        # table_idx = index of table on page, default is 0
    @retry_on_stale_element
    def copy_table_validate(self, table_idx=0):
        if self.target == 'CBT':
            return
        self.copy_table_click(table_idx)
        for c, cell in enumerate(self.format_clipboard()):
            table = self.tables()[table_idx]
            table_cell = self.get_cells(table)[c].text
            if None in [table_cell, cell]:
                continue
            if table_cell != cell:
                raise Exception('Copied table cell <{}> does not equal <{}> as expected'.format(
                    cell, table_cell))

    # Returns the download diagram button
    @property
    def download_button(self):
        return self.driver.find_element_by_css_selector(Selectors.DOWNLOAD_BUTTON.value)

    # Clicks download button and checks that the image canvas was created
    def download_diagram(self):
        if self.target == 'CBT':
            return
        self.download_button.click()
        if not self.driver.find_element_by_css_selector(Selectors.DIAGRAM_CANVAS.value):
            raise Exception('Download Diagram canvas was not created')
        sleep(1)  # Wait for download to happen

    @property
    def share(self):
        return self.driver.find_element_by_css_selector(Selectors.SHARE.value)

    @property
    def share_link(self):
        return self.driver.find_element_by_css_selector(Selectors.SHARE_LINK.value)

    @property
    def share_toggle(self):
        return self.driver.find_element_by_css_selector(Selectors.SHARE_TOGGLE.value)

    @property
    def public_share_message(self):
        return self.driver.find_elements_by_css_selector(Selectors.PUB_SHARE_MESSAGE.value)

    def ensure_private_share(self):
        if len(self.public_share_message) != 0:
            self.share_toggle.click()
        WebDriverWait(self.driver, 20).until_not(EC.presence_of_element_located(
            (By.CSS_SELECTOR, Selectors.PUB_SHARE_MESSAGE.value)))

    def ensure_public_share(self):
        self.ensure_private_share()
        self.share_toggle.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, Selectors.PUB_SHARE_MESSAGE.value)))

    @property
    def close_share_modal(self):
        return self.driver.find_element_by_css_selector(Selectors.MODAL_CLOSE.value)

    @property
    def read_only_message(self):
        return self.driver.find_element_by_css_selector(Selectors.READ_ONLY_MESSAGE.value)
