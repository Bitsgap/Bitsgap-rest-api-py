import asyncio
import logging
from unittest import TestCase
from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestRecentTrades(TestCase):

    """ Get recent trades for selected market and pair """
    def test_recent_trades_valid_data(self):
        async def run_test():

            market = 'okex'
            pair = 'ETH_BTC'

            lib = BitsgapClient(public_key, private_key)

            result = lib.recent_trades(market, pair)

            logging.debug(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)


            data = result['data']
            self.assertIsNotNone(data)
            self.assertTrue(len(data) > 0)

            # check time field
            self.assertIn('u', data[0])
            # check amount field
            self.assertIn('am', data[0])
            # check side field
            self.assertIn('s', data[0])
            # check price field
            self.assertIn('p', data[0])

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid market  """

    def test_recent_trades_invalid_market(self):
        async def run_test():
            market = 'no_market'
            pair = 'ETH_BTC'

            lib = BitsgapClient(public_key, private_key)

            result = lib.recent_trades(market, pair)

            logging.debug(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Invalid pair """

    def test_recent_trades_invalid_pair(self):
        async def run_test():
            market = 'okex'
            pair = 'no_pair'

            lib = BitsgapClient(public_key, private_key)

            result = lib.recent_trades(market, pair)

            logging.debug(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
