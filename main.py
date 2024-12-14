import pygame, sys # type: ignore
pygame.init()

from src.ui.views import index 
from src.utils.keys_state import mouse, keyboard
from src.utils.clock import CreateClock
from src.ui.viewManager import viewManager
from src.config.screen import screen

from src.graphics.index import mouseSurfaces

pygame.display.set_caption('Berek')
pygame.mouse.set_visible( False )

clock = pygame.time.Clock()
fps = 120

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()

    clock.tick(fps)
    
    # print(clock.get_fps())


    keyboard['refresh']()
    mouse['refresh']()

    screen.fill('#ffffff')
    viewManager.render()
    
    # draw mouse
    screen.blit( mouseSurfaces['basic'], mouse['pos']) 

    pygame.display.flip()

    
    CreateClock.increment( clock.get_time()) 
    
