from interfaces.interface import *
from datetime import date

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        # NubbinBattery needs service once every 4 years
        self.service_interval = 4
        super().__init__(last_service_date, current_date)