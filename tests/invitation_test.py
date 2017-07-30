import types
import unittest

from src.invitation import find_nearby_customers

from src.customer import Customer


class InvitationTest(unittest.TestCase):

    def test_find_customers(self):

        base_lat = 53.3393
        base_lon = -6.2576841

        customers = [
            Customer(
                '{"latitude": "52.92893", "user_id": 1, "name": "Alice",'
                '"longitude": "-7.27699"}'),  # ~ 81km to base
            Customer(
                '{"latitude": "53.92893", "user_id": 2, "name": "John",'
                '"longitude": "-5.27699"}'),  # ~ 92km to base
            Customer(
                '{"latitude": "54.22312", "user_id": 3, "name": "Obama",'
                '"longitude": "-7.02099"}')  # ~ 110km to base
        ]

        nearby = find_nearby_customers(
            customers, base_lat, base_lon, distance=80*1000)

        self.assertTrue(isinstance(nearby, types.GeneratorType))
        self.assertEqual(len(list(nearby)), 0)

        nearby = list(find_nearby_customers(
            customers, base_lat, base_lon, distance=90*1000))
        self.assertEqual(len(nearby), 1)
        self.assertEqual(nearby[0].name, "Alice")

        nearby = list(find_nearby_customers(
            customers, base_lat, base_lon, distance=109*1000))
        self.assertEqual(len(nearby), 2)
        self.assertIn("Alice", [c.name for c in nearby])
        self.assertIn("John", [c.name for c in nearby])

        nearby = list(find_nearby_customers(
            customers, base_lat, base_lon, distance=111 * 1000))
        self.assertEqual(len(nearby), 3)
