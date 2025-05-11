from enum import Enum


class DownloadState(Enum):
    READY, DOWNLOADING, PAUSED, COMPLETED, FAILED = range(6)
