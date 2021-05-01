import pygame
from screeninfo import get_monitors

from Card import Card
from CardDeck import CardDeck
from Game import Game
from Player import Player

pygame.init()

# size = get_monitors()[0].width, get_monitors()[0].height
size = (1000, 800)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Poker Game")
running = True
clock = pygame.time.Clock()
# bg = pygame.image.load("./assets/bg.jpeg")

# making an instance of deck (52 cards in there)
deck = CardDeck()
deck.shuffle()


user_name = "ardy"
user_age = 22
# user_name = input("\t > Please enter your name: ")
# user_age = int(input("\t > Please enter your age: "))

if user_age < 21:
    print(f"You can NOT play. You must wait {21 - user_age} years to be able to play")
    exit()

game = Game()
user = Player(user_name, user_age, 2000)
dummyPlayer1 = Player("dummy1", 0, 2000)
dummyPlayer2 = Player("dummy2", 0, 2000)
game.players.append(user)
game.players.append(dummyPlayer1)
game.players.append(dummyPlayer2)

user.assignPosOnScreen(2)
dummyPlayer1.assignPosOnScreen(1)
dummyPlayer2.assignPosOnScreen(3)

game.dealPreFlop(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.VIDEORESIZE:
        #     screen = pygame.display.set_mode((event.w, event.h))
        #     bg = pygame.transform.scale(bg, (event.w, event.h))
    # screen.blit(bg, (0, 0))
    
    # user.drawIcon(screen, size)
    # dummyPlayer1.drawIcon(screen, size)
    # dummyPlayer2.drawIcon(screen, size)

    
    pygame.display.flip()

    clock.tick(60)
