import pygame, sys
from pygame.locals import *
from Game import Game

#https://realpython.com/pygame-a-primer/
#https://stackoverflow.com/questions/11105836/multiple-displays-in-pygame

FPS = 60
WIDTH = 800
HEIGHT = 600

def main():
    global FPS, FPSCLOCK, DISPLAYSURF
    pygame.init()
    pygame.font.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Protect Your Circle!")

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def showStartScreen():
    #pass
    myFont = pygame.font.SysFont('Verdana', 30)
    felirat = myFont.render("Start Game", False, (255, 255, 255))
    pressKey = myFont.render("Press any key to continue!", True, (255, 0, 0))
    keyUp = False
    while not keyUp:
        DISPLAYSURF.blit(felirat, (DISPLAYSURF.get_width() // 2 - 150, DISPLAYSURF.get_height() // 2 - 20))
        DISPLAYSURF.blit(pressKey, (DISPLAYSURF.get_width() // 2 - 150, DISPLAYSURF.get_height() // 2 + 20))
        if pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()
        elif pygame.event.get(KEYUP):
            keyUp = True
        pygame.display.update( )
        FPSCLOCK.tick(FPS)

def runGame():
    game = Game(DISPLAYSURF, 3, 1)
    gameOver = False
    while not gameOver:
        gameOver = game.update()
        for event in pygame.event.get( ):
            if event.type == QUIT:
                pygame.quit( )
                sys.exit( )
            elif event.type == MOUSEBUTTONUP:
                game.clicked(event.pos)
        pygame.display.update( )
        FPSCLOCK.tick(FPS)

def showGameOverScreen():
    DISPLAYSURF.fill((0, 0, 0))
    myFont = pygame.font.SysFont('Verdana', 30)
    felirat = myFont.render("Game Over", False, (255, 255, 255))
    keyUp = False
    while not keyUp:
        DISPLAYSURF.blit(felirat, (DISPLAYSURF.get_width( ) // 2 - 100, DISPLAYSURF.get_height( ) // 2 - 100))
        if pygame.event.get(QUIT):
            pygame.quit( )
            sys.exit( )
        elif pygame.event.get(KEYUP):
            keyUp = True
        pygame.display.update( )
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
