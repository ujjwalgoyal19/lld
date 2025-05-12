from typing import List

from enums import SplitType
from models.split import Split
from models.split_validator.equal_split_validator import EqualSplitValidator
from models.split_validator.percentage_split_validator import PercentageSplitValidator
from models.split_validator.split_validator import SplitValidator
from models.split_validator.exact_split_validator import ExactSplitValidator


class SplitValidatorFactory:
    def build_split_validator(
        self,
        split_type: SplitType,
    ) -> SplitValidator:
        """
        Validate the split.
        """
        if split_type == SplitType.EQUAL:
            return EqualSplitValidator()
        elif split_type == SplitType.PERCENT:
            return PercentageSplitValidator()
        elif split_type == SplitType.EXACT:
            return ExactSplitValidator()
        else:
            raise ValueError("Invalid split type")
