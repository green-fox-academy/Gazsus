class Human:
    def __init__(self, name):
        self.__name = name
        self.__alive = True

    def get_name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return self.__name + (' status: alive ' if self.__alive else ' status: deceased ')

    def kill(self):
        self.__alive = False