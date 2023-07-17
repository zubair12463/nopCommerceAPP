import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import logging
from utilities import xlutils

class Test_001_Lognin:
    base_URL = ReadConfig.get_baseUrl()
    Path = './/TestData/data.xlsx'
    logger = LogGen.loggen()

    def test_login(self,setup):
        self.driver = setup
        self.logger.info("**************** VERIFYING test_login_DDT ****************")
        self.driver.get(self.base_URL)
        self.lp = Login(driver=self.driver)
        list = []
        row_count = xlutils.GetRowCount(self.Path,'Sheet1')
        for r in range(2,row_count+1):
             self.username = xlutils.readData(self.Path,'Sheet1',r,1)
             self.Passward = xlutils.readData(self.Path,'Sheet1',r,2)
             self.exp = xlutils.readData(self.Path,'Sheet1',r,3)
             self.lp.setUsername(self.username)
             self.lp.setPassward(self.Passward)
             self.lp.clickLogin()
             title = self.driver.title
             exp_title = 'Dashboard / nopCommerce administration'
             if title == exp_title:
                 if self.exp == 'Pass':
                     self.logger.info('***** Passed *****')
                     self.lp.doLogOut()
                     list.append('Pass')
                 elif self.exp == 'Fail':
                     self.logger.error('***** Failed *****')
                     self.lp.doLogOut()
                     list.append('Fail')   
             elif title != exp_title:
                 if self.exp == 'Fail':
                     self.logger.error('***** Passed *****')
                     list.append('Pass')
                 elif self.exp == 'Pass':
                     self.logger.error('***** Failed *****')  
                     list.append('Fail')           
        if 'Fail' not in list:
             self.logger.error('***** Test_Login_DDT Passed *****') 
             self.driver.close()
             assert True    
        else:
             self.logger.error('***** Test_Login_DDT Failed *****')  
             self.driver.close()
             assert False   