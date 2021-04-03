class Player:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        self.cards = []

    def __str__(self):
        return f"{self.name} has ${self.money}"

    def checkCards(self):
        if len(self.cards) > 2:
            raise RuntimeError("Player has more than 2 cards")
