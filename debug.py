from selenium import webdriver
from .pageobjects.report import GenericReportPage
from .pageobjects.login import LoginPage
from .pageobjects.history import HistoryPage
from .pageobjects.modules.people import PeoplePage
from .pageobjects.modules.shopper import ShopperPage
from .pageobjects.reports.count_report import CountReportPage
from .utils.redux_devtools import minimize_redux_devtools
from .settings import HOST, IMPLICIT_TIMEOUT, LOGIN_EMAIL, LOGIN_PASSWORD


if __name__ != '__main__':
    raise Exception('debug.py should never be imported, it is meant to be a standalone script')

# Initialize selenium driver
driver = webdriver.Chrome()
driver.implicitly_wait(IMPLICIT_TIMEOUT)
driver.set_window_size(1680, 1050)
driver.maximize_window()
driver.get(HOST)


# Define immediately after driver, so if something fails, this function is available
def close():
    """Convenience utility to close selenium session and quit terminal at once"""
    driver.close()
    quit()


# Minimize redux dev tools extention
minimize_redux_devtools(driver)

# Initialize Page Objects
login_page = LoginPage(driver)
history = HistoryPage(driver)
people_insights_page = PeoplePage(driver)
shopper_page = ShopperPage(driver)
count_report = CountReportPage(driver)
report = GenericReportPage(driver)


# NOTE: comment this out if you don't want to log in automatically
login_page.log_in(LOGIN_EMAIL, LOGIN_PASSWORD)

# Custom code to shorten feedback loop can be added here

# EXAMPLE
# my_reports_page.nav_link.click()
# my_reports_page.open_most_recent('Shopper Profile')
# report.get_tab('Favorite Stores')

# history.nav_link.click()
# history.open_most_recent('Count Report')
# sleep(3)

# tables = report.tables()
# table = tables[0]
# rows = report.get_rows(table)
# header = report.get_header_row(table)
# header_cells = report.headers(header)
