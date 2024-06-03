class Game:
    def __init__(self):
        self.state = {
            "location": 0,
            "inventory": []
        }

    def process_command(self, command: str):
        if command == "look":
            return self.look()
        elif command == "north":
            return self.move_north()
        else:
            return "Unknown command."

    def look(self):
        if self.state["location"] == 0:
            return "You are at the starting point. Paths lead north."
        elif self.state["location"] <= 9:
            return f"You leave starting point {self.state["location"]} miles away."

    def move_north(self):
        if self.state["location"] <= 9:
            self.state["location"] += 1
            return "You moved north."
        else:
            return "You reach the goal !!"