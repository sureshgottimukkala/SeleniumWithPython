import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linkText = "Logout"
    link_loginUserName_xpath = "//div[@id='navbarText']//li[@class='nav-item']/a[@class='nav-link disabled']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        ele = WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.ID, self.textbox_username_id)))
        ele.clear()
        ele.send_keys(username)
        # self.driver.find_element(By.ID, "Email").clear()
        # self.driver.find_element((By.ID, "Email")).send_keys(username)

    def setPassword(self, pwd):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        eleText = self.driver.find_element(By.XPATH, self.link_loginUserName_xpath).text
        return eleText
