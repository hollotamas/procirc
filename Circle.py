import pygame
from pygame.math import Vector2
import os

class Circle(object):
    # COLORS = {
    #     0: (255, 255, 255),
    #     1: (255, 0, 0),
    #     2: (0, 255, 0),
    #     3: (0, 0, 255),
    #     4: (255, 255, 0),
    #     5: (255, 0, 255),
    #     6: (0, 255, 255),
    # }

    BALLS = ["feher.png", "voros.png", "zold.png", "kek.png", "lila.png", "turkisz.png"]
    def __init__(self, displaySurf: pygame.Surface, path: str, image: int, pos=(250, 250), radius=50, vec=(0, 0), speed=1, scale = 1):
        self.displaySurf = displaySurf
        self.path = path
        self.imageStr = self.BALLS[image]
        self.pos = pos
        self.vec = vec
        self.speed = speed
        self.speedVec = self.getSpeedVector()
        self.radius = radius
        self.scale = scale
        self.image = pygame.image.load(os.path.join(self.path, self.imageStr))

    # def getColor(self):
    #     return self.COLORS[self.color]
    #
    # def setColor(self, color: int):
    #     self.color = color

    def getImage(self):
        return self.BALLS.index(self.imageStr)

    def setImage(self, image: int):
        self.imageStr = self.BALLS[image]
        self.image = pygame.image.load(os.path.join(self.path, self.imageStr))

    def draw(self):
        self.pos = (self.pos[0] + self.speedVec[0], self.pos[1] + self.speedVec[1])
        drawPos = (self.pos[0] - self.image.get_rect().size[0] // 2, self.pos[1] - self.image.get_rect().size[1] // 2)
        posInt = (int(drawPos[0]), int(drawPos[1]))
        self.displaySurf.blit(self.image, posInt)

    def getPos(self):
        return pygame.math.Vector2(self.pos)

    def getSpeedVector(self):
        return (self.vec[0]/self.speed, self.vec[1]/self.speed)


