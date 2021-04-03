class Game:

    def __init__(self, players, deck):
        self.players = players
        self.deck = deck

    def deal(self):
        self.deck.shuffle()
        for r in range(2):
            for player in self.players:
                player.cards.append(self.deck.cards.pop())
