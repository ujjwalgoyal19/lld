import string
import uuid

from models.ticket import Ticket
from models.user import User
from models.vehicle import Vehicle
from parking_lot import ParkingLot


class Entry:
    def __init__(self, parking_lot: ParkingLot):
        self.entry_id = string(uuid())
        self.__parking_lot = parking_lot

    def assign_parking_spot(self, vehicle: Vehicle):
        # Iterate over floors and spots to find an available spot for the vehicle
        for floor in self.__parking_lot.floors:
            for spot in floor.spots:
                if spot.is_available() and spot.can_fit_vehicle(vehicle):
                    spot.park_vehicle(vehicle)
                    return spot
        return None

    def get_ticket(self, user: User, vehicle: Vehicle) -> Ticket:
        spot = self.assign_parking_spot(vehicle)
        if not spot:
            raise Exception("No available parking spot for this vehicle type.")
        ticket = Ticket(user=user, vehicle=vehicle, spot=spot, entry_id=self.entry_id)
        spot.assign_ticket(ticket)
        return ticket
