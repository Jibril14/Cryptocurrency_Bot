# this file save as a default for fetching cryptocurrencies
# of a pagination
from selenium.webdriver.common.by import By


def default_pagination(self):
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
            self.el_in_paginations += 1
            self.nname.append(name[el].text)
            self.price.append(price[el].text)
            self.change.append(change[el].text)
            self.change_percent.append(change_percent[el].text)
            self.market_cap.append(market_cap[el].text)
            self.total_volume.append(total_volume[el].text)
            self.circulating_supply.append(circulating_supply[el].text)