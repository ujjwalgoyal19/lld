from typing import List

from models.split import Split
from models.split_validator.split_validator import SplitValidator


class PercentageSplitValidator(SplitValidator):
    def validate(self, total_amount: float, splits: List[Split]) -> bool:
        total_percentage = 0
        for split in splits:
            total_percentage += split.percentage
        if total_percentage != 100:
            return False
        split_total_amount = 0

        for split in splits:
            split_total_amount += split.amount
        if split_total_amount != total_amount:
            return False
        return True
