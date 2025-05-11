import threading


class SingletonMeta(type):
    __instances = {}
    __lock = threading.Lock()

    def __call__(self, *args, **kwargs):
        if self not in self.__instances:
            with self.__lock:
                if self not in self.__instances:
                    instance = super().__call__(*args, **kwargs)
                    self.__instances[self] = instance

        return self.__instances[self]
