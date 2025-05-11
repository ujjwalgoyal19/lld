import threading


class SingletonMeta(type):

    __instances = {}
    __lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            with cls.__lock:
                if cls not in cls.__instances:
                    instance = super().__call(*args, **kwargs)
                    cls.__instances[cls] = instance

        return cls.__instances[cls]
