import json, os

USERS_FILE = "data/users.json"
GAMES_FILE = "data/games.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def load_games():
    if not os.path.exists(GAMES_FILE):
        return []
    with open(GAMES_FILE, "r") as f:
        return json.load(f)

def save_games(games):
    with open(GAMES_FILE, "w") as f:
        json.dump(games, f, indent=4)
