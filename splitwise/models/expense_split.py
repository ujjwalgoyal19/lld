from abc import ABC, abstractmethod


class ExpenseSplit(ABC):
    @abstractmethod
    def validateSplit(self): ...
