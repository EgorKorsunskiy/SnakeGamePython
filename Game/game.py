import pygame
from .Snake.snake import Snake
from .Fruit.fruit import Fruit
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

    def fruit_collision_detection(self, fruit, snake, screen):
        snake_x, snake_y = snake.get_head_coords()
        fruit_x, fruit_y = fruit.get_coords()

        if fruit_x == snake_x and fruit_y == snake_y:
            print(constans.game_score)
            constans.game_score += 1
            snake.add_head(snake_x + self.direction_x, snake_y + self.direction_y)

            pygame.mixer.music.play()

            fruit.generate_new_coords()
            fruit.spawn(screen)

    def snake_collision_detection(self, snake):
        head_x, head_y = snake.get_head_coords()

        if (head_x < 1 or head_x > 19) or (head_y < 1 or head_y > 19):

            return True

        for part in snake.get_parts_coords():
            if head_x == part[0] and head_y == part[1]:

                return True

    def start_game(self):
        pygame.init()

        pygame.mixer.init()
        pygame.mixer.music.load("./Game/assets/Sounds/gulp.mp3")

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((constans.GAME_WIDTH, constans.GAME_HEIGHT))

        font = pygame.font.SysFont('./Game/assets/Fonts/GemunuLibre-Regular.ttf', 72)

        text = font.render('Press C to try again', 1, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (constans.GAME_WIDTH // 2, constans.GAME_HEIGHT // 2)

        font_score = pygame.font.SysFont('./Game/assets/Fonts/GemunuLibre-Regular.ttf', 42)

        snake = Snake()
        fruit = Fruit()

        is_game_over = False

        while True:

            while is_game_over:
                screen.blit(text, text_rect)
                pygame.display.flip()

                for events in pygame.event.get():
                    if pygame.key.get_pressed()[pygame.K_c]:
                        snake.reset()

                        self.direction_x = 0
                        self.direction_y = 0

                        constans.game_score = 0

                        is_game_over = False
                        break

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()

                self.directions_detection(pygame.key.get_pressed())

            score_text = font_score.render(f'Score {constans.game_score}', 1, (255, 255, 255))
            score_rect = score_text.get_rect()
            score_rect.center = (constans.GAME_WIDTH - 70, 25)
            screen.blit(score_text, score_rect)

            fruit.spawn(screen)
            snake.move_snake(self.direction_x, self.direction_y)
            snake.draw(screen)

            self.fruit_collision_detection(fruit, snake, screen)
            is_game_over = self.snake_collision_detection(snake)

            pygame.display.flip()
            clock.tick(constans.GAME_SPEED)
            screen.fill((0, 0, 0))
