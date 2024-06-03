import random
from .player import Player
from .enemy import Enemy
from .role import Role

class Combat:
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy

    def take_turn(self, role: Role, target: Role) -> str:
        skill = random.choice(role.skills)
        result = skill.use(role, target)

        if not target.is_alive():
            result += f"{target.name} is defeated!"

        return result
    
    def next_turn(self, turn: str):
        if turn == "player":
            return self.take_turn(self.player, self.enemy)
        elif turn == "enemy":
            return self.take_turn(self.enemy, self.player)
        else:
            return "Invalid arg in next_turn"
        
    def combat_status(self):
        return f"{self.player.name} HP: {self.player.health} \n{self.enemy.name} HP: {self.enemy.health}"


