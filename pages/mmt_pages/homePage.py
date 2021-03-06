from selenium.webdriver.common.by import By
from genericlib.WebdriverUtils import webUtils
from datetime import date
import time
class mmtHome:

    _crossBtn='//span[@class="crossIcon popupSprite popupCrossIcon"]'
    _flightBtn='//span[@class="chNavIcon appendBottom2 chSprite chFlights active"]'
    _fromBtn='//input[@id="fromCity"]'
    _fromBtn2='//input[@placeholder="From"]'
    _blrDropDown='//p[text()="Bengaluru, India"]'
    _toBtn='//input[@id="toCity"]'
    _toBtn2='//input[@placeholder="To"]'
    _goaDropDown='//p[text()="Goa, India"]/ancestor::li'
    _depDate='//label[@for="departure"]'
    _roundTrip='//li[@data-cy="roundTrip"]'
    _searchBtn = '//a[text()="Search"]'

    def __init__(self,driver):
        self.driver=driver
        obj = webUtils(driver)
        obj.implicitTime(10)

    def click_crossBtn(self):
        print('in cross click btn')
        return self.driver.find_element(By.XPATH,self._crossBtn)

    def roundTrip(self):
        print('in roundtrip')
        return self.driver.find_element(By.XPATH,self._roundTrip)

    def search(self):
        print('in search')
        return self.driver.find_element(By.XPATH,self._searchBtn)

    def checkFlightBtn(self):
        print('in check test_flight btn')
        Bool=self.driver.find_element(By.XPATH,self._flightBtn).is_selected()
        if Bool==False:
            self.driver.find_element(By.XPATH, self._flightBtn).click()

    def flightFrom(self,departingPlace):
        print('in test_flight from')
        self.driver.find_element(By.XPATH,self._fromBtn).click()
        self.driver.find_element(By.XPATH,self._fromBtn2).send_keys(departingPlace)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self._blrDropDown).click()
        time.sleep(3)

    def flightTo(self,destination):
        print('in test_flight to')
        self.driver.find_element(By.XPATH, self._toBtn).click()
        self.driver.find_element(By.XPATH, self._toBtn2).send_keys(destination)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self._goaDropDown).click()

    def departureDate(self):
        print('in departure date')
        self.driver.find_element(By.XPATH,self._depDate)
        today = date.today()
        global todayDate
        todayDate = today.strftime("%B,%d,%Y").split(',')
        todayDate[1] = str(int(todayDate[1])+1)
        depDate = "//div[text()='{}']/../..//p[text()='{}']".format(todayDate[0], todayDate[1])
        print('depdate xpath')
        return self.driver.find_element(By.XPATH,depDate)

    def returnDate(self):
        print("in return date")
        todayDate[1] = str(int(todayDate[1])+1)
        retDate = "//div[text()='{}']/../..//p[text()='{}']".format(todayDate[0], todayDate[1])
        print('retdate xpath')
        return self.driver.find_element(By.XPATH, retDate)

    def selectFlightOptions(self,Origin,destination):
        self.click_crossBtn().click()
        self.checkFlightBtn()
        self.roundTrip().click()
        self.flightFrom(Origin)
        self.flightTo(destination)
        self.departureDate().click()
        self.returnDate().click()
        self.search().click()




