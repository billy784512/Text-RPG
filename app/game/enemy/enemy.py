from app.game.skill import Bite
from ..role import Role

class Enemy(Role):
    def __init__(self, name):
        super().__init__(name, health=100, attack=10)
        bite = Bite()
        self.skills = [bite]

    def take_damage(self, value: int):
        damage = value - self.defense
        self.health -= damage
        self.damage = 0
        if self.health < 0:
            self.health = 0

