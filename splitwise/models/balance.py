class Balance:
    def __init__(self):
        self.__amount_owe = 0
        self.__amount_get_back = 0

    def set_amount_owe(self, amount_owe):
        self.__amount_owe = amount_owe

    def set_amount_get_back(self, amount_get_back):
        self.__amount_get_back = amount_get_back

    def get_amount_owe(self):
        return self.__amount_owe

    def get_amount_get_back(self):
        return self.__amount_get_back
