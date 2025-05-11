from abc import ABC

from enums import VehicleType


class Vehicle(ABC):
    def __init__(self, number_plate: str, type: VehicleType):
        self.__number_plate = number_plate
        self.__type = type

    @property
    def number_plate(self):
        return self.__number_plate

    @property
    def type(self):
        return self.__type


class TwoWheeler(Vehicle):
    def __init__(self, number_plate: str):
        super().__init__(number_plate=number_plate, type=VehicleType.TWO_WHEELER)


class Car(Vehicle):
    def __init__(self, number_plate: str):
        super().__init__(number_plate=number_plate, type=VehicleType.CAR)


class Truck(Vehicle):
    def __init__(self, number_plate: str):
        super().__init__(number_plate=number_plate, type=VehicleType.TRUCK)
