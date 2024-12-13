import pygame, sys # type: ignore
pygame.init()

from src.views import index 
import src.utils.handlerUtils as handlerUtils
from src.utils.clock import CreateClock
from src.utils.viewManager import viewManager

pygame.display.set_caption('Berek')

clock = pygame.time.Clock()
fps = 120

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()

    clock.tick(fps)
    # print(gameClock.get_fps())
    handlerUtils.keyboard['refresh']()
    viewManager.render()
    CreateClock.increment( clock.get_time()) 
    
