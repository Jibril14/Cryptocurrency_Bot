import crypto_market.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class CryptoMarket(webdriver.Chrome):
    def __init__(self, driver_path=const.DRIVER_PATH):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path

        super(CryptoMarket, self).__init__()
        self.crypto_data = []
        self.nname = []
        self.price = []
        self.change = []
        self.change_percent = []
        self.market_cap = []
        self.total_volume = []
        self.circulating_supply = []
        self.el_in_paginations = 0 # keep track of each pagination elements
        self.implicitly_wait(15)
        self.maximize_window()

    def visit_page(self):
        return self.get(const.WEBSITE)

    def first_crypto_pagination(self):
        self.el_in_paginations += 25
        pagination_elements = self.find_elements(
            By.XPATH, '//div[@id="scr-res-table"]//table//tbody//tr')
        name = self.find_elements(
            By.XPATH, '//div[@id="scr-res-table"]//table//tbody//tr//td[2]')
        price = self.find_elements(
            By.XPATH, '//div[@id="scr-res-table"]//table//tbody//tr//td[3]')
        change = self.find_elements(
            By.XPATH, '//div[@id="scr-res-table"]//table//tbody//tr//td[4]')
        change_percent = self.find_elements(
            By.XPATH, '//div[@id="scr-res-table"]//table//tbody//tr//td[5]')
        market_cap = self.find_elements(
            By.XPATH, '//div[@id="scr-res-table"]//table//tbody//tr//td[6]')
        total_volume = self.find_elements(
            By.XPATH, '//div[@id="scr-res-table"]//table//tbody//tr//td[9]')
        circulating_supply = self.find_elements(
            By.XPATH, '//div[@id="scr-res-table"]//table//tbody//tr//td[10]')

        # store each innerHtml in a list.
        # this enable us append cryptos of other paginations
        for el in range(len(pagination_elements)):
            self.nname.append(name[el].text)
            self.price.append(price[el].text)
            self.change.append(change[el].text)
            self.change_percent.append(change_percent[el].text)
            self.market_cap.append(market_cap[el].text)
            self.total_volume.append(total_volume[el].text)
            self.circulating_supply.append(circulating_supply[el].text)

    def display_data(self):
        df_cryto_currency = pd.DataFrame(
            columns=[
                'Names',
                'Price  Intraday',
                'Change',
                'Change %',
                'Market Cap',
                'Total Volumn(All Currency) 24Hr',
                'Circulation Supply'])
        print(df_cryto_currency)

        # self.nname, self.price, self.change etc are all list
        for i in range(self.el_in_paginations):
            df_cryto_currency = df_cryto_currency.append(
                {
                    'Names': self.nname[i],
                    'Price  Intraday': self.price[i],
                    'Change': self.change[i],
                    'Change %': self.change_percent[i],
                    'Market Cap': self.market_cap[i],
                    'Total Volumn(All Currency) 24Hr': self.total_volume[i],
                    'Circulation Supply': self.circulating_supply[i]

                },
                ignore_index=True)

        print(df_cryto_currency)
