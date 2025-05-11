from threading import Lock

from atm.state.atm_state import ATMState


class ATMMachine:
    _instance = None
    _lock: Lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._current_state = ATMState()
                cls._instance._idle_state
                cls._instance._authenticate_card_state
                cls._instance._choose_operation_state
                cls._instance._withdraw_money_state
                cls._instance._withdrawing_money_state
                cls._instance._deposit_money_state
                cls._instance._depositing_money_state
                cls._instance._check_balance_state
                cls._instance._remove_card_state
                cls._instance._maintenance_state

            return cls._instance

    # TODO: Every morning bank can fill the ATM with some amount of money, so that it's usable
    # TODO: There is a possibility that it's already filled therefore we will only fill the atm to desirable amount
    def fill_money():
        pass
