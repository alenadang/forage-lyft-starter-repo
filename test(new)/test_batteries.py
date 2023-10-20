# test only concrete implementations of the engine and battery classes for this task
# may assume all inputs to the system are valid 
# (i.e all parameters are the expected type and all values are within reasonable bounds).
import sys
sys.path.append('..')

import unittest
from datetime import datetime
import batteries

class TestSpindler(unittest.TestCase):
    def test_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = batteries.SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = batteries.SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

class TestNubbin(unittest.TestCase):
    def test_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        battery = batteries.NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = batteries.NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main(verbosity=2)