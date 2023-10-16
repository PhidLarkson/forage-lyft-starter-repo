from interfaces.interface import *

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        # SternmanEngine needs service only when the warning indicator is on
        return self.warning_light_on