from ast import List
from ssl import create_default_context
from typing import Dict
from venv import create

from enums import SpotSize
from models.spot import CompactSpot, MediumSpot, Spot


class SpotFactory:
    def __init__(self):
        pass

    def create_spot(self, floor_id: str, spot_size: SpotSize) -> Spot:
        if spot_size == SpotSize.COMPACT:
            return CompactSpot(floor_id=floor_id)
        elif spot_size == SpotSize.MEDIUM:
            return MediumSpot(floor_id=floor_id)
        elif spot_size == SpotSize.LARGE:
            return spot_size == SpotSize.LARGE
        else:
            raise ValueError("Wrong Spot Size")

    def bulk_create_spot(self, floor_id: str, spot_plan: Dict[SpotSize, int]):
        created_spots: List[Spot] = []
        for spot_to_create, total_spots_to_create in spot_plan:
            for i in range(total_spots_to_create):
                created_spots.append(
                    self.create_spot(floor_id=floor_id, spot_size=spot_to_create)
                )

        return created_spots
