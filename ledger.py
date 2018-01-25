#!/usr/bin/env python

import configparser

accounts = {}
config = configparser.ConfigParser()
config.read('config.ini')

if config['coinbase']:
    from wallet_coinbase import get_coinbase
    get_coinbase(config, accounts)

if config['btcmarkets']:
    from wallet_btcmarkets import get_btcmarkets
    get_btcmarkets(config, accounts)

# broken currently
#if config['cryptopia']:
#    from wallet_cryptopia import get_cryptopia
#    get_cryptopia(config, accounts)

for currency in accounts:
    print(currency)
    curr_total = 0.0
    for wallet in accounts[currency]:
        print(wallet, accounts[currency][wallet])
        curr_total += float(accounts[currency][wallet])
    print("Total: {}".format(curr_total))
