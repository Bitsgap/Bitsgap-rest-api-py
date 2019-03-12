import asyncio
import logging
from unittest import TestCase
from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestPlaceOrderDemo(TestCase):

    """ Get orderbook for selected market and pair """
    def test_orderbook_valid_data(self):
        async def run_test():

            market = 'bittrex'
            pair = 'EDR_USD'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orderbook(market, pair)

            logging.debug(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)

            data = result['data']

            self.assertIsNotNone(data)
            self.assertIn('asks',data)
            self.assertIn('bids',data)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Check invalid market error """
    def test_orderbook_invalid_market(self):
        async def run_test():

            market = 'no_market'
            pair = 'EDR_USD'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orderbook(market, pair)

            logging.debug(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Check invalid pair error """
    def test_orderbook_invalid_pair(self):
        async def run_test():

            market = 'bittrex'
            pair = 'no_pair'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orderbook(market, pair)

            logging.debug(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
