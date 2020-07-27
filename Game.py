import pygame
from random import randint
from Circle import Circle
from pygame.math import Vector2
from Status import Status


class Game(object):
    IMAGEPATH = "image/"
    STARTPOSRATE = .1
    def __init__(self, displaySurf: pygame.Surface, maxPont, ballsCount, speed, targetRate, ballRate, changeTargetSize=.2):
        self.displaySurf = displaySurf
        self.ballsCount = ballsCount
        self.speed = 1/speed
        self.targetImage = randint(0, len(Circle.BALLS)-1)
        self.pont = maxPont
        self.elapsedTime = 0
        self.targetRate = targetRate
        self.ballRate = ballRate
        self.changeTargetSize = changeTargetSize
        self.targetCircle = Circle(self.displaySurf, path=self.IMAGEPATH, image=self.targetImage, pos=(self.displaySurf.get_width() // 2, self.displaySurf.get_height() // 2),  scale=targetRate)
        self.pontFelirat = Status(self.displaySurf, (200, 10))
        self.ballsList = []
        self.ballsCreate()
        self.startTimeBalls = pygame.time.get_ticks()

    def getRandomStartPos(self):
        if randint(0, 1):
            xPos = randint(0, self.displaySurf.get_width( ))
        else:
            xPos = randint(self.displaySurf.get_width(), self.displaySurf.get_width() + self.displaySurf.get_width( ))

        if randint(0, 1):
            yPos = randint(0, self.displaySurf.get_width()*self.STARTPOSRATE)
        else:
            yPos = randint(self.displaySurf.get_height(), self.displaySurf.get_height() + self.displaySurf.get_width()*self.STARTPOSRATE)

        return (xPos, yPos)

    def ballCreate(self):
        pos = self.getRandomStartPos()
        vec = (self.targetCircle.getPos( )[0] - pos[0], self.targetCircle.getPos( )[1] - pos[1])
        self.ballsList.append(Circle(self.displaySurf, path=self.IMAGEPATH, image=randint(0, len(Circle.BALLS)-1), \
                                     pos=pos, \
                                     vec=vec,
                                     speed=pygame.math.Vector2(vec).length( ) * self.speed, \
                                     scale=self.ballRate))

    def ballsCreate(self):
        for i in range(self.ballsCount):
            self.ballCreate()

    def update(self):
        gameOver = False
        for ball in self.ballsList:
            if ball.getPos().distance_to(self.targetCircle.getPos()) < self.targetCircle.getRadius():
                if ball.getImage() != self.targetCircle.getImage():
                    self.pont -= 1
                    self.targetCircle.setScale(self.changeTargetSize)
                    self.targetCircle.setImage(self.targetImage)
                self.clearBall(ball)
        if len(self.ballsList) < 3:
            self.ballCreate()
        self.draw()
        if self.pont <= 0:
            gameOver = True
        return gameOver

    def getTime(self):
        self.elapsedTime = pygame.time.get_ticks( ) - self.startTimeBalls
        minute = self.elapsedTime // (60 * 1000)
        second = self.elapsedTime // 1000 - minute * 60
        return "{:0>2}:{:0>2}".format(minute, second)

    def draw(self):
        self.displaySurf.fill((0, 0, 0))
        self.targetCircle.draw()
        self.pontFelirat.draw(self.pont, self.getTime())
        for ball in self.ballsList:
            ball.draw()

    def clicked(self, pos):
        i = 0
        while i < len(self.ballsList) and not (self.ballsList[i].getPos().distance_to(pos) < self.ballsList[i].getRadius()):
            i += 1

        if i < len(self.ballsList):
            self.ballsList[i].setImage(randint(0, len(Circle.BALLS)-1))

    def clearBall(self, ball):
        self.ballsList.pop(self.ballsList.index(ball))


