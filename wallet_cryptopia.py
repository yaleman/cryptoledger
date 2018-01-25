import requests

#https://www.cryptopia.co.nz/api/GetBalance

from cryptopia_api import Api

def get_cryptopia(config, accounts):
    print(config['cryptopia']['api_key'],config['cryptopia']['api_secret'])
    api_wrapper = Api(config['cryptopia']['api_key'],config['cryptopia']['api_secret'])

    print(api_wrapper.api_query(feature_requested='GetBalance'))