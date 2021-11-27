from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from utils.decorators import retry_on_no_element, retry_on_stale_element, update_implicit_timeout
from pageobjects.modules.module import GenericModulePage
from constants.enums import NavLinks, Selectors, Attributes


class HistoryPage(GenericModulePage):

    def __init__(self, driver):
        super(HistoryPage, self).__init__(driver)

    @property
    def nav_link(self):
        """Returns link to 'My Reports' history page"""
        return self.module_nav_link(NavLinks.HISTORY.value)

    @property
    def title(self):
        """Returns history page title ('ALL MY REPORTS' breadcrumb)"""
        return self.driver.find_elements_by_css_selector(Selectors.FOLDER_BREADCRUMBS.value)[0]

    @property
    def search(self):
        """Returns search input box"""
        return self.driver.find_element_by_css_selector(Selectors.SEARCHBOX.value)

    @property
    def get_all_rows(self):
        """Returns all rows on the page"""
        return self.driver.find_elements_by_css_selector(Selectors.ROW.value)

    @property
    def row_locator(self):
        return (By.CSS_SELECTOR, Selectors.ROW.value)

    @staticmethod
    def is_folder(row):
        """
        Returns true if given row is a folder, else: false
        :Args:
         - row - row from history page
        """
        icon_class = row.find_element_by_tag_name(Attributes.TAG_I.value).get_attribute(Attributes.CLASS.value)
        return icon_class == Selectors.ICON_CLASS.value

    @staticmethod
    def get_row_title(row):
        """Returns folder/report name of a given row"""
        return row.find_element_by_css_selector(Selectors.ROW_DOC_NAME.value).text

    def get_rows(self, name):
        """
        Returns all rows with a given name
        :Args:
         - name - folder/report name of row
        """
        rows = []
        for row in self.get_all_rows:
            if self.is_folder(row):
                continue
            elif self.get_row_title(row) == name:
                rows.append(row)
        if len(rows) == 0:
            raise Exception('No <{}> group found, please create one'.format(name))
        return rows

    def get_row_options(self, name):
        """
        Returns the options element for the first row with a given folder/report name
        :Args:
         - name - folder/report name of row to get options of
        """
        row = self.get_rows(name)[0]
        return row.find_element_by_css_selector(Selectors.MEATBALLS.value)

    @property
    def all_row_options(self):
        return self.driver.find_elements_by_xpath(Selectors.ROW_OPTIONS.value)

    @property
    def row_options_locator(self):
        return (By.XPATH, Selectors.ROW_OPTIONS.value)

    @property
    def option_details(self):
        return self.all_row_options[0]

    def get_report_name(self, row):
        return row.find_element_by_class_name(Selectors.REPORT_NAME.value)

    def open_most_recent(self, name=(Attributes.ANY.value)):
        table_rows = []
        while True:
            if name.lower() != Attributes.ANY.value:
                self.search.send_keys(name)
            WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(self.row_locator))
            rows = self.get_all_rows
            if set(rows).issubset(table_rows):
                raise Exception('No <{}> report found, please run one'.format(name))
            for row in rows:
                if row in table_rows:
                    continue
                if self.is_folder(row):
                    table_rows.append(row)
                    continue
                report_status = row.find_element_by_class_name(Selectors.REPORT_STATUS.value)
                report_name = self.get_report_name(row)
                report_complete = report_status.text.lower() == Attributes.COMPLETE.value
                table_rows.append(row)
                if name.lower() == Attributes.ANY.value and report_complete:
                    report_name.click()
                    return
                if report_name.text.lower() == name.lower() and report_complete:
                    for _ in range(3):
                        try:
                            report_name.click()
                            return
                        except WebDriverException:
                            self.driver.find_element_by_css_selector(Selectors.BODY.value).send_keys(Keys.PAGE_DOWN)
                            sleep(0.5)  # Wait for scroll
            self.driver.find_element_by_css_selector(Selectors.BODY.value).send_keys(Keys.PAGE_DOWN)
            sleep(0.5)  # Wait for scroll

    @retry_on_no_element
    @retry_on_stale_element
    def get_first_row(self):
        for row in self.get_all_rows:
            if self.is_folder(row):
                continue
            return row
        raise Exception("Can't find a report")

    @retry_on_no_element
    @retry_on_stale_element
    def get_first_report(self, name):
        for row in self.get_all_rows:
            if self.is_folder(row):
                continue
            elif self.get_report_name(row).text != name:
                raise Exception('<{}> is not the first report'.format(name))
            else:
                return row

    @update_implicit_timeout(15)
    def row_options(self, row):
        return row.find_element_by_css_selector(Selectors.MEATBALLS.value)

    @update_implicit_timeout(10)
    def option_rename(self):
        return self.all_row_options[3]

    @property
    def modal_title(self):
        return self.driver.find_element_by_css_selector(Selectors.MODAL_TITLE.value)

    @property
    def modal_title_locator(self):
        return (By.CSS_SELECTOR, Selectors.MODAL_TITLE.value)

    @property
    def modal_input(self):
        return self.driver.find_element_by_css_selector(Selectors.RENAME_INPUT.value)

    @property
    def modal_save(self):
        return self.driver.find_element_by_css_selector(Selectors.RENAME_SAVE.value)

    def rename_report(self, report, name):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.report_running_locator))
        self.nav_link.click()
        WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(self.row_locator))
        self.row_options(self.get_first_report(report)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.row_options_locator))
        self.option_rename().click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.modal_title_locator))
        self.modal_input.send_keys(name)
        self.modal_save.click()
        sleep(1)  # Wait for modal close animation
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.row_locator))
        self.get_first_report(name)

    @property
    def details_title(self):
        return self.driver.find_element_by_css_selector(Selectors.DETAILS_TITLE.value)

    @property
    def details_title_locator(self):
        return (By.CSS_SELECTOR, Selectors.DETAILS_TITLE.value)

    @property
    def details_prompts(self):
        return self.driver.find_elements_by_css_selector(Selectors.DETAILS_PROMPT.value)

    @property
    def details_answers(self):
        return self.driver.find_elements_by_css_selector(Selectors.DETAILS_ANSWERS.value)

    @property
    def modal_close(self):
        return self.driver.find_element_by_css_selector(Selectors.MODAL_CLOSE.value)
