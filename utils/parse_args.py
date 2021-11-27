import argparse
from settings import LOCALHOST, STAGING, UK_STAGING


def bold(string):
    return '\033[1m' + string + '\033[0m'


def green(string):
    return '\033[92m' + string + '\033[0m'


def yellow(string):
    return '\033[93m' + string + '\033[0m'


parser = argparse.ArgumentParser(description='Insights Integration test')
parser.add_argument(
    '--browser',
    nargs=1,
    choices=['CHROME', 'SAFARI', 'FF', 'IE'],
    default=['CHROME'],
    help='Specifiy browser to use in integration test'
)
parser.add_argument(
    '--target',
    nargs=1,
    choices=['LOCAL', 'CBT'],
    default=['LOCAL'],
    help='Specify to run webdriver locally or on crossbrowsertesting'
)
parser.add_argument(
    '--host',
    nargs=1,
    choices=['STG', 'LOCAL'],
    default=['STG'],
    help='Specify host to run test against'
)
parser.add_argument(
    '--panel',
    nargs=1,
    choices=['US', 'UK'],
    default=['US'],
    help='Specify which panel to run test against'
)
parser.add_argument(
    '--test',
    nargs='+',
    default=['ALL'],
    help='Specify which test_class or test_classes to run (Separate tests by space)'
)

args = parser.parse_args()
browser = args.browser[0]
target = args.target[0]
host = args.host[0]
panel = args.panel[0]
test = args.test

unsupported_local_browsers = ['FF', 'IE']
if target == 'LOCAL' and browser in unsupported_local_browsers:
    raise Exception(bold(yellow('Please specify a browser that is supported locally')))

if host == 'LOCAL' and panel == 'UK':
    raise Exception(bold(yellow('UK Panel can only be run against STG, not LOCAL')))

host = LOCALHOST if host == 'LOCAL' else STAGING

if host == STAGING and panel == 'UK':
    host = UK_STAGING

if len(test) > 1:
    print(bold(green('Testing {} on {} against {} selenium server using {} and {} panel'.format(
        test, browser, target, host, panel))))
else:
    print(bold(green('Testing {} on {} against {} selenium server using {} and {} panel'.format(
        test[0], browser, target, host, panel))))


def parse_args():
    return browser, target, host, panel, test
