import pygame

from Game.assets.constans import CELL_SIZE


class Part:
    def __init__(self, x, y, color, sprite=None):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def get_coords(self):
        return self.x, self.y

