import unittest
import parts.tires as tires

class TestCarrigan(unittest.TestCase):
    def test_needs_service(self):
        tire = tires.CarriganTires([0.9, 0.5, 0.8, 0.95])
        self.assertTrue(tire.needs_service())

    def test_does_not_need_service(self):
        tire = tires.CarriganTires([0.1, 0.5, 0.8, 0.89])
        self.assertFalse(tire.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_needs_service(self):
        # sum of this is 3.0
        tire = tires.OctoprimeTires([0.9, 0.6, 0.8, 0.7])
        self.assertTrue(tire.needs_service())

    def test_does_not_need_service(self):
        # sum of this is 2.9
        tire = tires.OctoprimeTires([0.9, 0.5, 0.8, 0.7])
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main(verbosity=2)