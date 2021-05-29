import pygame


class Button:
    WIDTH = 200
    HEIGHT = 100
    def __init__(self, x, y, message ,callback):
        self.x = x
        self.y = y
        self.message = message
        self.callback = callback
        self.button_rect = pygame.Rect(self.x, self.y, Button.WIDTH, Button.HEIGHT)
        self.button_rect.x -= Button.WIDTH / 2
        self.button_rect.y -= Button.HEIGHT / 2
        self.clicked = False

    def being_clicked(self, mousePos):
        return self.button_rect.collidepoint(mousePos)

    def draw(self, screen):
        # HW get the self.message and render it as file on top of your button
        pygame.draw.rect(screen, (255, 255, 255), self.button_rect)