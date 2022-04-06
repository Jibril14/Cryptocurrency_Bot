import crypto_market.constants as const
from crypto_market.default_pagination import default_pagination
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import sqlalchemy

class CryptoMarket(webdriver.Chrome):
    def __init__(self, driver_path=const.DRIVER_PATH):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path

        super(CryptoMarket, self).__init__()
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
        self.implicitly_wait(15)
        print('Fetching Second Pagination')
        default_pagination(self)

    def second_crypto_pagination(self):
        self.implicitly_wait(15)
        next_btn = self.find_element(By.XPATH, '//div[@id="scr-res-table"]/div[2]/button[3]/span//span')
        print('Fetching Second Pagination')
        next_btn.click()
        default_pagination(self)

    def third_crypto_pagination(self):
        self.implicitly_wait(15)
        next_btn = self.find_element(By.XPATH, '//div[@id="scr-res-table"]/div[2]/button[3]/span//span')
        print('Fetching Third Pagination')
        next_btn.click()
        default_pagination(self)   

   
    def display_data(self):
        # display data with pandas
        df_cryto_currency = pd.DataFrame(
            columns=[
                'Names',
                'Price  Intraday',
                'Change',
                'Change %',
                'Market Cap',
                'Total Volumn(All Currency) 24Hr',
                'Circulation Supply'])
        
        print("self.name array", self.nname)
        print("len.change array", len(self.change))
        # self.nname, self.price, self.change etc are all list
        for i in range(self.el_in_paginations):
            print(i)
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

        # save data into an excel file
        df_cryto_currency.to_excel('crypto_real_time.xlsx', index=False)

        # save data to postgresSql
        engine = sqlalchemy.create_engine('postgres://postgres:abcde@localhost:5432')
        df_cryto_currency.to_sql('crypto_real_time_info', engine, index=False)

        return self.close()
