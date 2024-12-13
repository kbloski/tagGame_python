import pygame # type: ignore

keyboard = {
    'keys': pygame.key.get_pressed(),  
    'refresh': lambda: set_key_state()   
}

def set_key_state():
    keyboard['keys'] = pygame.key.get_pressed()

def isKeyPressed( key ):
    return keyboard['keys'][key]

