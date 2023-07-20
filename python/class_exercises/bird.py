from abc import ABC, abstractmethod


class Bird(ABC):
    fly = True
    babies = 0
    clutch_size = 1
    extinct = False

    def noise(self):
        return "Squalk"

    def reproduce(self):
        if not self.extinct:
            self.babies += self.clutch_size

    @abstractmethod
    def eat(self):
        pass


class Owl(Bird):
    clutch_size = 6

    def eat(self):
        return "Peck peck"

class Dodo(Bird):
    fly = False
    extinct = True

    def eat(self):
        return "Nom nom"