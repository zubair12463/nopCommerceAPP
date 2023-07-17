from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class SearchCustomer:

    txtEmail_id = "SearchEmail"
    txtFirstName_xpath = "//input[@id='SearchFirstName']"
    txtLastName_xpath = "//input[@id='SearchLastName']"
    btnSearch_xpath = "//button[@id='search-customers']"
    tableEmailRowsForEmail_xpath = "//tbody/tr/td[2]"
    tableEmailRowsForName_xpath = "//tbody/tr/td[3]"

    def __init__(self,driver:WebDriver):
       self.driver = driver

    def setEmail(self,email):
        self.email = email
        email_box = self.driver.find_element(By.ID, self.txtEmail_id)
        email_box.clear()
        email_box.send_keys(email)

    def clickSearchButton(self):
        sleep(3)
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def setFirstName(self,firstName):
        self.FirstName = firstName
        Name = self.driver.find_element(By.XPATH, self.txtFirstName_xpath)  
        Name.clear()
        Name.send_keys(firstName)

    def setLastName(self,lastName):
        self.lastName = lastName
        Name = self.driver.find_element(By.XPATH, self.txtLastName_xpath)
        Name.clear()
        Name.send_keys(lastName)      

    def verifyCustomerByEmail(self):
        flag = False
        Customers = self.driver.find_elements(By.XPATH, self.tableEmailRows_xpath)
        for customer in Customers:
            if self.email == customer.text.strip():
                flag = True
                break
        return flag
    
    def verifyCustomerByName(self):
        flag = False
        Customers = self.driver.find_elements(By.XPATH, self.tableEmailRowsForName_xpath)
        for customer in Customers:
            print('Name = ', customer.text)
            if self.FirstName + ' ' + self.lastName == customer.text:
                 flag = True
                 break
        return flag    
