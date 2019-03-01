from rest-api-py-lib import BitsgapClient

market = 'huobi'
symbol = 'XRP_BTC'

public_key = ''
private_key = ''
authClient = BitsgapClient(public_key, private_key)

# get orderbook
print(authClient.orderbook(market, symbol))
# get balance
print(authClient.balance())
