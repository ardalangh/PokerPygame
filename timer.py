

# import pygame
# import pygame.gfxdraw
# from screeninfo import get_monitors
#
# pygame.init()
#
# size = (1000, 500)
#
# screen = pygame.display.set_mode(size, pygame.RESIZABLE)
# pygame.display.set_caption("Poker Game")
#
# running = True
# clock = pygame.time.Clock()
#
#
# # pie(surface, x, y, r, start_angle, stop_angle, color)
#
#
# counter = 0
# steps = 18
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.VIDEORESIZE:
#             screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
#
#
#
#
#     screen.fill((255,255,255))
#
#     while counter != 20:
#         counter += 1
#         # find out about time .sleep in python
#         pygame.gfxdraw.pie(screen, size[0]//2,size[1]//2, 100, 0, counter * steps, (0,0,0))
#
#
#
#
#
#
#
#     pygame.display.flip()
#     clock.tick(60)