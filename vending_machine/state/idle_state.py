from vending_machine.state.state import State
from vending_machine.state.state_type import StateType


class IdleState(State):
    """Idle state of the vending machine."""

    def __init__(self):
        super().__init__(StateType.IDLE)
    
    
    def start_machine(self, vending_machine: ):
      
