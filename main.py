from Parts import Paddle
from Parts import Ball
from Parts import Game
import pygame


pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

paddle_height = 100
paddle_width = 20
paddle_speed = 10
ball_width = 20
ball_height = 20
ball_speed = 10

paddle_a = Paddle(WIN, 10, HEIGHT/2 - paddle_height/2, paddle_width, paddle_height, paddle_speed, (255, 255, 255))
paddle_b = Paddle(WIN, WIDTH - 10 - paddle_width, HEIGHT/2 - paddle_height/2, paddle_width, paddle_height, paddle_speed, (255, 255, 255))
ball = Ball(WIN, WIDTH/2 - ball_width/2, HEIGHT/2 - ball_height/2, ball_width, ball_height, ball_speed, color=(100, 100, 100))
clock = pygame.time.Clock()
FPS = 24

game = Game(WIN, clock, FPS, paddle_a, paddle_b, ball)
game.run()
