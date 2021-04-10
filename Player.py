class Player:
    def __init__(self, name, age, money = 2000):
        self.name = name
        self.age = age
        self.money = money
        self.cards = []
        self.img

    def __str__(self):
        return f"{self.name} has ${self.money}"

    def checkCards(self):
        if len(self.cards) > 2:
            raise RuntimeError("Player has more than 2 cards")


    def getMoneyFrom(self, otherPlayer, quantity):
        if (otherPlayer.money < quantity):
            raise RuntimeError(f"{otherPlayer.__str__()} is {quantity - otherPlayer.money} short")
        self.money += quantity
        otherPlayer.money -= quantity

    def giveMoneyTo(self, otherPlayer, quantity):
        if (self.money < quantity):
            raise RuntimeError(f"{self.__str__()} is {quantity - self.money} short")
        otherPlayer.money += quantity
        self.money -= quantity




