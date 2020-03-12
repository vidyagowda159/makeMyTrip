from selenium.webdriver.common.by import By
class mmtHome:
    _crossBtn='//span[@class="crossIcon popupSprite popupCrossIcon"]'
    _flightBtn='//span[@class="chNavIcon appendBottom2 chSprite chFlights active"]'
    _fromBtn='//input[@id="fromCity"]'
    _fromBtn2='//input[@class="react-autosuggest__input react-autosuggest__input--open"]'
    _blrDropDown='//p[text()="Bengaluru, India"]'
    _toBtn='//input[@id="toCity"]'
    _toBtn2='//input[@class="react-autosuggest__input react-autosuggest__input--open"]'
    _goaDropDown='//p[text()="Goa, India"]'

    def __init__(self,driver):
        self.driver=driver

    def click_crossBtn(self):
        self.driver.find_element(By.XPATH,self._crossBtn)

    def checkFlightBtn(self):
        Bool=self.driver.find_element(By.XPATH,self._flightBtn).is_selected()
        if Bool==False:
            self.driver.find_element(By.XPATH, self._flightBtn).click()

    def flightFrom(self,departingPlace):
        self.driver.find_element(By.XPATH,self._fromBtn).click()
        self.driver.find_element(By.XPATH,self._fromBtn2).send_keys(departingPlace)
        self.driver.find_element(By.XPATH,self._blrDropDown).click()

    def flightTo(self,destination):
        self.driver.find_element(By.XPATH, self._toBtn).click()
        self.driver.find_element(By.XPATH, self._toBtn2).send_keys(destination)
        self.driver.find_element(By.XPATH, self._goaDropDown).click()

    def booking(self,departingPlace,destination):
        self.click_crossBtn().click()
        self.checkFlightBtn()
        self.flightFrom(departingPlace)
        self.flightTo(destination)




