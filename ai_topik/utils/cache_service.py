import time
from typing import Any, Optional

class SimpleCacheService:
    def __init__(self, ttl: int = 3600):
        self.ttl = ttl
        self.cache = {}

    def get(self, key: str) -> Optional[Any]:
        entry = self.cache.get(key)
        if entry:
            value, expire = entry
            if expire > time.time():
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key: str, value: Any):
        expire = time.time() + self.ttl
        self.cache[key] = (value, expire)