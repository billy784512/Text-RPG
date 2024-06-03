from .skill import Skill
from ..role import Role
import math

class Fireball(Skill):
    def __init__(self):
        self.name = "Fireball"

    def use(self, user:Role, target:Role) -> str:
        val = user.attack * 2
        target.take_damage(val)
        return f"{user.name} =(Fireball, damage={val})=> {target.name}\n"
    
    def desc(self):
        pass

class Blizzard(Skill):
    def __init__(self):
        self.name = "Blizzard"

    def use(self, user:Role, target:Role) -> str:
        val = math.floor(user.attack * 1.5)
        val2 = user.attack // 2.5
        target.take_damage(val)
        user.defense += val2
        return f"{user.name} =(Blizzard, damage={val}, def_incr={val2})=> {target.name}\n"
    
    def desc(self):
        pass
