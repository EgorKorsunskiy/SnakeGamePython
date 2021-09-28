import pygame

from .part import Part
from ..assets.constans import CELL_SIZE, SNAKE_COLOR


class Snake:
    def __init__(self, sprite=None, start_position=(9*CELL_SIZE, 9*CELL_SIZE)):
        self.color = SNAKE_COLOR
        self.sprite = sprite
        self.start_position = start_position

        self.body = [Part(start_position[0], start_position[1], self.color)]

    def draw(self, screen):
        for part in self.body:
            part.draw(screen)

    def add_part(self, x, y):
        if not self.sprite:
            self.body.append(Part(x, y, self.color))
        else:
            pass

    def _remove_part(self):
        self.body.pop(0)

    def _get_head_coords(self):
        return self.body[0].x, self.body[0].y

    def get_parts_coords(self):
        for part in self.body:
            yield part.x, part.y

    def move_snake(self, direction_x, direction_y):
        head_x, head_y = self._get_head_coords()

        self._remove_part()

        self.body.append(Part(head_x + direction_x * CELL_SIZE, head_y + direction_y * CELL_SIZE, self.color))

        print(direction_x, direction_y)

