#!/usr/bin/env python

import configparser

accounts = {}
config = configparser.ConfigParser()
config.read('config.ini')

if config['coinbase']:
    from wallet_coinbase import get_coinbase_accounts
    get_coinbase_accounts(config, accounts)

if config['btcmarkets']:
    from btcmarkets import get_btcmarkets
    get_btcmarkets(config, accounts)

for currency in accounts:
    print(currency)
    curr_total = 0.0
    for wallet in accounts[currency]:
        print(wallet, accounts[currency][wallet])
        curr_total += float(accounts[currency][wallet])
    print("Total: {}".format(curr_total))
