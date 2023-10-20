# test only concrete implementations of the engine and battery classes for this task
# may assume all inputs to the system are valid 
# (i.e all parameters are the expected type and all values are within reasonable bounds).

import sys
sys.path.append('..')

import unittest
from datetime import datetime
import engines

class TestCapulet(unittest.TestCase):
    def test_needs_service(self):
        last_service_mileage = 0
        current_mileage = 30001

        engine = engines.CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 10

        engine = engines.CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_needs_service(self):
        last_service_mileage = 0
        current_mileage = 60001

        engine = engines.WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 150

        engine = engines.WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_needs_service(self):
        engine = engines.SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        engine = engines.SternmanEngine(False)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main(verbosity=2)