
from CardDeck import CardDeck
from Table import Table


class Game:

    smallBlindAmount = 5   # $5
    bigBlindAmount = 10    # $10 This is the min bet

    def __init__(self):
        self.round = 1
        self.dealer = None
        self.bigBlind = None
        self.smallBlind = None

        self.players = []    # LIST OF ALL PLAYERS
        self.deck = CardDeck()
        self.table = Table()


    def dealPreFlop(self, screen):
        if len(self.players) <= 1:
            raise Exception("You need at least 2 player to be able to play")
        self.deck.shuffle()

        for r in range(2):
            for player in self.players:
                x, y = player.assignCenter4drawCard((1000, 800))
                player.cards.append(self.deck.cards.pop().draw(screen, x, y, player.getAngleRot()))




    # def deal(self):
    #     if len(self.players <= 1):
    #         raise Exception("You need at least 2 player to be able to play")
    #
    #     self.deck.shuffle()  # shuffle the cards
    #
    #     # Give two cards to each players
    #     for r in range(2):
    #         for player in self.players:
    #             player.cards.append(self.deck.cards.pop())

        # bets()



        # self.table.setsPreFlop([self.deck.cards.pop() for i in range(3)])






    # def bets(self):


    def done(self):
        self.round += 1