import pygame
class Pont(object):
    def __init__(self, displaySurf: pygame.Surface, felirat: str, pos=(0, 0)):
        self.ablak = displaySurf
        self.pont = 0
        self.szoveg = felirat
        self.pos = pos
        self.myFont = pygame.font.SysFont('Verdana', 30)
        self.felirat = self.myFont.render(self.szoveg, False, (255, 255, 255))


    def draw(self, pont):
        self.felirat = self.myFont.render("%s: %s" % (self.szoveg, pont), False, (255, 255, 255))
        self.ablak.blit(self.felirat, self.pos)
    