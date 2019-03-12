import asyncio
import logging
from unittest import TestCase

import time

from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestUserDemoOrdersOpen(TestCase):

    """ Get user demo open orders """
    def test_user_demo_open_orders_valid_data(self):
        async def run_test():

            market = 'bittrex'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_open(market)

            logging.debug(result)

            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'ok')
            self.assertIn('time', result)

            if 'message' in result:
                self.assertTrue(result['message'] == 'Data not found') # no open orders
            else:
                self.assertIn('data', result)
                data = result['data']
                self.assertTrue(len(data) > 0)
                # check fields
                self.assertIn('id', data[0])
                self.assertIn('price', data[0])
                self.assertIn('amount', data[0])
                self.assertIn('pair', data[0])
                self.assertIn('type', data[0])
                self.assertIn('side', data[0])
                self.assertIn('uts', data[0])

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid market name """
    def test_user_open_orders_invalid_market(self):
        async def run_test():

            market = 'invalid_market'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_open(market)

            logging.debug(result)

            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)
            self.assertIn('time', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
