import pygame
from screeninfo import get_monitors

from Card import Card
from CardDeck import CardDeck
from Player import Player

pygame.init()

size = get_monitors()[0].height, get_monitors()[0].width

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Poker Game")
running = True
clock = pygame.time.Clock()
bg = pygame.image.load("./assets/bg.jpeg")

# making an instance of deck (52 cards in there)
deck = CardDeck()
deck.shuffle()


user_name = input("/t>Please enter your name: ")
user_age = input("/t>Please enter your age: ")

if user_age < 21:
    print(f"You can NOT play. You must wait {21 - user_age} years to be able to play")
    exit()


user = Player(user_name, user_age)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            bg = pygame.transform.scale(bg, (event.w, event.h))
    screen.blit(bg, (0, 0))

    pygame.display.flip()

    clock.tick(60)
