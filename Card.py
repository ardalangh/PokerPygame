class Card:
    def __init__(self, suit, face):
        self.suit = suit 
        self.face = face
        self.filePath = f"/assets/cards/ {self.face} {self.suit[0].upper()}.jpg"

