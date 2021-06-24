import pygame
from . import Ball
from . import Paddle


class Game:
    def __init__(self, WIN: pygame.surface.Surface, clock: pygame.time.Clock, FPS: int, paddle_a: Paddle,
                 paddle_b: Paddle, ball: Ball):
        self.WIN = WIN
        self.clock = clock
        self.FPS = FPS
        self.paddle_a = paddle_a
        self.paddle_b = paddle_b
        self.ball = ball
        self.score = 0

    def draw(self):
        self.WIN.fill((30, 30, 30))
        self.paddle_a.draw()
        self.paddle_b.draw()
        self.ball.draw()

        pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit(-1)

    def collision(self):
        pass

    def move(self):
        keys = pygame.key.get_pressed()

        # move the left paddle up
        if keys[pygame.K_w]:
            if self.paddle_a.y + self.paddle_a.speed >= 5:
                if self.paddle_a.is_direction_down():
                    self.paddle_a.change_direction()
                    self.paddle_a.move()
                else:
                    self.paddle_a.move()

        # move the left paddle down
        elif keys[pygame.K_s]:
            if self.paddle_a.y + self.paddle_a.h + self.paddle_a.speed <= self.WIN.get_height() - 5:
                if self.paddle_a.is_direction_down():
                    self.paddle_a.move()
                else:
                    self.paddle_a.change_direction()
                    self.paddle_a.move()

        # move the right paddle up
        elif keys[pygame.K_UP]:
            if self.paddle_b.y + self.paddle_b.speed >= 5:
                if self.paddle_b.is_direction_down():
                    self.paddle_b.change_direction()
                    self.paddle_b.move()
                else:
                    self.paddle_b.move()

        # move the right paddle down
        elif keys[pygame.K_DOWN]:
            if self.paddle_b.y + self.paddle_b.h + self.paddle_b.speed <= self.WIN.get_height() - 5:
                if self.paddle_b.is_direction_down():
                    self.paddle_b.move()
                else:
                    self.paddle_b.change_direction()
                    self.paddle_b.move()

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.draw()
            self.event_handler()
            self.collision()
            self.move()
