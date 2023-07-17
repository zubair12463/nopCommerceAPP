import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import logging
from pageObjects.AddCustomerPage import AddCustomer
import time
from selenium.webdriver.common.by import By
class Test_003_Lognin:
    base_URL = ReadConfig.get_baseUrl()
    username = ReadConfig.get_username()
    passward = ReadConfig.get_passward()
    logger = LogGen.loggen()

    def test_AddCustomer(self,setup):
        self.logger.info("**************** Test_003_AddCustomer ****************")
        self.logger.info("**************** Start Log IN ****************")
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
        self.AddCustm.clickAddNewCustomer()
        time.sleep(5)
        self.AddCustm.setEmail(email='zusgair67@gmail.com')
        self.AddCustm.setPassward('@45Zubair')
        self.AddCustm.setFirstName('Zubair')
        self.AddCustm.setLastName('Shahzad')
        self.AddCustm.selectGender('Male')
        self.AddCustm.setDateOfBirth('7/13/2001')
        self.AddCustm.setComoanyID('Habit ltd')
        self.AddCustm.clickIsTexEmpty()
        self.AddCustm.setNewsLetterID('Your store name')
        self.AddCustm.selectCustomerRole('Administrators')
        self.AddCustm.selectVender('Vender 1')
        self.AddCustm.clickActive()
        self.AddCustm.setAdminComment('My name is Zubair')
        self.AddCustm.clickSave()

        expted = self.driver.find_element(By.TAG_NAME, "body").text
        if 'The new customer has been added successfully.' in expted:
            self.logger.info("**************** Add Cutomer Test Passed ****************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots"+"\\test_AddCustomer.png")
            self.logger.info("**************** Add Cutomer Test Failed ****************")
            self.driver.close()
            assert False
