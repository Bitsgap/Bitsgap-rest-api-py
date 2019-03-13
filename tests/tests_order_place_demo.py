import asyncio
import logging
from unittest import TestCase
from rest.client import BitsgapClient
from rest.tests.keys import public_key,private_key


class TestRestOrderPlaceDemo(TestCase):

    """ Place order and check responses
        Valid data
    """
    def test_order_place_demo_valid_data(self):
        async def run_test():

            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0.250'
            amount = '150'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'ok')
            self.assertIn('data', result)

            data = result['data'] if 'data' in result else None

            self.assertIsNotNone(data)

            self.assertIn('id', data)
            self.assertIn('price', data)
            self.assertIn('amount', data)
            self.assertIn('pair', data)
            self.assertIn('side', data)
            self.assertIn('type', data)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Place order and check responses
        Invalid market name
    """
    def test_order_place_demo_invalid_market(self):
        async def run_test():
            market = 'no_market'
            pair = 'EDR_USD'
            price = '0.250'
            amount = '150'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Place order and check responses
        Invalid pair name
    """
    def test_order_place_demo_invalid_pair(self):
        async def run_test():
            market = 'bittrex'
            pair = 'no_pair'
            price = '0.250'
            amount = '150'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Place order and check responses
        Invalid price format
    """
    def test_order_place_demo_invalid_price_format(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0m250'
            amount = '150'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Place order and check responses
        Invalid price value
    """
    def test_order_place_demo_invalid_price_value(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '250000000000'
            amount = '150'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Place order and check responses
        Invalid price zero
    """
    def test_order_place_demo_invalid_price_zero(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0'
            amount = '150'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Place order and check responses
        Invalid amount maximum
    """
    def test_order_place_demo_invalid_amount_maximum(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0.25'
            amount = '150000000'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Place order and check responses
        Invalid amount zero
    """
    def test_order_place_demo_invalid_amount_zero(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0.25'
            amount = '0'
            side = 'sell'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Place order and check responses
        Invalid side
    """
    def test_order_place_demo_invalid_side(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0.25'
            amount = '150'
            side = 'no_value'
            ord_type = 'limit'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()

    """ Place order and check responses
        Invalid type
    """
    def test_order_place_demo_invalid_type(self):
        async def run_test():
            market = 'bittrex'
            pair = 'EDR_USD'
            price = '0.25'
            amount = '150'
            side = 'sell'
            ord_type = 'no_value'

            lib = BitsgapClient(public_key, private_key)

            result = lib.demo_orders_add(market, pair, amount, price, side, ord_type)

            logging.debug(result)

            self.assertIsNotNone(result)

            self.assertTrue(result['status'] == 'error')
            self.assertIn('message', result)

            await asyncio.sleep(1)

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        coro = asyncio.coroutine(run_test)
        event_loop.run_until_complete(coro())
        event_loop.close()