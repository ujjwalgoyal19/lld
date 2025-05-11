from enums import VehicleType
from models.vehicle import Car, Truck, TwoWheeler


class VehicleFactory:
    def __init__(self):
        pass

    def create_vehicle(self, vehicle_type: VehicleType, number_plate: str):
        if vehicle_type == VehicleType.CAR:
            return Car(number_plate=number_plate)
        elif vehicle_type == VehicleType.TWO_WHEELER:
            return TwoWheeler(number_plate=number_plate)
        elif vehicle_type == VehicleType.TRUCK:
            return Truck(number_plate=number_plate)
        else:
            raise ValueError("Wrong Vehicle Type")
