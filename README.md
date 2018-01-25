# CryptoLedger

Pulls crypto balances from all over the place and tells you what you have.

## Installation

You'll need the following packages:

- requests
- coinbase API (pip install coinbase)

## Configuration

Make a `config.ini` file with the following fields, if you don't have that account, don't add the fields and it'll ignore it.

```
[coinbase]
api_key = yourkey
api_secret = yoursecret
api_version = 2018-01-12 (shown on the api page)

[cryptopia]
api_key = yourkey
api_secret = yoursecret

[btcmarkets]
api_key_public = yourkey
api_key_private = yourprivatekey
```