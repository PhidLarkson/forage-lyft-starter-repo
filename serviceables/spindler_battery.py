from interfaces.interface import *
from datetime  import date

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        # SpindlerBattery now needs service after three years
        self.service_interval = 3
        super().__init__(last_service_date, current_date)

    def needs_service(self) -> bool:
        # Calculate the difference in years between last_service_date and current_date
        years_since_last_service = self.current_date.year - self.last_service_date.year

        # Check if the difference is greater than or equal to the new service interval
        return years_since_last_service >= self.service_interval
