import asyncio
import logging
from unittest import TestCase
from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestUserBalance(TestCase):

    """ Get user balance """
    def test_user_balance_valid_data(self):
        async def run_test():

            lib = BitsgapClient(public_key, private_key)

            result = lib.balance()

            logging.debug(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)

            data = result['data']

            self.assertIsNotNone(data)

            self.assertTrue(len(data) > 0)

            # get market name
            market = list(data.keys())[0]
            # get information for market from response
            market_data = data[market]
            # check fields
            self.assertIn('balance', market_data)
            self.assertIn('total', market_data)
            self.assertIn('uts', market_data)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Get user balance for market """
    def test_user_balance_market_valid_data(self):
        async def run_test():

            lib = BitsgapClient(public_key, private_key)

            result = lib.market_balance('bittrex')

            logging.debug(result)

            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'ok')
            self.assertIn('time', result)
            self.assertIn('data', result)

            data = result['data']

            self.assertIsNotNone(data)

            self.assertTrue(len(data) > 0)

            # check fields
            self.assertIn('available', data)
            self.assertIn('total', data)
            self.assertIn('uts', data)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Get user balance for market
        Invalid market 
    """
    def test_user_balance_market_invalid_market(self):
        async def run_test():

            lib = BitsgapClient(public_key, private_key)

            result = lib.market_balance('invalid')

            logging.debug(result)

            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')
            self.assertIn('time', result)
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Get user balance for market
        API key disabled 
    """
    def test_user_balance_market_api_key_disabled_or_empty(self):
        async def run_test():

            lib = BitsgapClient(public_key, private_key)

            result = lib.market_balance('kraken')

            logging.debug(result)

            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'error')
            self.assertIn('time', result)
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
