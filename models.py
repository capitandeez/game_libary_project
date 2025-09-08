class User:
    def __init__(self, username, password, balance=50):
        self.username = username
        self.password = password
        self.balance = balance
        self.games = []

    def buy_game(self, game):
        if game.name in self.games:
            return "Already own this game"
        if self.balance < game.price:
            return "Not enough balance"
        self.balance -= game.price
        self.games.append(game.name)
        return f"Bought {game.name}"

    def remove_game(self, game_name):
        if game_name in self.games:
            self.games.remove(game_name)
            return f"{game_name} removed"
        return f"{game_name} not in library"

class Game:
    def __init__(self, name, tags, price):
        self.name = name
        self.tags = tags
        self.price = price
