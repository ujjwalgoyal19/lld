from multiprocessing import Value

from enums import TicketStatus
from models.spot import Spot
from models.ticket import Ticket
from parking_lot import ParkingLot


class Exit:
    def __init__(self, parking_lot: ParkingLot):
        self.parking_lot = parking_lot

    def process_exit(self, ticket: Ticket, payment=None):
        if ticket.status == TicketStatus.SETTLED:
            if payment:
                ticket.make_payment(payment)
            else:
                raise ValueError("Payment required to exit")

        spot: Spot = ticket.spot
        spot.un_park_vehicle()
        return True
