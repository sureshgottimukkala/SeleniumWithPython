from datetime import datetime
from logging import getLogger

import pytest
from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path
import os
import utilities.ExcelUtils

from pageObjects.LoginPage import Login
from testCases.conftest import driver
from utilities.BaseClass import BaseClass
from utilities.ReadProperties import ReadProperties

featureFileDir = "BDD\\Features"
featureFileName = "Login.feature"
print(Path(__file__))
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
FeatureFile = BASE_DIR.joinpath(featureFileDir).joinpath(featureFileName)
print(FeatureFile)
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log = BaseClass.getLogger()
filePath = r"D:\AutomationTesting\PyCharmWS\nopCommerce\TestData\TestData.xlsx"
RootDir = BaseClass.setRootDir()


@scenario(FeatureFile, "Logging into nopCommerce App" )
def test_publish(setup):
    print("Test has got completed")
    pass


# @given("a login page", target_fixture="login_page")
# def login_page(setup):
#     return Login(setup)


@given("User is valid")
def step_imp(setup):
    # log.info("\n ************* test_Login ***************** ")
    log.info("1. Loading the App URL ")
    setup.get(ReadProperties.getAppURL())
    lp = Login(setup)
    # lp.setUserName(userName)
    # lp.setPassword(password)

    RowCount = utilities.ExcelUtils.getRowCount(filePath, "Sheet1")
    lst_status = []
    print("RowCount:", RowCount)
    log.info(BaseClass.random_generator())
    for i in range(2, RowCount + 1):
        userName = utilities.ExcelUtils.readExcelData(filePath, "Sheet1", i, 1)
        passWord = utilities.ExcelUtils.readExcelData(filePath, "Sheet1", i, 2)

        log.info("2. Enter Username ")
        lp.setUserName(userName)
        log.info("3. Enter Password ")
        lp.setPassword(passWord)
        log.info("4. Click Login ")
        lp.clickLogin()
        act_title = setup.title
        exp_title = "Dashboard / nopCommerce administration"
        log.info("5. Verify if Login is successful ")
        expStatus = utilities.ExcelUtils.readExcelData(filePath, "Sheet1", i, 3)
        # Validation

        if act_title == exp_title:
            if expStatus == "Pass":
                setup.get_screenshot_as_file(RootDir + r"\Screenshots\test_LoginPassed-%s.png" % now)
                lp.clickLogout()
                lst_status.append("Pass")
                log.info("PASSED: Login Successful")
            elif expStatus == "Fail":
                log.error("Error: Failed verifying the successful logging into the App")
                log.info(f"Credentials used are : UserName : {userName} and Password : {passWord}")
                lp.clickLogout()
                lst_status.append("Fail")
        elif act_title != exp_title:
            if expStatus == "Pass":
                log.error("Error: Failed verifying the negative scenario")
                log.info(f"Credentials used are : UserName : {userName} and Password : {passWord}")
                lst_status.append("Fail")
            if expStatus == "Fail":
                log.info("Passed: verifying the negative scenario")
                lst_status.append("Pass")

    if "Fail" not in lst_status:
        log.info("********* Test Case Passed **********")
        assert True
    else:
        log.error("********* Test Case failed *********")
        assert False
