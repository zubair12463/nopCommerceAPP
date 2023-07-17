import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import logging

class Test_001_Lognin:
    base_URL = ReadConfig.get_baseUrl()
    username = ReadConfig.get_username()
    passward = ReadConfig.get_passward()
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("**************** Test_001_Login ****************")
        self.logger.info("**************** VERIFYING test_homePage title ****************")
        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == 'Your store. Login':
            self.logger.info("**************** home_page_title PASSESD ****************")
            assert True  
        else:
            self.driver.save_screenshot(".\\Screenshots"+"\\test_homePage_title.png")
            self.logger.error("**************** home_page_title FAILED ****************")
            assert False
            

    def test_login(self,setup):
        self.driver = setup
        self.logger.info("**************** VERIFYING test_login ****************")
        self.driver.get(self.base_URL)
        self.lp = Login(driver=self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassward(self.passward)
        self.lp.clickLogin()
        title = self.driver.title
        if title == 'Dashboard / nopCommerce administratiosn':
            self.logger.info("**************** test_login PASSED ****************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots"+"\\test_login.png")
            self.driver.close()
            self.logger.error("**************** test_login FAILED ****************")
            assert False
            
