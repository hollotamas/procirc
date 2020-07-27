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
        gameTime = runGame(50, 2, 1)
        showGameOverScreen(gameTime)


def showStartScreen():
    title = pygame.font.SysFont('Verdana', 50)
    subtitle = pygame.font.SysFont('Verdana', 20)
    felirat = title.render("Start Game", False, (255, 255, 255))
    pressKey = subtitle.render("Press any key to continue!", True, (255, 0, 0))
    keyUp = False
    while not keyUp:
        DISPLAYSURF.blit(felirat, (DISPLAYSURF.get_width() // 2 - 150, DISPLAYSURF.get_height() // 2 - 40))
        DISPLAYSURF.blit(pressKey, (DISPLAYSURF.get_width() // 2 - 150, DISPLAYSURF.get_height() // 2 + 10))
        if pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()
        elif pygame.event.get(KEYUP):
            keyUp = True
        pygame.display.update( )
        FPSCLOCK.tick(FPS)

def runGame(maxPont=10, balls=3, ballSpeed=1, targetRate=2, ballRate=1):
    game = Game(DISPLAYSURF, maxPont, balls, ballSpeed, targetRate, ballRate)
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
    return str(game.elapsedTime / 1000)

def showGameOverScreen(elapsedTime: str):
    DISPLAYSURF.fill((0, 0, 0))
    title = pygame.font.SysFont('Verdana', 30)
    subtitle = pygame.font.SysFont('Verdana', 20)
    felirat = title.render("Game Over - Elapsed time: %s" % elapsedTime, False, (255, 255, 255))
    pressKey = subtitle.render("Press any key to new Game!", True, (255, 0, 0))
    keyUp = False
    while not keyUp:
        DISPLAYSURF.blit(felirat, (DISPLAYSURF.get_width() // 2 - 250, DISPLAYSURF.get_height() // 2 - 40))
        DISPLAYSURF.blit(pressKey, (DISPLAYSURF.get_width() // 2 - 250, DISPLAYSURF.get_height() // 2 + 10))
        if len(pygame.event.get(QUIT)) > 0:
            pygame.quit( )
            sys.exit( )
        keyUpEvents = pygame.event.get(KEYUP)
        if len(keyUpEvents) != 0:
            if keyUpEvents[0].key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            keyUp = True
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
