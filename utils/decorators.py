from time import sleep
from functools import wraps
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from settings import IMPLICIT_TIMEOUT


def retry_on_exception_factory(exc):
    def retry_on_exc(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except exc:
                sleep(5)
                return f(*args, **kwargs)

        return wrapped_f

    return retry_on_exc


retry_on_no_element = retry_on_exception_factory(NoSuchElementException)

retry_on_stale_element = retry_on_exception_factory(StaleElementReferenceException)


def update_implicit_timeout(time):
    def timeout(func):
        def wrap_func(self, *args, **kwargs):
            self.driver.implicitly_wait(time)
            try:
                f = func(self, *args, **kwargs)
            finally:
                self.driver.implicitly_wait(IMPLICIT_TIMEOUT)
                if not f:
                    raise Exception('No results found, please check manually')
            return f
        return wrap_func
    return timeout
