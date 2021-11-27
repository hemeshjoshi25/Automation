from unittest import TestCase
import requests
from pageobjects.login import LoginPage
from utils.drivers import driver
from utils.redux_devtools import delete_redux_devtools
from utils.parse_args import parse_args
from settings import LOGIN_EMAIL, LOGIN_PASSWORD, STAGING, CBT_USER, CBT_AUTH


class IscE2eTestCase(TestCase):
    """
    A wrapper of TestCase which will launch a selenium server, login, and add cookies in the setUp
    phase of each test.
    """

    @classmethod
    def setUpClass(cls, *args, **kwargs):
        _, _, host, _, _ = parse_args()
        cbt_test_name = getattr(cls, 'CBT_SHORT_DESC', cls.__name__)
        cls.api_session = requests.Session()
        cls.api_session.auth = (CBT_USER, CBT_AUTH)
        cls.test_result = 'fail'
        cls.driver = driver(cbt_test_name)
        cls.driver.get(host)
        # Redux Devtools doesn't exist in STG. Skip to save time
        if host != STAGING:
            # Remove Redux Devtools
            delete_redux_devtools(cls.driver)
        # Login
        cls.login = LoginPage(cls.driver)
        cls.login.log_in(LOGIN_EMAIL, LOGIN_PASSWORD)

    @classmethod
    def tearDownClass(cls):
        if cls.test_result is not None:
            cls.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + cls.driver.session_id,
                                data={'action': 'set_score', 'score': cls.test_result})
        cls.driver.quit()
