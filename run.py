from crypto_market.crypto_market import CryptoMarket


bot = CryptoMarket()
bot.visit_page()

try:
    bot.first_crypto_pagination()
    bot.second_crypto_pagination()
    bot.third_crypto_pagination()  
except:
    print("Network Errror or Element xpath may have been changed")
bot.display_data()

