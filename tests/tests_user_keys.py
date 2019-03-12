import asyncio
import logging
from unittest import TestCase

import time

from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestUserKeys(TestCase):

    """ Get user keys list with status """
    def test_user_keys_valid_data(self):
        async def run_test():

            lib = BitsgapClient(public_key, private_key)

            result = lib.keys()

            logging.debug(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)

            data = result['data']

            self.assertIsNotNone(data)

            self.assertTrue(len(data) > 0)

            market = list(data.keys())[0]

            market_data = data[market]

            self.assertIn('key', market_data)
            self.assertIn('status', market_data)
            self.assertIn('uts', market_data)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
