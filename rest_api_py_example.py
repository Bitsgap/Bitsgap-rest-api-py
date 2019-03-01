from rest_api_py_lib import BitsgapClient

market = 'huobi'
symbol = 'XRP_BTC'

public_key = 'pub@'
private_key = 'pr@'
authClient = BitsgapClient(public_key, private_key)

# get orderbook
print(authClient.orderbook(market, symbol))
# get balance
print(authClient.balance())
