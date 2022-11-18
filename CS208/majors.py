from Classes_2 import KClass
from Student import Student
from Professor import Prof


class Major:
    def __init__(self, name, kClass):
        self.name = name
        self.kClass = kClass

    def __repr__(self):
        return f"{self.name}, {self.kClass}"
