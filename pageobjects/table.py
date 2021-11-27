from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from utils.decorators import retry_on_stale_element
from utils.parse_args import parse_args
from constants.enums import Selectors, Attributes, Sort
from utils.IscE2eTestCase import IscE2eTestCase


class GenericReportTable(IscE2eTestCase):

    def __init__(self, driver):
        self.driver = driver
        _, self.target, _, _, _ = parse_args()

    # Returns all table elements on a page
    def tables(self):
        return self.driver.find_elements_by_css_selector(Selectors.TABLE.value)

    # Returns all header elements from a given table
        # table_idx = table idx to get headers from
    def headers(self, table_idx=0):
        table = self.tables()[table_idx]
        return table.find_elements_by_css_selector(Selectors.HEADER_CELL.value)

    # Compares two values and raises exception if they are not equal
        # one = value 1
        # two = value 2
    def assertEqual(self, one, two):
        if one != two:
            raise Exception("<{}> does not equal <{}> as expected".format(one, two))

    # Validates that a table's header row values are as expected
        # headers = list of expected header row cell values
        # head = header cell that dynamically changes
        # idx = index of head column, default is 0
        # table_idx = index of table on page
        # form = format text if header cell needs to be formatted
    def headers_validate(self, headers, head=None, idx=0, table_idx=0, form=None):
        for h, hdr in enumerate(self.headers(table_idx)):
            if head is not None and h == idx:
                self.assertEqual(hdr.text, head)
            elif headers[h] is None:
                continue
            else:
                self.assertEqual(hdr.text, headers[h].format(form))

    # Returns a list of cell elements in a specific column (not including header cells)
        # col_idx = index of column to pull cells from (idx starts at 1, not 0)
    def get_column(self, col_idx):
        return self.driver.find_elements_by_css_selector(Selectors.ROW_COL_IDX.value.format(col_idx))

    @staticmethod
    def get_table_cells(table):
        return table.find_elements_by_css_selector(Selectors.CELL_TEXT.value)

    # Validates that a table's column values are as expected
        # col_idx = index of column to validate (idx starts at 1, not 0)
        # col_names = list of expected column cell values
    def table_validate(self, col_idx, col_names):
        for c, col in enumerate(self.get_column(col_idx)):
            if col.text != col_names[c]:
                raise Exception('<{}> table cell does not equal <{}> as expected'.format(col.text, col_names[c]))

    # Validates that a table's column values are as expected (ORDER NOT IMPORTANT)
        # col_idx = index of column to validate (idx starts at 1, not 0)
        # col_names = list of expected column cell values
    def table_unordered_validate(self, col_idx, col_names):
        for c, col in enumerate(self.get_column(col_idx)):
            if col.text not in col_names:
                raise Exception('<{}> is not an expected table row'.format(col.text))

    # Returns the sort order of a given header cell
        # cell = header cell to pull the sort order from
    def get_cell_sort(self, cell):
        return cell.find_element_by_class_name(Selectors.CELL_SORT.value).get_attribute(Attributes.CLASS.value)

    # Sorts a column in the sort order given
        # col_idx = index of column to sort
        # sort = desired sort order (Ex: Sort.ASC.value)
        # table_idx = index of table on page, default is 0
    def click_sort(self, col_idx, sort, table_idx=0):
        cell = self.headers(table_idx)[col_idx]
        while sort not in self.get_cell_sort(cell):
            try:
                cell.click()
                continue
            except WebDriverException:
                self.scroll_down()
        if sort not in self.get_cell_sort(cell):
            raise Exception('Sort direction is not <{}> as expected'.format(sort))

    # Returns all the row elements from a given table
        # table = table element to pull rows from
    @staticmethod
    def get_rows(table):
        return table.find_elements_by_css_selector(Selectors.ROW.value)

    # Returns all the cell elements from a row or table
        # row_table = a given row or table to pull cells from
    @staticmethod
    @retry_on_stale_element
    def get_cells(row_table):
        return row_table.find_elements_by_class_name(Selectors.CELL.value)

    # Returns a uniform list that is all strings unless the given list is all floats
        # list = list to check
    def uniform_list(self, list):
        if all(isinstance(l, str) for l in list):
            return list
        elif all(isinstance(l, float) for l in list):
            return list
        else:
            for l, li in enumerate(list):
                if type(li) != str:
                    list[l] = str(int(li))
            return list

    # Tests that a column is sorted in the expected order
        # col_idx = index of column to test sort order
        # sort = expected sort order (Ex: Sort.ASC.value)
        # table_idx = index of table on page, default is 0
    def is_sorted(self, col_idx, sort, table_idx=0):
        rows = self.get_rows(self.tables()[table_idx])
        if len(rows) == 1:
            return
        cells = []
        for r in rows:
            text = self.get_cells(r)[col_idx].text
            text = text.translate(str.maketrans('', '', '%$,'))
            if text is not None and text != '-':
                try:
                    cells.append(float(text))
                except ValueError:
                    cells.append(text.lower())
        cells = self.uniform_list(cells)
        if sort == Sort.DESC.value:
            if cells != sorted(cells, reverse=True):
                raise Exception('Column is not sorted DESC as expected')
        else:
            if cells != sorted(cells):
                raise Exception('Column is not sorted ASC as expected')

    # Sorts a column of a table all three ways and validates the column is sorted correctly
        # col_idx = index of column to sort
        # table_idx = index of table on page, default is 0
    @retry_on_stale_element
    def test_sort(self, col_idx, value='str', table_idx=0):
        if self.target == 'CBT':
            return
        try:
            cell = self.headers(table_idx)[col_idx]
        except IndexError:
            return
        if Sort.NATURAL.value not in self.get_cell_sort(cell):
            raise Exception('Default sort direction is not NATURAL as expected')
        self.click_sort(col_idx, Sort.ASC.value, table_idx)
        self.is_sorted(col_idx, Sort.ASC.value, table_idx)
        self.click_sort(col_idx, Sort.DESC.value, table_idx)
        self.is_sorted(col_idx, Sort.DESC.value, table_idx)
        self.click_sort(col_idx, Sort.NATURAL.value, table_idx)

    # Scrolls down by pressing 'DOWN' arrow key
    def scroll_down(self):
        self.driver.find_element_by_css_selector(Selectors.BODY.value).send_keys(Keys.DOWN)
        sleep(0.5)  # Wait for scroll

    # Scrolls to top of page by pressing 'HOME' key
    def scroll_top(self):
        self.driver.find_element_by_css_selector(Selectors.BODY.value).send_keys(Keys.HOME)
        sleep(0.5)  # Wait for scroll
