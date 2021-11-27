from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def delete_redux_devtools(driver):
    try:
        element = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div')
    except NoSuchElementException:
        # redux extension doesn't exist (staging, qa, and production environments)
        pass
    else:
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)


def minimize_redux_devtools(driver):
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys('h') \
        .key_up(Keys.CONTROL) \
        .perform()
