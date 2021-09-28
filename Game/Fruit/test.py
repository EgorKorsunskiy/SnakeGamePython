from fruit import Fruit
from utils import get_coords
import pygame

pygame.init()
run = True
screen = pygame.display.set_mode((720, 480))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        f = Fruit(get_coords(), pygame, screen)
        f.spawn()
        pygame.time.delay(200)
        pygame.display.update()
        pygame.time.delay(200)
        screen.fill((0, 0, 0))
        pygame.display.update()
        pygame.time.delay(200)

pygame.quit()