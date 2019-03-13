import asyncio
import logging
from unittest import TestCase

import time

from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestUserDemoOrdersAdd(TestCase):

    """ Place order on demo market """
    def test_user_demo_orders_add_valid_data(self):
        async def run_test():

            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0.250'
            amount = '150'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'ok')
            self.assertIn('time', result)
            self.assertIn('data', result)

            data = result['data']
            self.assertIsNotNone(data)
            # check fields
            self.assertIn('id', data)
            self.assertIn('price', data)
            self.assertIn('amount', data)
            self.assertIn('state', data)
            self.assertIn('pair', data)
            self.assertIn('type', data)
            self.assertIn('side', data)
            self.assertIn('uts', data)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid market """
    def test_user_demo_orders_add_invalid_market(self):
        async def run_test():

            market = 'no_market'
            pair = 'EDR_USD'
            price = '0.250'
            amount = '150'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIn('time', result)
            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')

            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid market """
    def test_user_demo_orders_add_invalid_pair(self):
        async def run_test():
            market = 'bittrex'
            pair = 'no_pair'
            price = '0.250'
            amount = '150'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIn('time', result)
            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')

            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid side """
    def test_user_demo_orders_add_invalid_side(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0.250'
            amount = '150'
            side = 'invalid'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIn('time', result)
            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')

            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid type """
    def test_user_demo_orders_add_invalid_type(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0.250'
            amount = '150'
            side = 'sell'
            ord_type = 'invalid'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIn('time', result)
            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')

            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid price format """

    def test_user_demo_orders_add_invalid_price_format(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0*250'
            amount = '150'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIn('time', result)
            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')

            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid zero price """

    def test_user_demo_orders_add_invalid_price_zero(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0'
            amount = '150'
            side = 'buy'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIn('time', result)
            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')

            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid amount format"""
    def test_user_demo_orders_add_invalid_amount_format(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0.25'
            amount = '100*'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIn('time', result)
            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')

            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid amount zero"""
    def test_user_demo_orders_add_invalid_amount_zero(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0.25'
            amount = '0'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIn('time', result)
            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')

            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
