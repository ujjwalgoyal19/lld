from typing import Dict
from atm.currency.note import Note


class ATMCashStoreConfiguration:
    __note_configuration: Dict[Note, int]

    def __init__(self, note_configuration):
        self.__note_configuration = note_configuration


class ATMCashStore:
    _total_amount: int
    _note_count: Dict[Note, int]
    __configuration: ATMCashStoreConfiguration


    def __init__(self):
        



