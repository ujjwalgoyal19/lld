from threading import Lock

from vending_machine.state.state import State


class VendingMachine:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._state = State()
                cls.
                    
            return cls._instance
