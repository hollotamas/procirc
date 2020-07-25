import pygame
from pygame.math import Vector2

class Circle(object):
    COLORS = {
        0: (255, 255, 255),
        1: (255, 0, 0),
        2: (0, 255, 0),
        3: (0, 0, 255),
        4: (255, 255, 0),
        5: (255, 0, 255),
        6: (0, 255, 255),
    }
    MAPS = "image/"
    targetImage = "target.png"
    balls = ["feher.png", "voros.png", "zold.png", "kek.png", "lila.png", "turkisz.png"]

    def __init__(self, ablak: pygame.Surface, color=0, pos=(250, 250), radius=50, vec=(0, 0), speed=1):
        self.ablak = ablak
        self.color = color
        self.pos = pos
        self.vec = vec
        self.speed = speed
        self.speedVec = self.getSpeedVector()
        self.radius = radius

    def getColor(self):
        return self.COLORS[self.color]

    def setColor(self, color: int):
        self.color = color

    def draw(self):
        self.pos = (self.pos[0] + self.speedVec[0], self.pos[1] + self.speedVec[1])
        posInt = (int(self.pos[0]), int(self.pos[1]))
        pygame.draw.circle(self.ablak, self.getColor(), posInt, self.radius, 0)

    def getPos(self):
        return pygame.math.Vector2(self.pos)

    def getSpeedVector(self):
        return (self.vec[0]/self.speed, self.vec[1]/self.speed)


