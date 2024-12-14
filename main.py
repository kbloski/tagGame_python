import pygame, sys # type: ignore
pygame.init()

from src.ui.views import index 
import src.utils.keys_state as keys_state
from src.utils.clock import CreateClock
from src.ui.viewManager import viewManager
from src.config.screen import screen

from src.graphics.index import mouseSurfaces

pygame.display.set_caption('Berek')
pygame.mouse.set_visible( False );

clock = pygame.time.Clock()
fps = 120

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()

    clock.tick(fps)
    
    # print(clock.get_fps())


    keys_state.keyboard['refresh']()
    keys_state.mouse['refresh']()

    screen.fill('#ffffff')
    viewManager.render()
    
    # draw mouse
    screen.blit( mouseSurfaces['basic'], keys_state.mouse['pos']) 

    pygame.display.flip()

    
    CreateClock.increment( clock.get_time()) 
    
