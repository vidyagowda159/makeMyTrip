from settings import driver,url
from pages.mmt_pages.login import mmtLogin
from pages.mmt_pages.homePage import mmtHome
from genericlib.FileLib import fileData as f
from pages.mmt_pages.flightsPage import flightDetails
import pytest

class Testmmt:

    @pytest.fixture()
    def driver_methods(self):
        driver.get(url)
        driver.maximize_window()

    def test_validLogin(self,driver_methods):
        print("in valid login")
        objmmt=mmtLogin(driver)
        objfile=f()
        sheetname='Sheet1'
        maxRow=objfile.maxRowCount(sheetname)
        for i in range(1,maxRow+1):
            username=objfile.readData(sheetname,i+1,1,f.filepath_User)
            password=objfile.readData(sheetname,i+1,2,f.filepath_User)
            objmmt.login(username,password)

    def test_booking(self):
        objfile = f()
        objHome=mmtHome(driver)
        sheetname='Sheet2'
        maxRow = objfile.maxRowCount(sheetname)
        for i in range(1, maxRow + 1):
            origin = objfile.readData(sheetname, i + 1, 1, f.filepath_User)
            destination = objfile.readData(sheetname, i + 1, 2, f.filepath_User)
            objHome.selectFlightOptions(origin,destination)

    def test_flightd(self):
        obj = flightDetails(driver)
        obj.captureFlightDetails()

