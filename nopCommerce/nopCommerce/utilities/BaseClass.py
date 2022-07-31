import random
import string
from datetime import datetime
import logging
import inspect
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass:

    @staticmethod
    def setRootDir():
        RootDir = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
        return RootDir

    @staticmethod
    def getLogger():

        # logging.basicConfig(filename='.\\Logs\\logfile.log', formatter='%(asctime)s :%(levelname)s : %(name)s :%(
        # message)s')
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)

        # <<<< Another way of logging >>>>>>>>>>>>

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('.\\Logs\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)

        # <<<< Another way of logging >>>>>>>>>>>>
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    @staticmethod
    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
