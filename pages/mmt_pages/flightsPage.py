from genericlib.FileLib import fileData
from selenium.webdriver.common.by import By
from genericlib.WebdriverUtils import webUtils
obj_f = fileData()

class flightDetails:

    _flightName='//span[@class="airlineInfo-sctn"]'
    _depTime = '//div[@class="dept-time"]'
    _price = '//span[@class="actual-price"]'

    def __init__(self,driver):
        self.driver = driver
        obj = webUtils(driver)
        obj.implicitTime(10)

    def for_loop(self,xpath_exprn,xpath2,column):
        filepath = obj_f.filepath_flightsheet
        value = self.driver.find_elements(By.XPATH,xpath_exprn)

        for i in range(1,len(value)+1):
            name= self.driver.find_element(By.XPATH,xpath2.format(i)).text
            obj_f.writexlData("Ecocnomy",i+1,column,filepath,name)

    def flightName(self):
        f_name='(//span[@class="airlineInfo-sctn"])[{}]'
        self.for_loop(self._flightName,f_name,1)

    def flightTime(self):
        f_time='(//div[@class="dept-time"])[{}]'
        self.for_loop(self._depTime,f_time,2)

    def flightPrice(self):
        f_price='(//span[@class="actual-price"])[{}]'
        self.for_loop(self._price,f_price,3)

    def captureFlightDetails(self):
        self.flightName()
        self.flightTime()
        self.flightPrice()