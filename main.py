import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

ablak = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Protect Your Circle!")

circle = pygame.image.load('kor.png')
x = 25
y = 25
direction = 'right'

while True:

    ablak.fill((0,0,0))

    if direction == 'right':
        x += 5
        if x > 300:
            direction = 'down'

    elif direction == 'down':
        y += 5
        if y > 300:
            direction = 'left'

    elif direction == 'left':
        x -= 5
        if x < 25:
            direction = 'up'

    elif direction == 'up':
        y -= 5
        if y < 25:
            direction = 'right'

    ablak.blit(circle, (x, y))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)