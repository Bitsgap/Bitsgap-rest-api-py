import asyncio
import logging
from unittest import TestCase
from rest_api_py_lib import BitsgapClient
from tests.keys import public_key,private_key


class TestRestMessages(TestCase):

    """ Get user message list """
    def test_user_message_valid_data(self):
        async def run_test():

            lib = BitsgapClient(public_key, private_key)

            result = lib.messages()

            logging.debug(result)

            self.assertIn('status', result)
            self.assertTrue(result['status'] == 'ok')
            self.assertIn('time', result)

            self.assertIn('data', result)
            data = result['data']

            self.assertIsNotNone(data)
            self.assertTrue(len(data) > 0)

            message = data[0]

            self.assertIn('t', message)
            self.assertIn('type', message)
            self.assertIn('trade', message)
            self.assertIn('text', message)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
