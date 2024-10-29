import pygame, sys # type: ignore
pygame.init()

import utils.handlerUtils as handlerUtils
from utils.clock import CreateClock
from config.screen import screen
from ui.view_manager import ViewManager

pygame.display.set_caption('Berek')
view = ViewManager()

clock = pygame.time.Clock()
fps = 120

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()

    clock.tick(fps)
    # print(gameClock.get_fps())
    handlerUtils.keyboard['refresh']()

    view.render()

    CreateClock.increment( clock.get_time())

    pygame.display.flip()
    screen.fill( '#99DD00')
