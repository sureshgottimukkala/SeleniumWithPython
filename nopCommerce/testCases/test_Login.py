from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from pageObjects.LoginPage import Login
import os
from utilities.BaseClass import BaseClass
from utilities.ReadProperties import ReadProperties

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


class Test_001_Login(BaseClass):

    @pytest.mark.usefixtures("setup")
    def test_homePageTitle(self):
        log = self.getLogger()
        # log.info("\n ************** test_homePageTitle *************** ")
        log.info("1. Loading the App URL ")
        RootDir = self.setRootDir()
        # self.driver.get(self.baseURL)
        self.driver.get(ReadProperties.getAppURL())
        log.info("2. Verifying the homepage title ")
        act_title = self.driver.title
        if act_title == "Your store. Login1":
            log.info("PASSED: Verifying Homepage Title is Successful")
            assert True
        else:
            # now = datetime.now().strftime("%y-%m-%d-%H%M%S")
            # self.driver.get_screenshot_as_file(RootDir[0] + r'\Screenshots\screenshot-%s.png' % now)
            log.error("Error: Failed verifying the title of the webpage")
            assert False

    @pytest.mark.usefixtures("setup")
    def ggtest_Login(self):
        RootDir = self.setRootDir()
        log = self.getLogger()
        # log.info("\n ************* test_Login ***************** ")
        log.info("1. Loading the App URL ")
        self.driver.get(ReadProperties.getAppURL())
        self.lp = Login(self.driver)
        # self.lp.setUserName(self.userName)
        # self.lp.setPassword(self.password)
        log.info("2. Enter Username ")
        self.lp.setUserName(ReadProperties.getUserName())
        log.info("3. Enter Password ")
        self.lp.setPassword(ReadProperties.getPassword())
        log.info("4. Click Login ")
        self.eleText = self.lp.clickLogin()
        act_title = self.driver.title
        log.info("5. Verify if Login is successful ")
        # Validation
        if self.eleText == "John Smith":
            assert True
            self.driver.get_screenshot_as_file(RootDir + r"\Screenshots\test_LoginPassed-%s.png" % now)
            log.info("PASSED: Login Successful")
        else:
            # self.driver.get_screenshot_as_file(RootDir + r"\Screenshots\test_LoginAssertionFailed.png" % now)
            log.error("Error: Failed verifying the successful logging into the App")
            assert False
