import time
from abc import ABC, abstractmethod
from asyncio import queues
from collections import deque
from http import client
from queue import Queue
from typing import Deque, Dict


class RateLimiter(ABC):
    def __init__(self, max_requests: int, window_size: int):
        self.max_requests = max_requests
        self.window_size = window_size

    @abstractmethod
    def allow_requests(self, client_id: str):
        pass


class FixedWindowRateLimiter(RateLimiter):
    def __init__(self, max_requests: int, window_size: int):
        super().__init__(max_requests=max_requests, window_size=window_size)
        self._client_request_counts: Dict[str, int] = {}
        self._client_start_time: Dict[str, int] = {}

    def allow_requests(self, client_id):
        current_time = int(time.time())

        if client_id not in self._client_start_time:
            self._client_start_time[client_id] = current_time
            self._client_request_counts[client_id] = 0

        client_start_time = self._client_start_time[client_id]

        if current_time - client_start_time >= self.window_size:
            self._client_start_time[client_id] = current_time
            self._client_request_counts[client_id] = 1
        else:
            self._client_request_counts[client_id] += 1

        if self._client_request_counts[client_id] > self.max_requests:
            return False

        return True


class SlidingWindowRateLimiter(RateLimiter):
    def __init__(self, max_requests: int, window_size: int):
        super().__init__(max_requests=max_requests, window_size=window_size)
        self._request_timestamps: Dict[str, Queue[int]] = {}

    def allow_requests(self, client_id):
        current_time = int(time.time())
        if client_id not in self._request_timestamps:
            self._request_timestamps[client_id] = deque()

        timestamps: Deque[int] = self._request_timestamps[client_id]

        while timestamps and current_time - timestamps[0] >= self.window_size:
            timestamps.popleft()

        if len(timestamps) < self.max_requests:
            timestamps.append(current_time)
            return True

        return False
