import pygame

from Player import Player



class Card:
    MARGINBETWEENCARDS = 10
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


    """
        The function below are meant to be called in the order that they are displayed. 
        if you attempt to call it in any other order you will get unexpected behavior 
    """
    def belongs_to(self, player):
        self.player = player
        if player.dir != 2:
            self.filePath = f"./assets/cards/red_back.jpg"
            self.card_loaded = pygame.image.load(self.filePath)
            self.card_loaded = pygame.transform.scale(self.card_loaded, (140, 180))

    def rotate_card_in_respect_to_player_pos(self):

        assert self.player != None
        if self.player.dir == 1:
            self.x = self.screen_size[0] - Player.MARGIN - self.card_loaded.get_height()
            self.y = (self.screen_size[1] / 2 - self.card_loaded.get_width() / 2) +\
            ((self.player.cards.index(self)) * (self.card_loaded.get_width() + Card.MARGINBETWEENCARDS) -
             self.card_loaded.get_width() / 2)
            self.card_loaded_rotated = pygame.transform.rotate(self.card_loaded,-90.0)



        elif self.player.dir == 2:
            self.x = (self.screen_size[0] / 2 - self.card_loaded.get_width() / 2) +\
                     ((self.player.cards.index(self)) * (self.card_loaded.get_width() + Card.MARGINBETWEENCARDS) -
                      self.card_loaded.get_width()/2)
            self.y = self.screen_size[1] - Player.MARGIN - self.card_loaded.get_height()
            self.card_loaded_rotated = pygame.transform.rotate(self.card_loaded,0.0)

        elif self.player.dir == 3:
            self.x = Player.MARGIN
            self.y = (self.screen_size[1] / 2 - self.card_loaded.get_width() / 2) +\
            ((self.player.cards.index(self)) * (self.card_loaded.get_width() + Card.MARGINBETWEENCARDS) -
             self.card_loaded.get_width() / 2)
            self.card_loaded_rotated = pygame.transform.rotate(self.card_loaded, 90.0)

    def draw(self, screen):
        self.rotate_card_in_respect_to_player_pos()
        screen.blit(self.card_loaded_rotated, [self.x, self.y])
        return self


    def draw_middle_card(self,  screen, index):
        mid_pos = [(10,10), (40, 10), (70, 10)]
        screen.blit(self.card_loaded, mid_pos[index])




