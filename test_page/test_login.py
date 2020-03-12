from settings import driver,url
from pages.login import mmtLogin
from pages.homePage import mmtHome
from genericlib.FileLib import fileData
import pytest
import allpaths as a
class Testlogin:

    @pytest.fixture()
    def driver_methods(self):
        driver.get(url)
        driver.maximize_window()

    def test_validLogin(self,driver_methods):
        print("in valid login")
        objmmt=mmtLogin(driver)
        objfile=fileData()
        maxRow=objfile.maxRowCount()
        for i in range(1,maxRow+1):
            username=objfile.readData('Sheet1',i+1,1,a.filepath)
            password=objfile.readData('Sheet1',i+1,2,a.filepath)
            objmmt.login(username,password)

class Testhome:

    def test_booking(self):
        objfile = fileData()
        objHome=mmtHome(driver)
        maxRow = objfile.maxRowCount()
        for i in range(1, maxRow + 1):
            origin = objfile.readData('Sheet2', i + 1, 1, a.filepath)
            destination = objfile.readData('Sheet2', i + 1, 2, a.filepath)
            objHome.booking(origin,destination)
