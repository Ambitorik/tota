from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, volume):
        self.volume = volume

    @abstractmethod
    def counting(self):
        pass


class Coat(Clothes):

    @property
    def counting(self):
        return round((self.volume / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def counting(self):
        return round((self.volume * 2) + 0.3)


coat = Coat(99)
suit = Suit(195)
print(coat.counting)
print(suit.counting)
