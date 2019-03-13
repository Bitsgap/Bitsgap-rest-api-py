import asyncio
import logging
from unittest import TestCase
from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestUserDemoBalance(TestCase):

    """ Get user balance on demo markets """
    def test_user_demo_balance_valid_data(self):
        async def run_test():

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_balance()

            logging.debug(result)

            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)
            self.assertIn('time', result)

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

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
