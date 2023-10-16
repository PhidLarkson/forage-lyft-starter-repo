from interfaces.interface import Tires

class CarriganTires(Tires):
    def needs_service(self) -> bool:
        return any(wear >= 0.9 for wear in self.tire_wear)