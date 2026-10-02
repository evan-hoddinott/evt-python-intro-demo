"""Run from this folder: python -m unittest -v"""

import unittest

from speed import to_kmh


class SpeedTests(unittest.TestCase):
    def test_stopped(self):
        self.assertAlmostEqual(to_kmh(0), 0)

    def test_ten_metres_per_second(self):
        self.assertAlmostEqual(to_kmh(10), 36)

    def test_five_metres_per_second(self):
        self.assertAlmostEqual(to_kmh(5), 18)

    # During class, add a test here for 2.5 m/s -> 9 km/h.
