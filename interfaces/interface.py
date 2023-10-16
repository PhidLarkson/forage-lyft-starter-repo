from abc import ABC, abstractmethod
from datetime import date

# Define the Serviceable interface
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Battery(Serviceable):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        # Calculate the difference in years between last_service_date and current_date
        years_since_last_service = self.current_date.year - self.last_service_date.year

        # Check if the difference is greater than or equal to the required service interval
        return years_since_last_service >= self.service_interval


# Define the Engine class
class Engine(Serviceable):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        # Calculate the mileage since the last service and check if it exceeds the service interval
        raise NotImplementedError("Subclasses must implement the 'needs_service' method.")
