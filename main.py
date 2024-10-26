import pygame, sys
pygame.init()

import src.game as game
import src.utils.inputHandler as inputHandler
from screen import screen



pygame.display.set_caption('Berek')

clock = pygame.time.Clock()
fps = 120

appGame = game.Game(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()

    clock.tick(fps)
    # print(clock.get_fps())
    inputHandler.keyboard['refresh']()

    appGame.run()

    pygame.display.flip()
    pygame.draw.rect(screen, '#DDDDDD', [0,0,screen.get_width(), screen.get_height()])
