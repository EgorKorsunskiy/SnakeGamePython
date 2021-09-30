import pygame

from ..assets.constans import CELL_SIZE, FRUIT_COLOR
from .utils import generate_random_coords


class Fruit:
    def __init__(self):
        self.x, self.y = generate_random_coords()

    def spawn(self, screen):
        pygame.draw.circle(
            screen, FRUIT_COLOR, (self.x * CELL_SIZE + CELL_SIZE/3, self.y * CELL_SIZE + CELL_SIZE/3), CELL_SIZE/3
        )

    def generate_new_coords(self):
        self.x, self.y = generate_random_coords()

    def get_coords(self):
        return self.x, self.y
