import random

from Card import Card


class CardDeck:
    faces = ["A", "2", "3", "4", "5",
             "6", "7", "8", "9", "10",
             "J", "Q", "K"]
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

    def __init__(self, screen_size):
        """
        constructor of CardDeck class
        """
        self.screen_size = screen_size
        self.cards = []
        for face in CardDeck.faces:
            for suit in CardDeck.suits:
                self.cards.append(Card(suit, face, screen_size))

    def shuffle(self):
        """
            :return shuffled self.cards
        """
        random.shuffle(self.cards)
