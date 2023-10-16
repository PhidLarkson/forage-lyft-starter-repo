import unittest
from datetime import date

# Import the classes we want to test
from car_factory import CarFactory
from car import Car
from serviceables.capulet_engine import CapuletEngine
from serviceables.willoughby_engine import WilloughbyEngine
from serviceables.sternman_engine import SternmanEngine
from serviceables.spindler_battery import SpindlerBattery
from serviceables.nubbin_battery import NubbinBattery

class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        factory = CarFactory()
        car = factory.create_calliope(date(2023, 10, 1), date(2022, 5, 15), 15000, 12000)
        self.assertIsInstance(car, Car)
        self.assertTrue(car.needs_service())

    def test_create_glissade(self):
        factory = CarFactory()
        car = factory.create_glissade(date(2023, 10, 1), date(2022, 5, 15), 15000, 12000)
        self.assertIsInstance(car, Car)
        self.assertTrue(car.needs_service())

    def test_create_palindrome(self):
        factory = CarFactory()
        car = factory.create_palindrome(date(2023, 10, 1), date(2022, 5, 15), True)
        self.assertIsInstance(car, Car)
        self.assertTrue(car.needs_service())

    def test_create_rorschach(self):
        factory = CarFactory()
        car = factory.create_rorschach(date(2023, 10, 1), date(2022, 5, 15), 15000, 12000)
        self.assertIsInstance(car, Car)
        self.assertTrue(car.needs_service())

    def test_create_thovex(self):
        factory = CarFactory()
        car = factory.create_thovex(date(2023, 10, 1), date(2022, 5, 15), 15000, 12000)
        self.assertIsInstance(car, Car)
        self.assertTrue(car.needs_service())

class TestEngine(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        engine = CapuletEngine(10000, 40000)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_needs_service(self):
        engine = WilloughbyEngine(5000, 62000)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

class TestBattery(unittest.TestCase):
    def test_spindler_battery_needs_service(self):
        battery = SpindlerBattery(date(2022, 5, 15), date(2023, 10, 1))
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_needs_service(self):
        battery = NubbinBattery(date(2019, 5, 15), date(2023, 10, 1))
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
