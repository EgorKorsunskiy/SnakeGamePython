import time

import pygame

from .part import Part
from ..assets.constans import CELL_SIZE, SNAKE_COLOR


class Snake:
    def __init__(self, sprite=None, start_position=(9, 9)):
        self.color = SNAKE_COLOR
        self.sprite = sprite
        self.start_position = start_position

        self.body = [Part(start_position[0], start_position[1], self.color)]

    def draw(self, screen):
        for part in self.body:
            part.draw(screen)

    def add_head(self, x, y):
        self.body.append(Part(x, y, self.color))

    def get_parts_coords(self):
        for part in self.body[:-1]:
            yield part.x, part.y

    def get_head_coords(self):
        return self.body[-1].x, self.body[-1].y

    def move_snake(self, direction_x, direction_y):
        head_x, head_y = self.get_head_coords()

        self.body.pop(0)

        self.add_head(head_x + direction_x, head_y + direction_y)

    def reset(self):
        self.body = [Part(9, 9, self.color)]

