import crypto_market.constants as const
import os
from selenium import webdriver


class CryptoMarket(webdriver.Chrome):
    def __init__(self, driver_path = const.DRIVER_PATH):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path

        super(CryptoMarket, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def  visit_page(self):
        return self.get(const.WEBSITE)

   