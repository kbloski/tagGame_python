import pygame # type: ignore

mouse = {
    'pos' : pygame.mouse.get_pos(),
    'refresh' : lambda: _mouseRefresh(),
    'click' : pygame.mouse.get_pressed()
}

def _mouseRefresh():
    mouse['pos'] = pygame.mouse.get_pos()
    mouse['click'] = pygame.mouse.get_pressed()

keyboard = {
    'keys': pygame.key.get_pressed(),  
    'refresh': lambda: _setKeyboardState()   
}

def _setKeyboardState():
    keyboard['keys'] = pygame.key.get_pressed()

def isKeyPressed( key ):
    return keyboard['keys'][key]

