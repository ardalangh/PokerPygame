
from CardDeck import CardDeck
from Table import Table


class Game:

    smallBlindAmount = 5   # $5
    bigBlindAmount = 10    # $10 This is the min bet

    def __init__(self, screen_size):
        self.round = 1
        self.screen_size = screen_size
        self.dealer = None
        self.bigBlind = None
        self.smallBlind = None

        self.players = []    # LIST OF ALL PLAYERS
        self.deck = CardDeck(screen_size)
        self.table = Table()

        self.show_flops = False
        self.flops = []




    def dealPreFlop(self):
        if len(self.players) <= 1:
            raise Exception("You need at least 2 player to be able to play")
        self.deck.shuffle()

        for r in range(2):
            for player in self.players:
                card = self.deck.cards.pop()
                card.belongs_to(player)
                player.cards.append(card)


    def dealFlop(self):
        [self.flops.append(self.deck.cards.pop()) for _ in range(3)]
        self.show_flops = True






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