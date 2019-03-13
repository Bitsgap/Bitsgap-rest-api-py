import asyncio
import logging
from unittest import TestCase
from rest.client import BitsgapClient
from rest.tests.keys import public_key,private_key


class TestRestPlaceOrderDemo(TestCase):

    def test_place_order_and_move_valid_data(self):
        async def run_test():

            market = 'bittrex'
            pair = 'EDR_USD'

            lib = BitsgapClient(public_key, private_key)

            pl = lib.orders_add(market, pair, '150', '0.250', 'sell', 'limit')

            logging.debug(pl)

            self.assertTrue(pl['status'] == 'ok')
            self.assertIn('data', pl)

            data = pl['data'] if 'data' in pl else None
            id = data['id'] if 'id' in data else None

            self.assertIsNotNone(id)

            mv = lib.orders_move(market, id, '0.2')

            logging.debug(mv)

            self.assertTrue(mv['status'] == 'ok')
            self.assertIn('data', mv)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """
        Get open orders list and move first of it 
    """
    def test_move_open_order_valid_data(self):
        async def run_test():

            market = 'bittrex'

            lib = BitsgapClient(public_key, private_key)

            result = lib.orders_open(market)

            logging.debug(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)

            data = result['data'] if 'data' in result else None
            id = data['id'] if 'id' in data else None

            self.assertIsNotNone(id)

            mv = lib.orders_move(market, id, '0.2')

            logging.debug(mv)

            self.assertTrue(mv['status'] == 'ok')
            self.assertIn('data', mv)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()
