import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec

import utilities.ExcelUtils
from pageObjects.LoginPage import Login
import os
from utilities.BaseClass import BaseClass
from utilities.ReadProperties import ReadProperties

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


class Test_001_Login:
    log = BaseClass.getLogger()
    filePath = r"D:\AutomationTesting\PyCharmWS\nopCommerce\TestData\TestData.xlsx"
    RootDir = BaseClass.setRootDir()

    @pytest.mark.usefixtures("setup")
    def test_Login(self):

        # log.info("\n ************* test_Login ***************** ")
        self.log.info("1. Loading the App URL ")
        self.driver.get(ReadProperties.getAppURL())
        self.lp = Login(self.driver)
        # self.lp.setUserName(self.userName)
        # self.lp.setPassword(self.password)

        RowCount = utilities.ExcelUtils.getRowCount(self.filePath, "Sheet1")
        lst_status = []
        print("RowCount:", RowCount)
        self.log.info(BaseClass.random_generator())
        for i in range(2, RowCount + 1):
            userName = utilities.ExcelUtils.readExcelData(self.filePath, "Sheet1", i, 1)
            passWord = utilities.ExcelUtils.readExcelData(self.filePath, "Sheet1", i, 2)

            self.log.info("2. Enter Username ")
            self.lp.setUserName(userName)
            self.log.info("3. Enter Password ")
            self.lp.setPassword(passWord)
            self.log.info("4. Click Login ")
            self.lp.clickLogin()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            self.log.info("5. Verify if Login is successful ")
            expStatus = utilities.ExcelUtils.readExcelData(self.filePath, "Sheet1", i, 3)
            # Validation

            if act_title == exp_title:
                if expStatus == "Pass":
                    self.driver.get_screenshot_as_file(self.RootDir + r"\Screenshots\test_LoginPassed-%s.png" % now)
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                    self.log.info("PASSED: Login Successful")
                elif expStatus == "Fail":
                    self.log.error("Error: Failed verifying the successful logging into the App")
                    self.log.info(f"Credentials used are : UserName : {userName} and Password : {passWord}")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if expStatus == "Pass":
                    self.log.error("Error: Failed verifying the negative scenario")
                    self.log.info(f"Credentials used are : UserName : {userName} and Password : {passWord}")
                    lst_status.append("Fail")
                if expStatus == "Fail":
                    self.log.info("Passed: verifying the negative scenario")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.log.info("********* Test Case Passed **********")
            assert True
        else:
            self.log.error("********* Test Case failed *********")
            assert False
