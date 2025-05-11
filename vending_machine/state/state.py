from abc import ABC

from vending_machine.state.state_type import StateType


class State(ABC):
    _state: StateType

    def __init__(self, state: StateType):
        self._state = state

    def get_state(self) -> StateType:
        return self._state
