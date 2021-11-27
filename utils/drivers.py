import requests
from selenium import webdriver
from utils.parse_args import parse_args
from settings import IMPLICIT_TIMEOUT, CBT_USER, CBT_AUTH

# For a full list of crossbrowsertesting (CBT) capabilities:
# https://help.crossbrowsertesting.com/selenium-testing/tutorials/crossbrowsertesting-automation-capabilities/


def chrome_config(cbt_test_name):
    return {
        'name': cbt_test_name,
        'browserName': 'Chrome',
        'version': 'Latest',
        'platform': 'Windows 10',
        'screenResolution': '1920x1080',
        'record_video': True,
    }


def safari_config(cbt_test_name):
    return {
        'name': cbt_test_name,
        'browserName': 'Safari',
        'version': 'Latest',
        'platform': 'Mac OSX 10.15',
        'screenResolution': '1920x1080',
        'record_video': True,
    }


def firefox_config(cbt_test_name):
    return {
        'name': cbt_test_name,
        'browserName': 'Firefox',
        'version': 'Latest',
        'platform': 'Mac OSX 10.15',
        'screenResolution': '1920x1080',
        'record_video': True,
    }


def internet_explorer_config(cbt_test_name):
    return {
        'name': cbt_test_name,
        'browserName': 'Internet Explorer',
        'version': '11',
        'platform': 'Windows 10',
        'screenResolution': '1920x1080',
        'record_video': True,
    }


def browser_configs(cbt_test_name):
    return {
        'CHROME': chrome_config(cbt_test_name),
        'SAFARI': safari_config(cbt_test_name),
        'FF': firefox_config(cbt_test_name),
        'IE': internet_explorer_config(cbt_test_name)
    }


def multi_browser_configs(cbt_test_name):
    return [
        chrome_config(cbt_test_name),
        safari_config(cbt_test_name),
        firefox_config(cbt_test_name),
        internet_explorer_config(cbt_test_name)
    ]


def driver(cbt_test_name):
    browser, target, _, _, _ = parse_args()
    config = browser_configs(cbt_test_name)[browser]
    # TODO: Implement FF geckodriver to man running against FF locally an option
    driver = chrome_driver() if target == 'LOCAL' else remote_cbt_driver(config)
    driver.implicitly_wait(IMPLICIT_TIMEOUT)
    driver.set_window_position(0, 0)
    driver.set_window_size(1650, 1600)
    return driver


def chrome_driver():
    return webdriver.Chrome()


def remote_cbt_driver(config):
    """Starts a remote selenium driver via cbt given a config"""
    api_session = requests.Session()
    api_session.auth = (CBT_USER, CBT_AUTH)
    # Start the remote browser on our server
    return webdriver.Remote(
        desired_capabilities=config,
        command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (CBT_USER, CBT_AUTH)
    )
