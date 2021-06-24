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
        self.score_a = 0
        self.score_b = 0
        self.font = pygame.font.SysFont("comicsans", 40)

    def draw(self):
        self.WIN.fill((30, 30, 30))
        self.paddle_a.draw()
        self.paddle_b.draw()
        self.ball.draw()

        score_label = self.font.render(f"""A: {self.score_a} | B: {self.score_b}""", True, (255, 255, 255))
        self.WIN.blit(score_label, (self.WIN.get_width()/2 - score_label.get_width()/2, 5))

        pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit(-1)

    def move(self):
        # move the paddles based on the keys that pressed by the user
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
        if keys[pygame.K_s]:
            if self.paddle_a.y + self.paddle_a.h + self.paddle_a.speed <= self.WIN.get_height() - 5:
                if self.paddle_a.is_direction_down():
                    self.paddle_a.move()
                else:
                    self.paddle_a.change_direction()
                    self.paddle_a.move()

        # move the right paddle up
        if keys[pygame.K_UP]:
            if self.paddle_b.y + self.paddle_b.speed >= 5:
                if self.paddle_b.is_direction_down():
                    self.paddle_b.change_direction()
                    self.paddle_b.move()
                else:
                    self.paddle_b.move()

        # move the right paddle down
        if keys[pygame.K_DOWN]:
            if self.paddle_b.y + self.paddle_b.h + self.paddle_b.speed <= self.WIN.get_height() - 5:
                if self.paddle_b.is_direction_down():
                    self.paddle_b.move()
                else:
                    self.paddle_b.change_direction()
                    self.paddle_b.move()

        # move ball based on collisions

        # detecting collision in the edges of the screen in the y axis
        if self.ball.y + self.ball.speed_y <= 5:
            self.ball.speed_y *= -1
        elif self.ball.y + self.ball.h + self.ball.speed_y >= self.WIN.get_height() - 5:
            self.ball.speed_y *= -1

        # detecting collision in the edges of the screen in the y axis
        if self.ball.x + self.ball.speed_x <= 5:
            self.score_b += 1
            self.ball.speed_x *= -1
            self.ball.y = self.WIN.get_height()/2 - self.ball.h/2
            self.ball.x = self.WIN.get_width()/2 - self.ball.w/2
        elif self.ball.x + self.ball.w + self.ball.speed_x >= self.WIN.get_width() - 5:
            self.score_a += 1
            self.ball.speed_x *= -1
            self.ball.y = self.WIN.get_height()/2 - self.ball.h/2
            self.ball.x = self.WIN.get_width()/2 - self.ball.w/2

        self.ball.y += self.ball.speed_y
        self.ball.x += self.ball.speed_x

        # ball collision with the paddles
        if self.ball.x <= self.paddle_a.x + self.paddle_a.w and self.ball.y >= self.paddle_a.y and self.ball.y <= self.paddle_a.y + self.paddle_a.h:
            self.ball.speed_x *= -1
        elif self.ball.x + self.ball.w >= self.paddle_b.x and self.ball.y >= self.paddle_b.y and self.ball.y <= self.paddle_b.y + self.paddle_b.h:
            self.ball.speed_x *= -1

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.draw()
            self.event_handler()
            self.move()
