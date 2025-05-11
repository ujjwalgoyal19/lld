class Expense:
    def __init__(self, description: str, total_amount: float, splits: any):
        self.__description = description
        self.__total_amount = total_amount
        self.__splits = splits
