#!/usr/bin/env python

try:
	import coinbase
	import coinbase.wallet.client
	# https://developers.coinbase.com/docs/wallet/guides/bitcoin-wallet
except ImportError:
	exit("Please install coinbase package")

import configparser


config = configparser.ConfigParser()
config.read('config.ini')

def get_coinbase_accounts(config=config):
	coinbase_client = coinbase.wallet.client.Client(config['coinbase']['api_key'], config['coinbase']['api_secret'])

	try:
		coinbase_accounts = coinbase_client.get_accounts()
	except coinbase.wallet.error.AuthenticationError as e:
		print("Authentication error contacting coinbase API, error:")
		print(e)
		exit()
	print(coinbase_accounts)

#print( config['btcmarkets']['api_key_private'])
# BTCMarkets has one, but it doesn't look great - https://github.com/BTCMarkets/api-client-python
get_coinbase_accounts()