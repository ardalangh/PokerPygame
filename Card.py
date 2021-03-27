import pygame


class Card:
    def __init__(self, suit, face):
        self.suit = suit 
        self.face = face
        self.filePath = f"./assets/cards/ {self.face} {self.suit[0].upper()}.jpg"
        self.size = (None , None) # width : 0 height : 1


    def draw(self, screen, x , y):
        card = pygame.image.load(self.filePath)
        screen.blit(card, [x, y])

