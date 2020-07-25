import pygame
from random import randint
from Circle import Circle
from pygame.math import Vector2
from Pont import Pont


class Game(object):

    def __init__(self, displaySurf: pygame.Surface, ballsCount, speed):
        self.displaySurf = displaySurf
        self.ballsCount = ballsCount
        self.speed = speed
        self.targetCircle = Circle(self.displaySurf, color=randint(0, len(Circle.COLORS)-1), pos=(self.displaySurf.get_width() // 2, self.displaySurf.get_height() // 2), radius=30)
        self.pontFelirat = Pont(self.displaySurf, "Elért pont", (300, 10))
        self.ballsList = []
        self.ballsCreate()
        self.pont = 10
        self.startTimeBalls = pygame.time.get_ticks()

    def ballCreate(self):
        pos = (randint(0, self.displaySurf.get_width()), randint(0, self.displaySurf.get_height()))
        vec = (self.targetCircle.getPos( )[0] - pos[0], self.targetCircle.getPos( )[1] - pos[1])
        self.ballsList.append(Circle(self.displaySurf, color=randint(0, len(Circle.COLORS) - 1), \
                                     pos=pos, \
                                     radius=20, \
                                     vec=vec,
                                     speed=pygame.math.Vector2(vec).length( ) * self.speed))

    def ballsCreate(self):
        for i in range(self.ballsCount):
            self.ballCreate()

    def update(self):
        gameOver = False
        for ball in self.ballsList:
            if ball.getPos().distance_to(self.targetCircle.getPos()) < self.targetCircle.radius:
                if ball.getColor() != self.targetCircle.getColor():
                    self.pont -= 1
                self.clearBall(ball)
        if len(self.ballsList) < 3:
            self.ballCreate()
        self.draw()
        if self.pont <= 0:
            gameOver = True
        return gameOver

    def draw(self):
        self.displaySurf.fill((0, 0, 0))
        self.targetCircle.draw()
        self.pontFelirat.draw(self.pont)
        for ball in self.ballsList:
            ball.draw()


    def clicked(self, pos):
        i = 0
        while i < len(self.ballsList) and not (self.ballsList[i].getPos().distance_to(pos) < self.ballsList[i].radius):
            i += 1

        if i < len(self.ballsList):
            self.ballsList[i].setColor(randint(0, len(Circle.COLORS)-1))

    def clearBall(self, ball):
        self.ballsList.pop(self.ballsList.index(ball))