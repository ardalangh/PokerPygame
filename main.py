import pygame

pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Poker Game")





running = True 

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type  == Pygame.QUIT:
            running = False
