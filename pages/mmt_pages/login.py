from selenium.webdriver.common.by import By
from genericlib.WebdriverUtils import webUtils

class mmtLogin:
    _username='//input[@id="identifierId"]'
    _password='//input[@name="password"]'
    _nextbtn='//span[text()="Next"]'
    _nextbtn2='//span[text()="Next"]'
    _createAccount=" //p[contains(text(),'Login or Create Account')]"
    _googleBtn='//div[@data-cy="googleLogin"]'

    def __init__(self,driver):
        self.driver=driver
        obj=webUtils(driver)
        obj.implicitTime(10)

    def createAccount(self):
        print('in create account')
        return self.driver.find_element(By.XPATH,self._createAccount)

    def nextBtn_user(self):
        print('in nextbtn user')
        return self.driver.find_element(By.XPATH,self._nextbtn)

    def nextBtn_pwd(self):
        print('in nextbtn pwd')
        return self.driver.find_element(By.XPATH,self._nextbtn2)

    def googleBtn(self):
        print('in googlbtn')
        return self.driver.find_element(By.XPATH,self._googleBtn)

    def getUsername(self):
        print('get username')
        return self.driver.find_element(By.XPATH,self._username)

    def getPasssword(self):
        print('get password')
        return self.driver.find_element(By.XPATH, self._password)

    def windowHandling(self):
        pagetitle=self.driver.title
        print(pagetitle)
        obj_webutils = webUtils(self.driver)
        obj_webutils.windowHandler(pagetitle)

    def login(self,username,password):
        self.createAccount().click()
        self.googleBtn().click()
        self.windowHandling()
        self.getUsername().send_keys(username)
        self.nextBtn_user().click()
        self.getPasssword().send_keys(password)
        self.nextBtn_pwd().click()
        self.windowHandling()
