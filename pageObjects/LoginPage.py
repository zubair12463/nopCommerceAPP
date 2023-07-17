from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Login:
    textbox_username_id = "Email"
    textbox_passward_id = "Password"
    button_login_xpath = "//button[@class = 'button-1 login-button']"
    button_logout_link_text = 'Logout'

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def setUsername(self,username):
        username_element = self.driver.find_element(By.ID, self.textbox_username_id)
        username_element.clear()
        username_element.send_keys(username)
    
    def setPassward(self,passward):
        passward_element = self.driver.find_element(By.ID, self.textbox_passward_id)
        passward_element.clear()
        passward_element.send_keys(passward)    

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def doLogOut(self):
        self.driver.find_element(By.LINK_TEXT, self.button_logout_link_text).click()
                