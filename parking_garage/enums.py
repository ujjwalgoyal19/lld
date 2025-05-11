from enum import Enum


class PaymentMethod(Enum):
    UPI, CASH, CARD = range(3)


class VehicleType(Enum):
    TWO_WHEELER, CAR, TRUCK = range(3)


class UserType(Enum):
    CUSTOMER, ADMIN = range(2)


class SpotStatus(Enum):
    AVAILABLE, OCCUPIED, MAINTENANCE = range(3)


class SpotSize(Enum):
    COMPACT, MEDIUM, LARGE = range(3)


class TicketStatus(Enum):
    LOST, IN_PROGRESS, SETTLED = range(3)
