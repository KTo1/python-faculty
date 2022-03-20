from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_volume(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self._size = size

    @property
    def fabric_volume(self):
        return round(self._size/6.5 + 0.5, 2)


class Costume(Clothes):

    def __init__(self, growth):
        self._growth = growth

    @property
    def fabric_volume(self):
        return round(2 * self._growth + 0.3, 2)


coat = Coat(20)
costume = Costume(170)

print(coat.fabric_volume)
print(costume.fabric_volume)

