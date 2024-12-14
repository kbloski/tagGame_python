import pygame, sys # type: ignore
pygame.init()

from src.ui.views import index 
import src.utils.keys_state as keys_state
from src.utils.clock import CreateClock
from src.ui.viewManager import viewManager
from src.config.screen import screen

pygame.display.set_caption('Berek')

clock = pygame.time.Clock()
fps = 120

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()

    clock.tick(fps)
    
    # print(clock.get_fps())


    keys_state.keyboard['refresh']()

    screen.fill('#ffffff')
    viewManager.render()
    pygame.display.flip()
    
    CreateClock.increment( clock.get_time()) 
    
