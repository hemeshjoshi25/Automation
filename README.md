# Insights End-to-End Tests

The QA directory represents our End-to-End testing suite (currently using Selenium).

## Installation

We use virtual environments to keep track of our dependencies:

```bash
# Navigate to the qa directory
$ cd /isc-insights/qa

# Create a fresh virtual environment
$ python3 -m venv .venv

# Activate the virtual environment
$ source .venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt
```

If you are testing locally, you will also need to install **chromedriver** via `brew cask install chromedriver`
or at http://chromedriver.chromium.org/downloads.

## Usage

Remember to activate your virtualenv (with all dependencies installed) _before_ running the tests.

```bash
# Navigate to the qa directory
$ cd /isc-insights/qa

# Run the test.py file with the help flag for more info
$ python3 test.py -h
# -OR-
$ python3 test.py --help

usage: test.py [-h] [--browser {CHROME,FF,IE}] [--target {CBT,LOCAL}]
               [--host {LOCAL,STG}] [--panel {US,UK}] [--test TEST [TEST ...]]

Insights Integration test

optional arguments:
  -h, --help            show this help message and exit
  --browser {CHROME,FF,IE}
                        Specifiy browser to use in integration test
  --target {CBT,LOCAL}  Specify to run webdriver locally or on
                        crossbrowsertesting
  --host {LOCAL,STG}    Specify host to run test against
  --panel {US,UK}       Specify which panel to run test against
  --test TEST [TEST ...]
                        Specify which test_class or test_classes to run
                        (Separate tests by space)

```

### Using command-line options

#### --browser

Use the `--browser` option to select a browser to run against.

Options:

- CHROME, FF, IE (Default is CHROME)

#### --target

Use the `--target` option to run webdriver locally or on remotely crossbrowsertesting

Options:

- LOCAL, CBT (Default is LOCAL)

Note:

- **If you want to run remotely, you MUST create a tunnel with CBT.** See the section below (_Creating a tunnel with CrossBrowserTesting_) on how to do this.

#### --host

Use the `--host` option to run against staging environment or locally

Options:

- STG, LOCAL (Default is STG)

#### --panel

Use the `--panel` option to run against US or UK Insights

Options:

- US, UK (Default is US)

#### --test

Use the `--test` option to run a specific test or set of tests

Options:

- Any <test_class> or <test_module> as listed in the test.py file (Default is 'ALL')
- To run multiple tests, separate by a single space

#### Example

To run the Login tests against Firefox via CBT, you might execute

```bash
python3 test.py --target CBT --browser IE --test Login
```

### Creating a tunnel with CrossBrowserTesting

There are two ways to do this:

- (Preferred) Start a tunnel with node

  - https://github.com/crossbrowsertesting/cbt-tunnel-nodejs

  ```bash
  npm install -g cbt_tunnels
  cbt_tunnels --username=<username> --authkey=<authkey>
  ```

- Use their Chrome extension and their web app

  - Download the chrome extension if you don't already have it for crossbrowsertesting: https://chrome.google.com/webstore/detail/crossbrowsertesting-local/ldabplgpogjknofonmccpbgeoolbcbfm
  - Log into https://app.crossbrowsertesting.com/ and turn **ON** "Local Connection" in the top nav bar

### Entering debug mode

This is useful for doing quick test and running in the shell against a session

```bash
python -i debug.py
```

and to close the session and exit the python shell

```bash
>>> close()
```

### Running Integration test on CBT against a local server

1. Find your network address.

```bash
$ ifconfig
# Use ifconfig in the terminal
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether 8c:85:90:2c:2d:9f
	inet6 fe80::e5:690d:efc2:d8c9%en0 prefixlen 64 secured scopeid 0x6
	inet 10.254.0.169 netmask 0xffffff00 broadcast 10.254.0.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
```

Here, the address is `10.254.0.169`

2. Update the following files

```diff
### /client/src/js/util/api.jsx
-const DEV_URL = 'http://127.0.0.1:8000/';
+const DEV_URL = 'http://10.254.0.169:8000/';

### /qa/settings.py
-HOST = 'http://localhost:7002'
+HOST = 'http://10.254.0.169:7002'

### /server/isc_insights/insights/settings/__init__.py
+ALLOWED_HOSTS = {
+    '10.254.0.169',
+    '127.0.0.1',
+    'localhost',
+    '.infoscoutinc.net',
+    '.infoscout.co',
+    '.numerator.com',
+}
```

3. Run the test. Ex. for Internet Explorer -> `python test.py IE`

## Contributing

### Adding in new test classes

1. Open up `isc-insights/qa/test.py`
2. Import the test class to be added to test
3. Add to `test_classes` list

Group the test classes together

```
# Basic Tests
login = [InsightsLogin]
navigation = [OtherNav, PeopleNav, ShopperNav, BrandNav, NewItemNav,
              PromoNav, SurveysNav, ToolsNav, LabsNav]
details = [ReadOnly, ReportDetails]
```

Combine the test classes

```
# Combine Basic Tests
basic_tests = (login + navigation + details)
```

Add Test Groups to `test_classes`

```
# Combine All Test Classes
test_classes = (basic_tests + groups + run_reports
                + run_rv_reports + run_cg_reports + completed_reports
                + completed_rv_reports + completed_cg_reports)
```

If you want the ability to run tests as a module, add the group to `test_modules`, and add the name of the test to `module_text`

```
# Module Test Text
module_text = ['Login', 'Navigation', 'ShareDetails', 'BasicTests', ...
...
# Module Test Classes
test_modules = [login, navigation, share_details, basic_tests, ...
```
