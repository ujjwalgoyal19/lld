from abc import ABC, abstractmethod

from enums import SpotSize, SpotStatus, VehicleType
from models.vehicle import Vehicle


class Spot(ABC):
    def __init__(self, size: SpotSize, floor_id: str):
        self.__size = size
        self.__floor_id = floor_id
        self.__spot_status = SpotStatus.AVAILABLE
        self.parked_vehicle: Vehicle = None

    @property
    def spot_status(self):
        return self.__spot_status

    @property
    def size(self):
        return self.__size

    @property
    def floor_id(self):
        return self.__floor_id

    def is_available(self):
        return self.__spot_status == SpotStatus.AVAILABLE

    def set_spot_to_maintenance(self):
        if self.__spot_status == SpotStatus.OCCUPIED:
            raise ValueError(
                "Spot is already occupied, please first un park the vehicle"
            )
        self.__spot_status = SpotStatus.MAINTENANCE

    def set_spot_to_available(self):
        self.__spot_status = SpotStatus.AVAILABLE

    def set_spot_to_occupied(self):
        self.__spot_status = SpotStatus.OCCUPIED

    @abstractmethod
    def can_fit_vehicle(self, vehicle: Vehicle):
        pass

    def park_vehicle(self, vehicle):
        if not self.is_available():
            raise ValueError("Spot is not available")
        if not self.can_fit_vehicle(vehicle):
            raise ValueError(
                f"Vehicle type {vehicle.type} cannot fit spot size {self.size}"
            )

        self.set_spot_to_occupied()
        self.parked_vehicle = vehicle

    def un_park_vehicle(self):
        self.set_spot_to_available()
        self.parked_vehicle = None


class CompactSpot(Spot):
    def __init__(self, floor_id: str):
        super().__init__(size=SpotSize.COMPACT, floor_id=floor_id)

    def can_fit_vehicle(self, vehicle):
        if vehicle.type == VehicleType.TWO_WHEELER:
            return True
        else:
            return False


class MediumSpot(Spot):
    def __init__(self, floor_id: str):
        super().__init__(size=SpotSize.MEDIUM, floor_id=floor_id)

    def can_fit_vehicle(self, vehicle):
        if vehicle.type == VehicleType.TWO_WHEELER or vehicle.type == VehicleType.CAR:
            return True
        else:
            return False


class LargeSpot(Spot):
    def __init__(self, floor_id: str):
        super().__init__(size=SpotSize.LARGE, floor_id=floor_id)

    def can_fit_vehicle(self, vehicle):
        if (
            vehicle.type == VehicleType.TWO_WHEELER
            or vehicle.type == VehicleType.CAR
            or vehicle.type == VehicleType.TRUCK
        ):
            return True
        else:
            return False
