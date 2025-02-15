from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

car_us = us_factory.create_car("Dodge", "Challenger")
car_us.start_engine()

car_eu = eu_factory.create_car("Volkswagen", "Passat")
car_eu.start_engine()

moto_us = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
moto_us.start_engine()

moto_eu = eu_factory.create_motorcycle("BMW", "R1250")
moto_eu.start_engine()
