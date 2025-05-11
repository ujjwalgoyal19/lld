from enum import Enum


class StateType(Enum):
    """State types for the vending machine."""

    IDLE = "IDLE"
    COLLECTING = "COLLECTING"
    SELECTING = "SELECTING"
    DISPENSING = "DISPENSING"
    CLOSING = "CLOSING"
    MAINTENANCE = "MAINTENANCE"

    def __str__(self):
        return self.value
