from settings import driver,url,username,pwd
from pages.mmt_pages.login import mmtLogin
from pages.mmt_pages.logoutPage import Logout
import pytest

class FixtureBaseClass:

     @pytest.fixture(scope="class",autouse=True)
     def launch(self):
          driver.get(url)
          driver.maximize_window()
          yield
          driver.close()

     @pytest.mark.dependency(name="Login")
     @pytest.fixture(scope="function",autouse=True)
     def login(self):
         objmmt = mmtLogin(driver)
         objmmt.login(username, pwd)

     @pytest.mark.dependency(depends=["Login"])
     def logout(self):
         obj_logout = Logout(driver)
         obj_logout.logout()
