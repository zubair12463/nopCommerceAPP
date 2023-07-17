from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class AddCustomer:
      
      lnkCustomers_menu_xpath = "//i[@class='nav-icon far fa-user']"
      lnkCustomers_menuItem_xpath = "(//p[contains(text(),'Customers')])[2]"
      btnAddnew_xpath = "//a[normalize-space()='Add new']"
      txtEmail_id = 'Email'
      txtPassward_id = "Password"
      txtFirstName_id = "FirstName"
      txtLastName_id = "LastName"
      rdMaleGender_id = "Gender_Male"
      rdFemaleGender_id = "Gender_Female"
      txtDateOfBirth_id = "DateOfBirth"
      txtCompany_id = "Company"
      rdIsTaxExempt_id = "IsTaxExempt"
      txtNewsLetter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
      selectNewsLetter_StoreName_xpath = "//li[normalize-space()='Your store name']"
      selectNewsLetter_Store2_xpath = "//li[normalize-space()='Test store 2']"
      txtCustomerRole_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
      selectCustomerRole_Adminstrator_xpath = "//li[normalize-space()='Administrators']"
      selectCustomerRole_Moderators_xpath = "//li[normalize-space()='Forum Moderators']"
      selectVender_id = "VendorId"
      rdActie_id = "Active"
      txtAdminComment_id = "AdminComment"
      btnSave_xpath = "//button[@name='save']"
    
      def __init__(self,driver:WebDriver):
        self.driver = driver

      def clickCustomerMenue(self):
          self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

      def clickCustomerMenuItem(self):
          self.driver.find_element(By.XPATH, self.lnkCustomers_menuItem_xpath).click()

      def clickAddNewCustomer(self):
          self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

      def setEmail(self,email):
          self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

      def setPassward(self,passward):
          self.driver.find_element(By.ID, self.txtPassward_id).send_keys(passward)

      def setFirstName(self,name):
          self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(name)

      def setLastName(self,name):
          self.driver.find_element(By.ID, self.txtLastName_id).send_keys(name)

      def selectGender(self,gender):
          if gender == 'Male':
              self.driver.find_element(By.ID, self.rdMaleGender_id).click()
          elif gender == 'Female':
              self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
          else:
              self.driver.find_element(By.ID, self.rdMaleGender_id).click()

      def setDateOfBirth(self,dob):
          self.driver.find_element(By.ID,self.txtDateOfBirth_id).send_keys(dob)

      def setComoanyID(self,id):
          self.driver.find_element(By.ID, self.txtCompany_id).send_keys(id)

      def clickIsTexEmpty(self):
          self.driver.find_element(By.ID, self.rdIsTaxExempt_id).click()

      def setNewsLetterID(self,id):
          News = self.driver.find_element(By.XPATH, self.txtNewsLetter_xpath)
          News.click()
          if id == 'Your store name':
              News_letter = self.driver.find_element(By.XPATH,self.selectNewsLetter_StoreName_xpath)
          elif id == 'Test store 2':
              News_letter = self.driver.find_element(By.XPATH, self.selectNewsLetter_Store2_xpath)
          else:
              News_letter = self.driver.find_element(By.XPATH,self.selectNewsLetter_StoreName_xpath)
          sleep(2)    
          self.driver.execute_script('arguments[0].click();',News_letter)      

      def selectCustomerRole(self,role):
          self.driver.find_element(By.XPATH, self.txtCustomerRole_xpath).click()
          if role == 'Administrators':
              C_role = self.driver.find_element(By.XPATH, self.selectCustomerRole_Adminstrator_xpath)
          elif role == 'Forum Moderators':
              C_role = self.driver.find_element(By.XPATH, self.selectCustomerRole_Moderators_xpath)
          else:
              pass
          sleep(3)
          C_role.click()       

      def selectVender(self,vender):
          Select_Vender = self.driver.find_element(By.ID, self.selectVender_id)  
          Select_Vender.click()
          Select_V = Select(Select_Vender)
          if vender == 'Not a vendor':
            Select_V.select_by_visible_text('Not a vendor')
          elif vender == 'Vendor 1':
              Select_V.select_by_visible_text('Vendor 1')
          elif vender == 'Vendor 2':
              Select_V.select_by_visible_text('Vendor 2')     
          else:
              Select_V.select_by_visible_text('Not a vendor')

      def clickActive(self):
          self.driver.find_element(By.ID, self.rdActie_id).click()                                                      

      def setAdminComment(self,comment):
          self.driver.find_element(By.ID, self.txtAdminComment_id).send_keys(comment)

      def clickSave(self):
          self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
                  