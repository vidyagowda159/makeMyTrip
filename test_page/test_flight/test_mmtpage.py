from settings import driver,origin,destination
from pages.mmt_pages.homePage import mmtHome
from pages.mmt_pages.flightsPage import flightDetails
from pages.mmt_pages.walletPage import Wallet
from genericlib.FixtureBaseClass import FixtureBaseClass

class Testmmt(FixtureBaseClass):

    def test_captureFlightDetails(self):
        objHome=mmtHome(driver)
        objHome.selectFlightOptions(origin,destination)

        objFlight= flightDetails(driver)
        objFlight.captureFlightDetails()

        objWallet=Wallet(driver)
        objWallet.walletBalance()

