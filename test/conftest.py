#--conftest.py

import pytest
from selenium import webdriver

# --IMPORTANT--
driver=None #driver imported as globally

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", defult="chrome"
    )

#at first this conftest will initiliza then test_e2e will start
@pytest.fixture(scope="class")

#when declare fixture, it will have a request as an istance
def setup(request): #request is a instance for our fixture. that comes with defult
    global driver#initialize one driver object, this is a new variable created, it will not create new driver object
    #it will use global driver whatever defined here, it will create new variable if we not define global driver here
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome("D:\software programs\python\Lib\site-packages\selenium\chromedriver.exe")

    elif browser_name=="firefox":
        driver= webdriver.FireFox("D:\software programs\python\Lib\site-packages\selenium\geckodriver.exe")

    elif browser_name=="firefox":
        print("IE driver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    #return driver  # it will catch the test_e2e def function but we could not use this bcs of yield so
    #we will use instead

    #this is a sort of return command
    request.cls.driver=driver #cls is a class object, we ere assigning our local driver of this fixture to the class driver.
    #yerel driver class driver a atandı.
    #cls.driver test_e2e daki driver a aittir

    #until this will be executed then yield transfer to test_e2e then execution finish come back here end driver get closed
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """"

        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test failed
        :param item:
    """

    pytest_html=item.config.pluginmanager.getplugin('html')
    outcome=yield
    report=outcome.get_result()
    extra=getattr(report, 'extra', [])

    if report.when=='call' or report.whem=="setup":
        xfail=hasattr(report,'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name=report.nodeid.replace("::","_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html='<div><img src="%s" alt="screenshot" style="width:304px;height:228p"' \
                     'onclick="window.open(this.src)" align="right/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra=extra

    def _capture_screenshot(name):
        driver.get_screenshot_as_file(name) #this friver use global driver



