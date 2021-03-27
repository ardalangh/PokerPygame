import pygame

pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Poker Game")





running = True 

clock = pygame.time.Clock()

bg = pygame.image.load("./assets/bg.jpeg")


while running:
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
                bg = pygame.transform.scale(bg, (event.w, event.h))
    screen.blit(bg, (0,0))

    pygame.display.flip()

    clock.tick(60)
