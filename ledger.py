#!/usr/bin/env python

try:
	import coinbase
	import coinbase.wallet.client
	# https://developers.coinbase.com/docs/wallet/guides/bitcoin-wallet
except ImportError:
	exit("Please install coinbase package")

import configparser

accounts = {}
config = configparser.ConfigParser()
config.read('config.ini')

def get_coinbase_accounts(config=config):
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
				#print("{}\t{}\t(${} {})".format(current_currency, current_balance, account['native_balance']['amount'], account['native_balance']['currency']))
	except coinbase.wallet.error.AuthenticationError as e:
		print("Authentication error contacting coinbase API, error:")
		print(e)
		exit()


#print( config['btcmarkets']['api_key_private'])
# BTCMarkets has one, but it doesn't look great - https://github.com/BTCMarkets/api-client-python
get_coinbase_accounts()
for currency in accounts:
	print(currency)
	for wallet in accounts[currency]:
		print(wallet, accounts[currency][wallet])