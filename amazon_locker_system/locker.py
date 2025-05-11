import uuid
from abc import ABC

from enums import LockerSize, LockerStatus
from location import Location


class Locker(ABC):
    def __init__(self, location: Location, size: LockerSize):
        self.locker_id = str(uuid.uuid4())
        self.location = location
        self.size = size
        self.status: LockerStatus = LockerStatus.AVAILABLE


class SmallLocker(Locker):
    def __init__(self, location: Location):
        super().__init__(self, location=location, size=LockerSize.SMALL)


class MediumLocker(Locker):
    def __init__(self, location: Location):
        super().__init__(self, location=location, size=LockerSize.MEDIUM)


class LargeLocker(Locker):
    def __init__(self, location: Location):
        super().__init__(self, location=location, size=LockerSize.LARGE)
