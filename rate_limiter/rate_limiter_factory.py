from rate_limiter import FixedWindowRateLimiter, SlidingWindowRateLimiter


class RateLimiterFactory:
    def createRateLimiter(type: str, max_requests: int, window_size: int):
        if type == "fixed":
            return FixedWindowRateLimiter(
                max_requests=max_requests, window_size=window_size
            )
        elif type == "sliding":
            return SlidingWindowRateLimiter(
                max_requests=max_requests, window_size=window_size
            )
        else:
            raise ValueError("Unknown rate limiter")
