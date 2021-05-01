import pygame


class Card:
    def __init__(self, suit, face):
        self.suit = suit 
        self.face = face
        self.filePath = f"./assets/cards/{self.face}{self.suit[0].upper()}.jpg"
        self.size = (None , None) # width : 0 height : 1
        # print(self.filePath)


    def draw(self, screen, x , y, angle):
        card = pygame.image.load(self.filePath)
        card = pygame.transform.scale(card, (140, 180))
        card = pygame.transform.rotate(card, angle)

        screen.blit(card, [x, y])
        return self

