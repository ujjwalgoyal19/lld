from typing import List

from models.split import Split
from models.split_validator.split_validator import SplitValidator


class ExactSplitValidator(SplitValidator):
    """
    This class validates if the split is unequal.
    """

    def validate(self, total_amount: float, splits: List[Split]) -> bool:
        total_split_amount = 0
        for split in splits:
            total_split_amount += split.amount
        if total_split_amount != total_amount:
            return False
        return True
