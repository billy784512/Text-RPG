from ..role import Role
from app.game.skill import Skill

class Player(Role):
    def __init__(self, name):
        super().__init__(name, health=100, attack=10)
        self.skills = []
        #self.inventory = []
    
    def status(self):
        return f"name={self.name} \nHP={self.health}, \nATK={self.attack}, \nDEF={self.defense}, \nskills={[x.name for x in self.skills]}"

    def take_damage(self, value: int):
        damage = max(0, value - self.defense)
        self.health -= damage
        self.defense = 0
        if self.health < 0:
            self.health = 0

    def add_skill(self, skill:Skill):
        self.skills.append(skill)


    #def add_to_inventory(self, item):
        #self.inventory.append(item)
