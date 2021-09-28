import time
import pygame
from .Snake.snake import Snake
from .assets import constans


class Game:
    def __init__(self):
        self.w = 0
        self.s = 0
        self.a = 0
        self.d = 0

        self.direction_x = 0
        self.direction_y = 0

    def directions_detection(self, event):

        if event[pygame.K_w] and not self.s:
            self.a, self.d = 0, 0
            self.w = 1

            self.direction_x = 0
            self.direction_y = -1

        elif event[pygame.K_s] and not self.w:
            self.a, self.d = 0, 0
            self.s = 1

            self.direction_x = 0
            self.direction_y = 1

        elif event[pygame.K_a] and not self.d:
            self.w, self.s = 0, 0
            self.a = -1

            self.direction_x = -1
            self.direction_y = 0

        elif event[pygame.K_d] and not self.a:
            self.w, self.s = 0, 0
            self.d = 1

            self.direction_x = 1
            self.direction_y = 0

    def start_game(self):
        pygame.init()
        screen = pygame.display.set_mode((constans.GAME_WIDTH, constans.GAME_HEIGHT))
        snake = Snake()

        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()

                self.directions_detection(pygame.key.get_pressed())

            snake.draw(screen)
            snake.move_snake(self.direction_x, self.direction_y)
            pygame.display.flip()

            time.sleep(1 / constans.GAME_SPEED)
            screen.fill((0, 0, 0))
