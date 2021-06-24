import pygame


class Paddle:
    def __init__(self, WIN, x: int, y: float, w: int, h: int, speed: int, color: tuple=(255, 255, 255)):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.color = color

    def draw(self):
        pygame.draw.rect(self.WIN, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

    def move(self):
        self.y += self.speed

    def change_direction(self):
        self.speed *= -1

    def is_direction_down(self):
        if self.speed > 0:
            return True
        return False
