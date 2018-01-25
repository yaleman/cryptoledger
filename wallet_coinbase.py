try:
    import coinbase
    import coinbase.wallet.client
# https://developers.coinbase.com/docs/wallet/guides/bitcoin-wallet
except ImportError:
    exit("Please install coinbase package")

def get_coinbase_accounts(config, accounts):
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