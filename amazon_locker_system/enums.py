from enum import Enum


class PackageSize(Enum):
    SMALL, MEDIUM, LARGE = range(3)


class LockerSize(Enum):
    SMALL, MEDIUM, LARGE = range(3)


class PackageStatus(Enum):
    SHIPPED, IN_LOCKER, DELIVERED = range(3)


class LockerStatus(Enum):
    ASSIGNED, OUT_OF_SERVICE, AVAILABLE = range(3)
