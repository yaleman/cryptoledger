#!/usr/bin/env python

try:
    import coinbase
    import coinbase.wallet.client
    # https://developers.coinbase.com/docs/wallet/guides/bitcoin-wallet
except ImportError:
    exit("Please install coinbase package")


#try:
from btcmarkets import BTCMarkets 
#except ImportError:
    #exit("Can't load BTCmarkets module")

import configparser

accounts = {}
config = configparser.ConfigParser()
config.read('config.ini')

def get_coinbase_accounts(config=config):
    """ handle coinbase API calls
    config needs these values, all taken from coinbase. remember, 48 hour delay if you make changes to the API keys.
    [coinbase]
    api_key = blah
    api_secret = blah
    api_version = 2018-01-12
    """

    coinbase_client = coinbase.wallet.client.Client(config['coinbase']['api_key'], config['coinbase']['api_secret'])

    try:
        coinbase_accounts = coinbase_client.get_accounts()
        #print(coinbase_accounts)
        for account in coinbase_accounts['data']:
            if float(account['balance']['amount']) != 0.0:
                current_currency = account['balance']['currency']
                current_balance = account['balance']['amount']
                if current_currency not in accounts:
                    accounts[current_currency] = {}
                accounts[current_currency]['coinbase'] = current_balance
    except coinbase.wallet.error.AuthenticationError as e:
        print("Authentication error contacting coinbase API, error:")
        print(e)
        exit()

def get_btcmarkets(config=config):
    """ handle the BTCMarkets API calls 
    config needs:
    [btcmarkets]
    api_key_public = blah
    api_key_private = blah
    """
    # BTCMarkets has one, but it doesn't look great - https://github.com/BTCMarkets/api-client-python
    client = BTCMarkets(config['btcmarkets']['api_key_public'],config['btcmarkets']['api_key_private'])
    #print (client.get_market_tick('ETH','AUD'))
    #print(client.trade_history('ETH', 'AUD', 10, 1))
    #print("BTC Account Balances")
    balances = client.account_balance()
    for balance in balances:
        if balance['balance'] != 0:
            if balance['currency'] not in accounts:
                accounts[balance['currency']] = {}
            accounts[balance['currency']]['BTCMarkets'] = float(balance['balance'])/100000000


get_coinbase_accounts()

get_btcmarkets()

for currency in accounts:
    print(currency)
    curr_total = 0.0
    for wallet in accounts[currency]:
        print(wallet, accounts[currency][wallet])
        curr_total += float(accounts[currency][wallet])
    print("Total: {}".format(curr_total))
