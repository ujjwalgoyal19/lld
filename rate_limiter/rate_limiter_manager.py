from rate_limiter import RateLimiter
from rate_limiter_factory import RateLimiterFactory
from singleton import SingletonMeta


class RateLimiterManager(metaclass=SingletonMeta):
    _rate_limiter: RateLimiter

    def __init__(self):
        self._rate_limiter = RateLimiterFactory.createRateLimiter(
            type="sliding", max_requests=100, window_size=60000
        )

    def is_allowed(self, client_id):
        self._rate_limiter.allow_requests(client_id=client_id)


# TODO : Here we can also have a different Rate Limiter configuration which can use observer pattern and that way we can dynamically change rate limiters max_requests and window_size for every limiter that has been instantiated!!
