# Serviceable interface
class Serviceable:
    def needs_service(self):
        pass

# Battery interface
class Battery(Serviceable):
    def needs_service(self):
        pass

# Engine interface
class Engine(Serviceable):
    def needs_service(self):
        pass

