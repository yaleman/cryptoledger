import requests

#https://www.cryptopia.co.nz/api/GetBalance

from cryptopia_api import PrivCApi

def get_cryptopia(config, accounts):
    api_wrapper = PrivCApi(config['cryptopia']['api_key'],config['cryptopia']['api_secret'])

    for balance in api_wrapper.getbalance():
        if balance['Available'] != 0.0:
            #print(balance)
            if balance['Symbol'] not in accounts:
                accounts[balance['Symbol']] = {}
            accounts[balance['Symbol']]['cryptopia'] = balance['Total']