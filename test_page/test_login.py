from settings import driver,url
from pages.login import mmtLogin
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

