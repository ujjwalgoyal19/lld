from controllers.user_controller import UserController
from singleton import SingletonMeta


class SplitWise(meta=SingletonMeta):
    def __init__(self):
        self.__user_controller = UserController()

    def run(self):
        pass


if __name__ == "__main__":
    split_wise_instance = SplitWise()
    split_wise_instance.run()
