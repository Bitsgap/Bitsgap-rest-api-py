import asyncio
import logging
from unittest import TestCase
from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestUserDemoOrdersMove(TestCase):

    """ Move order """
    def test_user_demo_orders_move_valid_data(self):
        async def run_test():

            market = 'okex'

            lib = BitsgapClient(public_key, private_key)

            # get open orders
            result = lib.demo_orders_open(market)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'ok')
            self.assertIn('time', result)

            self.assertIn('data', result)
            data = result['data']

            self.assertIsNotNone(data)
            self.assertTrue(len(data) > 0)
            self.assertIn('id', data[0])

            id = data[0]['id']
            self.assertIsNotNone(id)

            old_price = data[0]['price']
            self.assertIsNotNone(old_price)
            new_price = float(old_price) * 0.999

            result_move = lib.demo_orders_move(market, id, str(new_price))

            self.assertIn('status', result_move)
            self.assertTrue(result_move['status'] == 'ok')
            self.assertIn('data', result_move)
            self.assertIn('time', result_move)

            data = result_move['data']

            self.assertIsNotNone(data)

            self.assertIn('price', data)
            self.assertIn('pair', data)
            self.assertIn('state', data)
            self.assertIn('side', data)
            self.assertIn('uts', data)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Move executed order """
    def test_user_demo_orders_move_invalid_executed_order(self):
        async def run_test():

            market = 'okex'

            lib = BitsgapClient(public_key, private_key)

            # get executed orders
            result = lib.demo_orders_history(market)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'ok')
            self.assertIn('time', result)

            self.assertIn('data', result)
            data = result['data']

            self.assertIsNotNone(data)
            self.assertTrue(len(data) > 0)
            self.assertIn('id', data[0])

            id = data[0]['id']
            self.assertIsNotNone(id)

            old_price = data[0]['price']
            self.assertIsNotNone(old_price)
            new_price = float(old_price) * 0.999

            result_move = lib.demo_orders_move(market, id, str(new_price))

            self.assertIn('status', result_move)
            self.assertTrue(result_move['status'] == 'error')
            self.assertIn('message', result_move)
            self.assertIn('time', result_move)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid order id """
    def test_user_demo_orders_move_invalid_id(self):
        async def run_test():

            market = 'okex'

            lib = BitsgapClient(public_key, private_key)

            id = 'invalid'
            new_price = '0.01'

            result_move = lib.demo_orders_move(market, id, new_price)

            self.assertIn('status', result_move)
            self.assertTrue(result_move['status'] == 'error')
            self.assertIn('message', result_move)
            self.assertIn('time', result_move)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid market"""
    def test_user_orders_move_invalid_market(self):
        async def run_test():

            market = 'invalid'

            lib = BitsgapClient(public_key, private_key)

            id = 'invalid'
            new_price = '0.01'

            result_move = lib.demo_orders_move(market, id, new_price)

            self.assertIn('status', result_move)
            self.assertTrue(result_move['status'] == 'error')
            self.assertIn('message', result_move)
            self.assertIn('time', result_move)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()