import random


class Dice:

    def __init__(self, number_of_dices):
        self.__number_of_dices = number_of_dices
        self.__min_dice_face = 1
        self.__max_dice_face = 6

    def roll_dice(self):
        dice_rolls_total = 0
        for _ in range(self.__number_of_dices):
            dice_rolls_total += random.randint(
                self.__min_dice_face, self.__max_dice_face
            )

        return dice_rolls_total
