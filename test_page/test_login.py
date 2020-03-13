from settings import driver,url
from pages.login import mmtLogin
from pages.homePage import mmtHome
from genericlib.FileLib import fileData as f
from pages.flightsPage import flightDetails
import pytest
class Testlogin:

    @pytest.fixture()
    def driver_methods(self):
        driver.get(url)
        driver.maximize_window()

    def test_validLogin(self,driver_methods):
        print("in valid login")
        objmmt=mmtLogin(driver)
        objfile=f()
        maxRow=objfile.maxRowCount()
        for i in range(1,maxRow+1):
            username=objfile.readData('Sheet1',i+1,1,f.filepath_User)
            password=objfile.readData('Sheet1',i+1,2,f.filepath_User)
            objmmt.login(username,password)

class Testhome:

    def test_booking(self):
        objfile = f()
        objHome=mmtHome(driver)
        maxRow = objfile.maxRowCount()
        for i in range(1, maxRow + 1):
            origin = objfile.readData('Sheet2', i + 1, 1, f.filepath_User)
            destination = objfile.readData('Sheet2', i + 1, 2, f.filepath_User)
            objHome.selectFlightOptions(origin,destination)

class Testflightspage:
    def test_flightd(self):
        obj = flightDetails(driver)
        obj.captureFlightDetails()
