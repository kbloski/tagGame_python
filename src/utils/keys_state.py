import pygame # type: ignore

mouse = {
    'pos' : pygame.mouse.get_pos(),
    'refresh' : lambda: getMousePos()
}

def getMousePos():
    mouse['pos'] = pygame.mouse.get_pos()

keyboard = {
    'keys': pygame.key.get_pressed(),  
    'refresh': lambda: set_key_state()   
}

def set_key_state():
    keyboard['keys'] = pygame.key.get_pressed()

def isKeyPressed( key ):
    return keyboard['keys'][key]

