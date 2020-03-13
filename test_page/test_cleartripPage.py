from settings import driver,url
from pages.cleartrip_pages.loginpage import clearTrip

class Testcleartrip:

    def get_url(self):
        driver.get(url)
        driver.maximize_window()

    def test_loginpage(self):
        obj_login = clearTrip(driver)
        obj_login.login("","")
