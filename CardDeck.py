import random 

class CardDeck:
    faces = ["A", "2", "3", "4", "5",
             "6", "7", "8", "9", "10",
             "J", "Q", "K"]
    suit = ["Hearts", "Diamonds", "Spades", "Clubs"]




    def __init__(self):
        self.cards = []
        # HW: using the lists above geneate all the 52 cards 
        # and .append() it to self.cards

    
    def shuffle (self):
        """
        shuffles the self.card which contains all the cards
        """
        random.shuffle(self.cards)


    


