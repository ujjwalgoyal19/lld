from snake_ladder.jump import Jump


class Cell:
    def __init__(self, position):
        self.__jump: Jump = None
        self.__position = position

    def set_jump(self, jump):
        self.__jump = jump

    def stay_or_jump(self):
        if self.__jump:
            return self.__jump.get_end()
        else return 
