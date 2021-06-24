import pygame


class Ball:
    def __init__(self, WIN: pygame.surface.Surface, x: float, y: float, w: int, h: int, speed: int, color: tuple=(255, 255, 255)):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.speed_x = -self.speed
        self.speed_y = self.speed
        self.color = color

    def draw(self):
        pygame.draw.rect(self.WIN, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
