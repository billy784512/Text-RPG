import requests

def main():
    print("Welcome to the Text RPG!")
    # True for player, False for enemy
    turn = True

    while True:
        print("-----------------------------------------------")
        print("Take Action! \n [0] Check Self Status, [1] Fight")
        command = input("> ")

        if command == "1":
            action = "fight"+str(int(turn))
            response = requests.post("http://127.0.0.1:8000/command", json={"command": action})
            print(response.json()["response"])

            action2 = "status"
            response = requests.post("http://127.0.0.1:8000/command", json={"command": action2})
            print(response.json()["response"])
            
            turn = not turn

        elif command == "0":
            action = "self_status"
            response = requests.post("http://127.0.0.1:8000/command", json={"command": action})
            print(response.json()["response"])
        

if __name__ == "__main__":
    main()