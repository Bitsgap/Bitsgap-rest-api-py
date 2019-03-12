import asyncio
import logging
from unittest import TestCase

import time

from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestOhlc(TestCase):

    """ Get open-high-low-close prices and volumes for market and pair in selected interval"""
    def test_ohlc_valid_data(self):
        async def run_test():

            market = 'bittrex'
            pair = 'EDR_USD'
            start = int(time.time() - 3600)
            end = int(time.time())

            lib = BitsgapClient(public_key, private_key)

            result = lib.ohlc(market, pair, start, end)

            logging.debug(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)

            data = result['data']

            self.assertTrue(len(data)> 0)

            item = data[0]

            self.assertIn('open', item)
            self.assertIn('high', item)
            self.assertIn('low', item)
            self.assertIn('close', item)
            self.assertIn('time', item)
            self.assertIn('volume', item)

            volume = item['volume']

            self.assertIn('buy', volume)
            self.assertIn('sell', volume)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ 
        Invalid market
    """
    def test_ohlc_invalid_market(self):
        async def run_test():

            market = 'no_market'
            pair = 'EDR_USD'
            start = int(time.time() - 3600)
            end = int(time.time())

            lib = BitsgapClient(public_key, private_key)

            result = lib.ohlc(market, pair, start, end)

            logging.debug(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ 
        Invalid pair
    """
    def test_ohlc_invalid_pair(self):
        async def run_test():

            market = 'bittrex'
            pair = 'no_pair'
            start = int(time.time()) - 3600
            end = int(time.time())

            lib = BitsgapClient(public_key, private_key)

            result = lib.ohlc(market, pair, start, end)

            logging.debug(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ 
        Too big interval
    """
    def test_ohlc_too_big_interval(self):
        async def run_test():

            market = 'bittrex'
            pair = 'EDR_USD'
            start = int(time.time()) - 360000
            end = int(time.time())

            lib = BitsgapClient(public_key, private_key)

            result = lib.ohlc(market, pair, start, end)

            logging.debug(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ 
        Interval start > end
    """
    def test_ohlc_invalid_interval_seq(self):
        async def run_test():

            market = 'bittrex'
            pair = 'EDR_USD'
            start = int(time.time())
            end = int(time.time()) - 3600

            lib = BitsgapClient(public_key, private_key)

            result = lib.ohlc(market, pair, start, end)

            logging.debug(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
