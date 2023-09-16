# -- test_HomePage
import pytest

from TestData.HomePageData import HomePageData  # package name/ file name/ class name respectively
from pageObjects.HomePage import HomePage
from test.e2eTest import driver
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    # this block ll execute at once so we need to write refresh code line in order to wrapp next data.
    def test_fromSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self, driver)
        log.info("first name is " + getData["firstname"])
        homepage.getName().send_keys(getData[
                                         "firstname"])  # rather then write getData[0] we write getData["firstname"] to understand the which index it is.
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(),
                                getData["gender"])  # first argument is locator, second argument is text

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    # dictionary data type will help to run test case as different data sets
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param

#Data will drive from excel not any other files
