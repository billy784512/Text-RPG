from abc import ABC, abstractmethod

class Role(ABC):

    def __init__(self, name:str, health: int, attack: int):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = 0
        self.skills = []

    @abstractmethod
    def take_damage(self, value):
        pass

    def is_alive(self):
        return self.health > 0