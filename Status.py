import pygame
class Status(object):
    def __init__(self, displaySurf: pygame.Surface, pos=(0, 0)):
        self.ablak = displaySurf
        self.pont = 0
        self.pos = pos
        self.myFont = pygame.font.SysFont('Verdana', 30)

    def draw(self, pont, time):
        felirat = self.myFont.render("Health: %s - Elapsed time: %s" % (pont, time), False, (255, 255, 255))
        self.ablak.blit(felirat, self.pos)
    