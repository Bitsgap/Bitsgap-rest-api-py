import asyncio
import logging
from unittest import TestCase

import time

from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestUserOrdersAdd(TestCase):

    """ Place order """
    def test_user_orders_add_valid_data(self):
        async def run_test():

            market = 'okex'
            pair = 'ETH_BTC'
            price = '0.015'
            amount = '0.1'
            side = 'buy'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)

            data = result['data'] if 'data' in result else None

            self.assertIsNotNone(data)

            self.assertIn('id', data)
            self.assertIn('price', data)
            self.assertIn('amount', data)
            self.assertIn('pair', data)
            self.assertIn('side', data)
            self.assertIn('type', data)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid market """

    def test_user_orders_add_invalid_market(self):
        async def run_test():

            market = 'invalid_market'
            pair = 'ETH_BTC'
            price = '0.015'
            amount = '0.1'
            side = 'buy'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid pair """
    def test_user_orders_add_invalid_pair(self):
        async def run_test():
            market = 'okex'
            pair = 'invalid_pair'
            price = '0.015'
            amount = '0.1'
            side = 'buy'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid side """
    def test_user_orders_add_invalid_side(self):
        async def run_test():
            market = 'okex'
            pair = 'ETH_BTC'
            price = '0.015'
            amount = '0.1'
            side = 'invalid'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid type """
    def test_user_orders_add_invalid_type(self):
        async def run_test():

            market = 'okex'
            pair = 'ETH_BTC'
            price = '0.015'
            amount = '0.1'
            side = 'buy'
            ord_type = 'invalid'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid price format """
    def test_user_orders_add_invalid_price_format(self):
        async def run_test():
            market = 'okex'
            pair = 'ETH_BTC'
            price = '0*250'
            amount = '0.1'
            side = 'buy'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid price zero """
    def test_user_orders_add_invalid_price_zero(self):
        async def run_test():
            market = 'okex'
            pair = 'ETH_BTC'
            price = '0'
            amount = '0.1'
            side = 'buy'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid price maximum """
    def test_user_orders_add_invalid_price_maximum(self):
        async def run_test():
            market = 'okex'
            pair = 'ETH_BTC'
            price = '250000000000'
            amount = '0.1'
            side = 'buy'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid amount zero """
    def test_user_orders_add_invalid_amount_zero(self):
        async def run_test():
            market = 'okex'
            pair = 'ETH_BTC'
            price = '0.015'
            amount = '0'
            side = 'buy'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid amount minimum """

    def test_user_orders_add_invalid_amount_minimum(self):
        async def run_test():
            market = 'okex'
            pair = 'ETH_BTC'
            price = '0.015'
            amount = '0.00000001'
            side = 'buy'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid amount maximum """
    def test_user_orders_add_invalid_amount_maximum(self):
        async def run_test():
            market = 'okex'
            pair = 'ETH_BTC'
            price = '0.015'
            amount = '150000000000000'
            side = 'buy'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()