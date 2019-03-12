import asyncio
import logging
from unittest import TestCase
from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestMarkets(TestCase):

    """ Get markets and pairs list """
    def test_markets_valid_data(self):
        async def run_test():

            lib = BitsgapClient(public_key, private_key)

            result = lib.markets()

            logging.debug(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
