from enum import Enum


class SplitType(Enum):
    """
    Enum for Splitwise split types.
    """

    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"
