import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import logging
from pageObjects.AddCustomerPage import AddCustomer
import time
from selenium.webdriver.common.by import By
from pageObjects.SearchCustomerPage import SearchCustomer

class Test_004_SearchCustomer:
    base_URL = ReadConfig.get_baseUrl()
    username = ReadConfig.get_username()
    passward = ReadConfig.get_passward()
    logger = LogGen.loggen()

    def test_SearchCustomer(self,setup):
        self.logger.info("**************** Test_004_SearchCustomer By Email ****************")
        self.logger.info("**************** Start Login ****************")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = Login(driver=self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassward(self.passward)
        self.lp.clickLogin()
        self.logger.info("**************** Log in Succesful ****************")

        time.sleep(5)
        self.AddCustm = AddCustomer(driver=self.driver)
        self.AddCustm.clickCustomerMenue()
        self.AddCustm.clickCustomerMenuItem()
        time.sleep(3)

        self.SearchCustomer = SearchCustomer(driver=self.driver)
        self.SearchCustomer.setEmail('reetam3@gmail.com')
        self.SearchCustomer.clickSearchButton()
        time.sleep(10)
        self.flag = self.SearchCustomer.verifyCustomerByEmail()
        if self.flag == True:
         self.logger.info("**************** Search Customer By Email Test Passed ****************")
         self.driver.close()
         assert True
        else:
         self.driver.save_screenshot(".\\Screenshots"+"\\test_AddCustomer.png")
         self.logger.info("**************** Search Customer By Email Test Failed ****************") 
         self.driver.close()
         assert False  
        