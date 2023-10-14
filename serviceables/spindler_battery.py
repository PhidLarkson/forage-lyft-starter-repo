from datetime import date
from interfaces.interface import *

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # Simplified logic for demonstration
        return (self.current_date - self.last_service_date).days >= 365  # Check if one year has passed
