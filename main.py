import pygame, sys

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 600, 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

clock = pygame.time.Clock()
FPS = 30

from classes import *
from process import process

startPoint = (100, 100)

snake = Snake(startPoint[0], startPoint[1], 20)

while True:

    process(snake, SCREENWIDTH, SCREENHEIGHT)

    screen.fill((0, 0, 0))

    if not snake.game_over:
        snake.movement(SCREENWIDTH, SCREENHEIGHT)

    for i in range(len(snake.body)):
        pygame.draw.rect(screen, (255, 255, 255), (snake.body[i][0][0] , snake.body[i][0][1], snake.size, snake.size), 0)

    pygame.draw.circle(screen, (255, 255, 255), (snake.foodx, snake.foody), snake.food_radius, 0)

    pygame.display.flip()
    clock.tick(FPS)
