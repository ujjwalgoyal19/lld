import datetime
import string
import uuid

from enums import TicketStatus
from models import payment
from models.spot import Spot
from models.user import User
from models.vehicle import Vehicle


class Ticket:
    def __init__(self, user: User, vehicle: Vehicle, spot: Spot):
        self.ticket_id = string(uuid())
        self.user = user
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.datetime.now()
        self.exit_time = None
        self.status = TicketStatus.IN_PROGRESS
        self.payment = None

    def make_payment(self, payment_details):
        self.payment = payment
        self.status = TicketStatus.SETTLED
        self.exit_time = datetime.datetime.now()
