class Table:
    def __init__(self):
        self.cards = []
        self.preFlop = [None] * 3
        self.flop = None
        self.turn = None


    def checkTableCards(self):
        if len(self.cards) > 5:
            raise RuntimeError("Table has 5 cards")

    def setsPreFlop(self, preFlopCards):
        if len(preFlopCards) != 3:
            raise RuntimeError("PreFlop must have 3 cards")
        self.preFlop = preFlopCards
