from abc import ABC, abstractmethod

from enums import VehicleType


class CostCalculationStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, entry_time, exit_time, vehicle_type):
        pass


class HourlyRateStrategy(CostCalculationStrategy):
    def __init__(self):
        self.rates = {
            VehicleType.TWO_WHEELER: 20,
            VehicleType.CAR: 50,
            VehicleType.TWO_WHEELER: 100,
        }

    def calculate_cost(self, entry_time, exit_time, vehicle_type):
        duration = exit_time - entry_time

        hours = duration.total_seconds() / 3600
        hours = max(1, round(hours))
        return hours * self.rates[vehicle_type]
