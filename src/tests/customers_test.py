import unittest

from src.customer import Customer


class CustomerTest(unittest.TestCase):

    def test_01_constructor(self):
        serialized = '{"latitude": "52.986375", ' \
                     '"user_id": 12, ' \
                     '"name": "Obama", ' \
                     '"longitude": "-6.043701"}'
        c = Customer(serialized)
        self.assertEqual(c.lat, 52.986375)
        self.assertEqual(c.lon, -6.043701)
        self.assertEqual(c.customer_id, 12)
        self.assertEqual(c.name, "Obama")

        c = Customer()
        self.assertIsNone(c.lat)
        self.assertIsNone(c.lon)
        self.assertIsNone(c.customer_id)
        self.assertIsNone(c.name)

    def test_02_toString(self):
        serialized = '{"latitude": "52.986375", ' \
                     '"user_id": 12, ' \
                     '"name": "Obama", ' \
                     '"longitude": "-6.043701"}'
        c = Customer(serialized)
        self.assertEqual(
            c.__str__(),
            '(id=12, name=Obama, lat=52.986375, lon=-6.043701)')

