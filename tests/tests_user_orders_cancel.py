import asyncio
import logging
from unittest import TestCase

import time

from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestUserOrdersCancel(TestCase):

    """ Cancel order """
    def test_user_orders_cancel_valid_data(self):
        async def run_test():

            market = 'bittrex'

            lib = BitsgapClient(public_key, private_key)

            # get open orders
            result = lib.orders_open(market)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)

            data = result['data']

            self.assertIsNotNone(data)
            self.assertTrue(len(data) > 0)
            self.assertIn('id', data[0])

            id = data[0]['id']

            self.assertIsNotNone(id)

            result_cancel = lib.orders_cancel(market, id)

            self.assertIn('status', result_cancel)
            self.assertTrue(result_cancel['status'] == 'ok')
            self.assertIn('data', result_cancel)
            self.assertIn('time', result_cancel)

            data = result_cancel['data']

            self.assertIsNotNone(data)

            self.assertIn('id', data)
            self.assertIn('price', data)
            self.assertIn('amount_init', data)
            self.assertIn('pair', data)
            self.assertIn('state', data)
            self.assertIn('type', data)
            self.assertIn('side', data)
            self.assertIn('uts', data)
            self.assertIn('amount', data)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Cancel executed order """
    def test_user_orders_cancel_executed_order(self):
        async def run_test():

            market = 'bittrex'

            lib = BitsgapClient(public_key, private_key)

            # get executed orders
            result = lib.orders_history(market)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)

            data = result['data']

            self.assertIsNotNone(data)
            self.assertTrue(len(data) > 0)
            self.assertIn('id', data[0])

            id = data[0]['id']

            self.assertIsNotNone(id)

            result_cancel = lib.orders_cancel(market, id)

            self.assertIn('status', result_cancel)
            self.assertTrue(result_cancel['status'] == 'error')
            self.assertIn('message', result_cancel)
            self.assertIn('time', result_cancel)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Cancel invalid order id """
    def test_user_orders_cancel_invalid_id(self):
        async def run_test():
            market = 'bittrex'
            id = 'invalid'

            lib = BitsgapClient(public_key, private_key)

            result_cancel = lib.orders_cancel(market, id)

            self.assertIn('status', result_cancel)
            self.assertTrue(result_cancel['status'] == 'error')
            self.assertIn('time', result_cancel)
            self.assertIn('message', result_cancel)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Cancel invalid order market """
    def test_user_orders_cancel_invalid_market(self):
        async def run_test():
            market = 'invalid'
            id = '123'

            lib = BitsgapClient(public_key, private_key)

            result_cancel = lib.orders_cancel(market, id)

            self.assertIn('status', result_cancel)
            self.assertTrue(result_cancel['status'] == 'error')
            self.assertIn('time', result_cancel)
            self.assertIn('message', result_cancel)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

