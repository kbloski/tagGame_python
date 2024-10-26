import pygame, sys # type: ignore
pygame.init()

import utils.handlerUtils as handlerUtils
import game.game_manager as game
from screen import screen



pygame.display.set_caption('Berek')

clock = pygame.time.Clock()
fps = 120

appGame = game.CreateGame()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()

    clock.tick(fps)
    # print(clock.get_fps())
    handlerUtils.keyboard['refresh']()


    appGame.run()

    pygame.display.flip()
    screen.fill( '#99DD00')
