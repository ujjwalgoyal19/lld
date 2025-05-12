from typing import List

from models.split import Split


class SplitValidator:
    """
    A class to validate the splits for a given transaction.
    """

    def validate(self, total_amount: float, splits: List[Split]) -> bool: ...
