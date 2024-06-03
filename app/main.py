from fastapi import FastAPI
from pydantic import BaseModel
from app.game import Game, Combat
from app.game.player import Player
from app.game.enemy import Enemy
from app.game.skill import Blizzard, Fireball, Heal, Defense

# Init Sever & Game
app = FastAPI()
game = Game()

# Init Role
player = Player(name="Tinanana")
enemy = Enemy(name="BGTW")

# Add Skills
fireball = Fireball()
defense = Defense()
player.add_skill(fireball)
player.add_skill(defense)

combat = Combat(player, enemy)

class Command(BaseModel):
    command: str
    
@app.post("/command")
def process_command(cmd: Command):
    command = cmd.command

    if command == "go":
        result = game.move_north()
    elif command == "look":
        result = game.look()
    elif command == "fight1":
        result = combat.next_turn("player")
    elif command == "fight0":
        result = combat.next_turn("enemy")
    elif command == "status":
        result = combat.combat_status()
    elif command == "self_status":
        result = player.status()
    else:
        result = command
    return {"response": result}


@app.get("/")
def root():
    return {"message": "Hello World"}