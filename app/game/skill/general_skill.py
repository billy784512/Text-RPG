from .skill import Skill
from ..role import Role

class Defense(Skill):
    def __init__(self):
        self.name = "Defense"

    def use(self, user:Role, target:Role) -> str:
        val = (user.attack)//2
        user.defense += val
        return f"{user.name} =(Defense, value={val})=> {user.name}.\n"

    def desc(self):
        pass

class Heal(Skill):
    def __init__(self):
        self.name = "Heal"

    def use(self, user:Role, target:Role) -> str: 
        val = (user.attack)//3
        target.health += val
        return f"{user.name} =(Heal, value={val})=> {target.name}.\n"
    
    def desc(self):
        pass

class Bite(Skill):
    def __init__(self):
        self.name = "Bite"

    def use(self, user:Role, target:Role) -> str: 
        val = user.attack
        target.take_damage(val)
        return f"{user.name} =(Bite, value={val})=> {target.name}.\n"
    
    def desc(self):
        pass
