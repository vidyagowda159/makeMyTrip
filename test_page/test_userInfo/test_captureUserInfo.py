from genericlib.FileLib import fileData
from settings import driver
from pages.mmt_pages.userInfoPage import userInfo
from genericlib.FixtureBaseClass import FixtureBaseClass
path=r'C:\Users\Vidyashree\PycharmProjects\makeMyTrip\testData\userInfo.json'

class TestUserinfo(FixtureBaseClass):

    def test_userdetails(self):
        obj_user =userInfo(driver)
        obj_user.get_userDetails()
        userDetails=obj_user.get_userDetails()
        obj_file=fileData()
        obj_file.writeJson(path,userDetails)
