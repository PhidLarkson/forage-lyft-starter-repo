from interfaces.interface import *

class Car:
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        # Check if either the engine or battery needs service
        engine_service = self.engine.needs_service()
        battery_service = self.battery.needs_service()
        return engine_service or battery_service
