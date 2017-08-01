import unittest

from src.gcd import GCD


class GCDTest(unittest.TestCase):

    def test_constructor(self):
        g1 = GCD()
        g2 = GCD(r=50)
        self.assertEqual(g2.R, 50)
        self.assertEqual(g1.R, 6371000.0)

    def test_calc(self):
        g1 = GCD()
        g2 = GCD(r=50)

        self.assertEqual(
            g1.calc_distance(lat1=50, lon1=50, lat2=50, lon2=50), 0.0)
        self.assertEqual(
            g2.calc_distance(lat1=50, lon1=50, lat2=50, lon2=50), 0.0)

        self.assertEqual(
            g1.calc_distance(lat1=40, lon1=30, lat2=54, lon2=55),
            2430506.413)

        self.assertEqual(
            g2.calc_distance(lat1=40, lon1=30, lat2=54, lon2=55),
            19.075)

        # being compared to http://andrew.hedges.name/experiments/haversine/
        self.assertEqual(
            g1.calc_distance(lat1=38.898556, lon1=-77.037852,
                             lat2=38.897147, lon2=-77.043934),
            549.156)

    def test_distance_to(self):
        g = GCD()
        g.set_base(lat=38.898556, lon=-77.037852)

        self.assertEqual(g.distance_to(lat=38.897147, lon=-77.043934), 549.156)
        self.assertEqual(g.distance_to(lat=38.898556, lon=-77.037852), 0)

    def test_is_nearby(self):
        g = GCD()
        g.set_base(lat=38.898556, lon=-77.037852)

        self.assertFalse(
            g.is_nearby(lat=38.897147, lon=-77.043934, distance=549))

        self.assertTrue(
            g.is_nearby(lat=38.897147, lon=-77.043934, distance=549.156))
        self.assertTrue(
            g.is_nearby(lat=38.897147, lon=-77.043934, distance=550))
