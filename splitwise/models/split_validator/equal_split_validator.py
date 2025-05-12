from typing import List

from models.split import Split
from models.split_validator.split_validator import SplitValidator


class EqualSplitValidator(SplitValidator):
    """
    Validator for equal splits.
    """

    def validate(self, total_amount: float, splits: List[Split]) -> bool:
        """
        Validate the split.
        """
        for split in splits:
            if split.amount != total_amount / len(splits):
                return False
        return True
