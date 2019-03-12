import requests
import json
import hmac
import hashlib
import logging

VERSION = 'v1'
BASE_URL = 'https://bitsgap.com/api'

# market data
PATH_SYMBOLS = "markets"
PATH_LAST_PRICE = "last-price"
PATH_ORDERBOOK = "order-book"
PATH_RECENT_TRADES = "recent-trades"
PATH_OHLC = "ohlc"

#user data
PATH_KEYS = 'keys'
PATH_BALANCE = "balance"
PATH_MESSAGES = "messages"
PATH_ORDERS_HISTORY = "orders/history"
PATH_ORDERS_OPEN = "orders/open"
PATH_ORDERS_ADD = "orders/add"
PATH_ORDERS_CANCEL = "orders/cancel"
PATH_ORDERS_MOVE = "orders/move"

# HTTP request timeout in seconds
TIMEOUT = 10.0

logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s', level=logging.DEBUG)


class BitsgapBaseClient(object):
    def __init__(self, key, secret, proxies=None):
        self.URL = f"{BASE_URL}/{VERSION}"
        self.KEY = key
        self.SECRET = secret
        self.PROXIES = proxies

    def url_for(self, path, market_type=None):
        if market_type:
            path = f"{market_type}/{path}"
        return f"{self.URL}/{path}"

    def _sign_payload(self, payload):
        return hmac.new(self.SECRET.encode(),
                        payload.encode(),
                        digestmod=hashlib.sha512).hexdigest()

    def _post(self, url, params=None):
        req_params = {
            'key': self.KEY
        }

        message_dict = {
            'key': self.KEY
        }
        if params:
            message_dict.update(params)

        params_str = json.dumps(message_dict)

        req_params['data'] = params_str

        req_params['signature'] = self._sign_payload(params_str)

        req = requests.post(url, data=req_params)

        logging.debug(url)

        logging.debug(req_params)

        if req.status_code != 200:
            logging.error(u"Failed to request:%s %d headers:%s", url, req.status_code, req.headers)
        try:
            return req.json()
        except Exception as e:
            logging.exception('Failed to POST:%s result:%s', url, req.text)
            raise e


class BitsgapClient(BitsgapBaseClient):

    """ Client for the Bitsgap API. """
    def markets(self):
        """
        POST /api/v1/markets
        POST https://bitsgap.com/api/v1/markets
        {
          "status": "ok",
          "time": 1550059232,
          "data": {
            "binance": [
              {
                "pair_from": "ADABNB",
                "pair_to": "ADA_BNB"
              },
              ...
              {
                "pair_from": "ZRXETH",
                "pair_to": "ZRX_ETH"
              }
            ],
            ...
            "zb.com": [
              {
                "pair_from": "1st_btc",
                "pair_to": "1ST_BTC"
              },
              ...
              {
                "pair_from": "zrx_usdt",
                "pair_to": "ZRX_USDT"
              }
            ]
          }
        }

        """
        return self._post(self.url_for(PATH_SYMBOLS))

    def last_price(self, market, symbol):
        """
        # Return last price for selected market and pair

        # Request
        POST /api/v1/last-price
        POST https://bitsgap.com/api/v1/last-price

        # Params
        market - market name
        pair - Bitsgap pair name

        # Response
        {
          "status": "ok",
          "time": 1550139967,
          "data": {
            "market": "kraken",
            "pair": "BTC_USD",
            "ask": 3562,
            "bid": 3561.6
          }
        }
        """
        return self._post(self.url_for(PATH_LAST_PRICE), params={'market': market, 'pair': symbol})

    def orderbook(self, market, symbol):
        """
        # Return orderbook for selected market and pair

        # Request
        POST /api/v1/orderbook
        POST https://bitsgap.com/api/v1/orderbook

        # Params
        market - market name
        pair - Bitsgap pair name

        # Response
        {
          "status": "ok",
          "time": 1550142307,
          "data": {
            "asks": {
              "0.03456": 0.548,
              "0.03397": 0.30571034,
              ...
              "0.03384": 144.57178082
            },
            "bids": {
              "0.03311": 0.30313283,
              "0.03358": 0.11167361,
              ...
              "0.03357": 0.14015984
            }
        }
        """
        return self._post(self.url_for(PATH_ORDERBOOK), params={'market': market, 'pair': symbol})

    def recent_trades(self, market, symbol):
        """
        # Return recent trades for selected market and pair

        # Request
        POST /api/v1/recent-trades
        POST https://bitsgap.com/api/v1/recent-trades

        # Params
        market - market name
        pair - Bitsgap pair name

        # Response
        {
          "status": "ok",
          "time": 1551198454,
          "data": {
            "market": "kraken",
            "pair": "ADA_USD",
            "data": [
              {
                "u": 1551197501,         // trade timestamp
                "am": "7333.17200000",   // amount
                "s": "buy",              // trade side "buy" or "sell"
                "p": "0.042593"          // trade price
              },
              ...
              {
                "u": 1551177580,
                "am": "0.00097975",
                "s": "buy",
                "p": "0.042937"
              }
            ]
          }
        }
        """
        return self._post(self.url_for(PATH_RECENT_TRADES), params={'market': market, 'pair': symbol})

    def ohlc(self, market, symbol, start, end):
        """
        # Return ohlc data for selected market and pair in selected period
        # Maximum request interval 72 hours

        # Request
        POST /api/v1/ohlc
        POST https://bitsgap.com/api/v1/ohlc

        # Params
        market - market name
        pair - Bitsgap pair name
        start - start time of the period
        end - end time of the period

        # Response
        {
          "status": "ok",
          "time": 1551198180,
          "data": [
              {
                "timestamp": 1551198180,
                "open": 3892.2,
                "high": 3895.1,
                "low": 3892.2,
                "close": 3894.1,
                "volume": {
                  "buy": 0,
                  "sell": 0
                }
              },
              {
                "timestamp": 1551198240,
                "open": 3894,
                "high": 3894.9,
                "low": 3893.9,
                "close": 3894.3,
                "volume": {
                  "buy": 0.13194656,
                  "sell": 0
                }
              }
            ]
        }
        """
        return self._post(self.url_for(PATH_OHLC), params={'market': market, 'pair': symbol, 'start': start, 'end': end})

    # real market
    # trading methods

    def keys(self):
        """
        # Return user API keys and key status

        # Request
        POST /api/v1/keys
        POST https://bitsgap.com/api/v1/keys

        # Params
        None

        # Response
        {
          "status": "ok",
          "time": 1552296397,
          "data": {
            "zb.com": {
              "key": "dfxxxxb8-9xx6-4xxd-bxxe-efxxxxxxxx8e",
              "status": "disabled",
              "uts": 1551692245
            },
            "exmo": {
              "key": "K-c1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx50",
              "status": "active",
              "uts": 1552293501
            },
            "kucoin": {
              "key": "5cxxxxxxxxxxxxxxxxxxxx12",
              "status": "incorrect",
              "uts": 1552295796,
              "message": "Invalid API-key: KC-API-KEY not exists"
            }
          }
        }
        """
        return self._post(self.url_for(PATH_KEYS))

    def balance(self):
        """
        # Return balance for selected user for all markets, where user added API keys

        # Request
        POST /api/v1/balance
        POST https://bitsgap.com/api/v1/balance

        # Params
        None

        # Response
        {
          "status": "ok",
          "data": {
            "cex.io": {
              "balance": {
                "EUR": 13.61,
                "USD": 31.04
              },
              "uts": 1548234796.982768,
              "total": {
                "EUR": 13.61,
                "USD": 31.04
              }
            },
            ...
            "binance": {
              "balance": {
                "ETH": 0.00028982,
                "SC": 4995,
                "WAVES": 0.00256,
                "BTC": 0.00811678,
              },
              "uts": 1550130203.1725256,
              "total": {
                "ETH": 0.00028982,
                "WAVES": 0.00256,
                "SC": 4995,
                "BTC": 0.00811678,
              }
            }
          }
        }
        """
        return self._post(self.url_for(PATH_BALANCE))

    def messages(self):
        """
        # Return last 100 trade messages for selected user

        # Request
        POST /api/v1/messages
        POST https://bitsgap.com/api/v1/messages

        # Params
        None

        # Response
        {
          "status": "ok",
          "data": [
            {
              "t": 1550130203,
              "type": "success",
              "trade": "real",
              "text": "binance: filled limit sell 290 ADA_BNB per 0.005"
            },
            {
              "t": 1550130137,
              "type": "success",
              "trade": "real",
              "text": "binance: placed limit sell 290 ADA_BNB per 0.005"
            },
            ...
            {
              "t": 1549876741,
              "type": "success",
              "trade": "real",
              "text": "bit-z: filled limit buy 125.76 777_BTC per 0.00000005"
            }
          ]
        }
        """
        return self._post(self.url_for(PATH_MESSAGES))

    def orders_history(self, market):
        """
        # Return last 20 trades for selected user

        # Request
        POST /api/v1/orders/history
        POST https://bitsgap.com/api/v1/orders/history

        # Params
        market - market name

        # Response
        {
          "status": "ok",
          "data": [
            {
              "price": "0.00001149",
              "order_type": "market",
              "amount_init": "79.37062937",
              "amount": "79.37062937",
              "sid": "c2xx71xxb3xx40xx80xx64xxc2xxd2xx",
              "id": "XXXXXX-XXXXX-XXXXXX",
              "price_avg": "0.00001149",
              "type": "buy",
              "state": "filled",
              "time": 1549823293.934,
              "pair": "ADA_BTC",
              "created": 1549823293.934
            },
            ...
            {
              "price": "0.0000121",
              "order_type": "limit",
              "amount_init": "100",
              "created": 1547199916.525,
              "amount": "100",
              "price_avg": "0.0000121",
              "id": "XXXXXX-XXXXX-XXXXXX",
              "type": "buy",
              "time": 1547199916.525,
              "pair": "ADA_BTC",
              "state": "filled"
            }
          ]
        }
        """
        return self._post(self.url_for(PATH_ORDERS_HISTORY), params={'market': market})

    def orders_open(self, market):
        """
        # Return open orders for selected user and market

        # Request
        POST /api/v1/orders/open
        POST https://bitsgap.com/api/v1/orders/open

        # Params
        market - market name

        # Response
        {
          "status": "ok",
          "data": [
            {
              "price": "0.005",
              "price_avg": "0",
              "amount_init": "290",
              "pid": "12792274",
              "pair": "ADA_BNB",
              "guid": "96bxxacxxda3xx688xxcd7xx4acxx4ef",
              "source": "market",
              "state": "opened",
              "type": "limit",
              "volume": "290",
              "side": "sell",
              "uts": 1550745027.645
            }
          ]
        }
        """
        return self._post(self.url_for(PATH_ORDERS_OPEN), params={'market': market})

    def orders_add(self, market,
                        pair,
                        amount,
                        price,
                        side,
                        order_type
                        ):
        """
        # Return result of place order

        # Request
        POST /api/v1/orders/add
        POST https://bitsgap.com/api/v1/orders/add

        # Params
        market - market name
        pair - Bitsgap pair name
        amount - order amount
        price - order price
        side - order side: buy or sell
        type - order type: limit, market, shadow

        # Response
        {
          "status": "ok",
          "time": 1551241472,
          "data": {
            "price": "0.25",
            "uts": 1551241472.8151486,
            "amount_init": "150",
            "guid": "e9xxxxxxxxxxxxxxxxxxxxxxxxxxxxb9",
            "side": "sell",
            "pid": "2exxxx7b-3xxc-4xx0-bxxc-81xxxxxxxxcf",
            "source": "api",
            "type": "limit",
            "state": "opened",
            "volume": "150",
            "pair": "EDR_USD",
            "our": 1
          }
        }
        """
        params = {
            'market': market,
            'pair': pair,
            'amount': amount,
            'price': price,
            'side': side,
            'type': order_type
        }
        return self._post(self.url_for(PATH_ORDERS_ADD), params=params)

    def orders_cancel(self, market, id):
        """
        # Cancel real market order by id

        # Request
        POST /api/v1/orders/cancel
        POST https://bitsgap.com/api/v1/orders/cancel

        # Params
        market - market name
        id - order ID

        # Response
        {
          "status": "ok",
          "time": 1551250312,
          "data": {
            "price": "0.2",
            "uts": 1551241373.593,
            "amount_init": "150",
            "guid": "e8xxxxxxxxxxxxxxxxxxxxxxxxxxxx2c",
            "side": "sell",
            "pid": "59xxxxda-exx8-4xx1-axxd-dxxxxxxxxxxb",
            "source": "site",
            "type": "limit",
            "state": "closed",
            "volume": "150",
            "pair": "EDR_USD",
            "our": 1
          }
        }
        """
        return self._post(self.url_for(PATH_ORDERS_CANCEL), params={'market': market, 'id': id})

    def orders_move(self, market, id, price):
        """
        # Move real market order by id to new price
        # If market dosn't support move action order will be cancelled and placed with new price

        # Request
        POST /api/v1/orders/move
        POST https://bitsgap.com/api/v1/orders/move

        # Params
        market - market name
        id - order ID
        price - new price value

        # Response

        """
        return self._post(self.url_for(PATH_ORDERS_MOVE), params={'market': market, 'id': id, 'price': price})

    # demo trading
    def demo_balance(self):
        """
        # Return balance for selected user for all markets, where user added API keys

        # Request
        POST /api/v1/demo/balance
        POST https://bitsgap.com/api/v1/demo/balance

        # Params
        None

        # Response
        {
          "status": "ok",
          "data": {
            "poloniex.demo": {
              "total": {
                "ARDR": 14,
                "BTC": 4.0419087099999995,
                "USD": 0.00008671905795520907
              },
              "balance": {
                "ARDR": 14,
                "BTC": 4.0419087099999995,
                "USD": 0.00008671905795520907
              }
            },
            ...
            "livecoin.demo": {
              "total": {
                "BTC": 0.18401769999999995,
                "EUR": 12055.604291973374,
                "USD": 70542.85009198637
              },
              "balance": {
                "BTC": 0.18401769999999995,
                "EUR": 12055.604291973374,
                "USD": 70542.85009198637
              }
            },
          }
        }
        """
        return self._post(self.url_for(PATH_BALANCE, 'demo'))

    def demo_orders_history(self, market):
        """
        # Return last 20 trades for selected user

        # Request
        POST /api/v1/demo/orders/history
        POST https://bitsgap.com/api/v1/demo/orders/history

        # Params
        market - market name

        # Response
        {
          "status": "ok",
          "data": [
            {
              "amount": 0.322,
              "price": 3292.5,
              "descr": "",
              "id": "28ae7f296def42b88e1543280d56b9f9",
              "type": "buy",
              "time": 1547117407,
              "pair": "BTC_EUR"
            },
            ...
            {
              "amount": 0.11,
              "price": 3486,
              "descr": "",
              "id": "c5c41601dfb044b3a3788033ca24b943",
              "type": "sell",
              "time": 1546795036,
              "pair": "BTC_EUR",
              "sid": "d9f909ff896c4af6b4faae3687a8bcd3"
            }
          ]
        }
        """
        return self._post(self.url_for(PATH_ORDERS_HISTORY, 'demo'), params={'market': market})

    def demo_orders_open(self, market):
        """
        # Return open orders for selected user and market

        # Request
        POST /api/v1/demo/orders/open
        POST https://bitsgap.com/api/v1/demo/orders/open

        # Params
        market - market name

        # Response
        {
          "status": "ok",
          "data": [
            {
              "pid": "43xxxxxxxxxxxxxxxxxxxxxxxxxxxxx36", // market order id
              "uts": 1551241582, // order creation time
              "price": 0.04,     // order price
              "pair": "ADA_USD", // order pair
              "type": "limit",   // order type
              "volume": 10,
              "side": "buy",
              "shadow": false   // shadow order flag
            }
          ]
        }
        """
        return self._post(self.url_for(PATH_ORDERS_OPEN, 'demo'), params={'market': market})

    def demo_orders_add(self, market,
                        pair,
                        amount,
                        price,
                        side,
                        order_type
                        ):
        """
        # Return result of place order

        # Request
        POST /api/v1/demo/orders/add
        POST https://bitsgap.com/api/v1/demo/orders/add

        # Params
        market - market name
        pair - Bitsgap pair name
        amount - order amount
        price - order price
        side - order side: buy or sell
        type - order type: limit, market, shadow

        # Response
        {
          "status": "ok",
          "time": 1551855974,
          "data": {
            "price": 0.02,
            "amount_init": 10,
            "guid": "caxxxxxxxxxxxxxxxxxxxxxxxxxxxx1d",
            "amount": 10,
            "state": "opened",
            "type": "limit",
            "pair": "ADA_USD",
            "side": "buy",
            "uts": 1551855974.5700731
          }
        }
        """
        return self._post(self.url_for(PATH_ORDERS_ADD, 'demo'), params={'market': market,
                                                                         'pair': pair,
                                                                         'amount': amount,
                                                                         'price': price,
                                                                         'side': side,
                                                                         'type': order_type})

    def demo_orders_cancel(self, market, id):
        """
        # Return result of cancel order

        # Request
        POST /api/v1/demo/orders/cancel
        POST https://bitsgap.com/api/v1/demo/orders/cancel

        # Params
        market - market name
        id - order ID

        # Response
        {
          "status": "ok",
          "time": 1551861893,
          "data": {
            "amount": 10,
            "price": 0.02,
            "uts": 1551861893.0678823,
            "side": "buy",
            "state": "closed",
            "amount_init": 10,
            "pair": "ADA_USD",
            "guid": "4dxxxxxxxxxxxxxxxxxxxxxxxxxxxc1"
          }
        }
        """
        return self._post(self.url_for(PATH_ORDERS_CANCEL, 'demo'), params={'market': market, 'id': id})

    def demo_orders_move(self, market, id, price):
        """
        # Return result of move order

        # Request
        POST /api/v1/demo/orders/move
        POST https://bitsgap.com/api/v1/demo/orders/move

        # Params
        market - market name
        id - order ID
        price - new order price

        # Response
        """
        return self._post(self.url_for(PATH_ORDERS_MOVE, 'demo'), params={'market': market, 'id': id, 'price': price})


    def demo_keys(self):
        """
        # Return user API keys and key status

        # Request
        POST /api/v1/keys
        POST https://bitsgap.com/api/v1/keys

        # Params
        None

        # Response
        {
          "status": "ok",
          "time": 1552296397,
          "data": {
            "zb.com": {
              "key": "dfxxxxb8-9xx6-4xxd-bxxe-efxxxxxxxx8e",
              "status": "disabled",
              "uts": 1551692245
            },
            "exmo": {
              "key": "K-c1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx50",
              "status": "active",
              "uts": 1552293501
            },
            "kucoin": {
              "key": "5cxxxxxxxxxxxxxxxxxxxx12",
              "status": "incorrect",
              "uts": 1552295796,
              "message": "Invalid API-key: KC-API-KEY not exists"
            }
          }
        }
        """
        return self._post(self.url_for(PATH_KEYS, 'demo'))