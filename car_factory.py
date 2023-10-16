from interfaces.interface import *
from serviceables.capulet_engine import *
from serviceables.nubbin_battery import *
from serviceables.spindler_battery import *
from serviceables.sternman_engine import *
from serviceables.willoughby_engine import *
from serviceables.optoprime_tires import *
from serviceables.carrigan_tires import *
from car import *
from datetime import date

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        # Create a car with appropriate engine, battery, and tire types
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear) if any(wear >= 0.9 for wear in tire_wear) else OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)

    
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        # Create a car with appropriate engine, battery, and tire types
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear) if any(wear >= 0.9 for wear in tire_wear) else OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)


    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        # Create a car with appropriate engine, battery, and tire types
        engine = SternmanEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear) if any(wear >= 0.9 for wear in tire_wear) else OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)\
        
  
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        # Create a car with appropriate engine, battery, and tire types
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear) if any(wear >= 0.9 for wear in tire_wear) else OctoprimeTires(tire_wear)
        return Car(engine, battery, tires) 

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        # Create a car with appropriate engine, battery, and tire types
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear) if any(wear >= 0.9 for wear in tire_wear) else OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)
    
#former_format

    # @staticmethod
    # def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    #     # Create a Thovex car with an appropriate engine and battery
    #     engine = CapuletEngine(last_service_mileage, current_mileage)
    #     battery = NubbinBattery(last_service_date, current_date)
    #     return Car(engine, battery)
