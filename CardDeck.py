import random

from Card import Card


class CardDeck:

    faces = ["A", "2", "3", "4", "5",
             "6", "7", "8", "9", "10",
             "J", "Q", "K"]
    suit = ["Hearts", "Diamonds", "Spades", "Clubs"]




    def __init__(self):
        """
        constructor of CardDeck class
        """
        self.cards = []
        for face in CardDeck.faces:
            for suit in CardDeck.suits:
                self.cards.append(Card(suit, face))



    
    def shuffle (self):
        """
        shuffles the self.card which contains all the cards
        """
        random.shuffle(self.cards)


    


