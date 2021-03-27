import pygame

from Card import Card
from CardDeck import CardDeck

pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Poker Game")



deck = CardDeck()
deck.shuffle()

running = True 

clock = pygame.time.Clock()

bg = pygame.image.load("./assets/bg.jpeg")

# card = deck.cards.pop()

cardJS = Card("Hearts", "K")

while running:
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
                bg = pygame.transform.scale(bg, (event.w, event.h))
    screen.blit(bg, (0,0))


    cardJS.draw(screen, 10, 10)


    pygame.display.flip()

    clock.tick(60)
