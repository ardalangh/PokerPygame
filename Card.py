import pygame

from Player import Player



class Card:
    def __init__(self, suit, face, screen_size):
        self.screen_size = screen_size
        self.suit = suit
        self.face = face
        self.filePath = f"./assets/cards/{self.face}{self.suit[0].upper()}.jpg"
        self.size = (None, None)  # width : 0 height : 1
        self.player = None
        self.card_loaded = pygame.image.load(self.filePath)
        self.card_loaded = pygame.transform.scale(self.card_loaded, (140, 180))
        self.card_loaded_rotated = None
        self.x = None
        self.y = None

    # def draw(self, screen):
    #
    #
    #     screen.blit(card, [x, y])
    #     return self

    def belongs_to(self, player):
        self.player = player

    def rotate_card_in_respect_to_player_pos(self):
        """
        make sure that this function is called after the card belongs to a player
        """
        assert self.player != None
        if self.player.dir == 1:
            self.x = self.screen_size[0] - Player.MARGIN
            self.y = self.screen_size[1] / 2
            self.card_loaded_rotated = pygame.transform.rotate(self.card_loaded,-90.0)
        elif self.player.dir == 2:
            self.card_loaded_rotated = pygame.transform.rotate(self.card_loaded,0.0)
        elif self.player.dir == 3:
            self.card_loaded_rotated = pygame.transform.rotate(self.card_loaded, 90.0)




