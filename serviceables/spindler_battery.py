from interfaces.interface import *
from datetime  import date

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        # SpindlerBattery needs service once every 2 years
        self.service_interval = 2
        super().__init__(last_service_date, current_date)
