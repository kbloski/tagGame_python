import pygame

def updateKeysInKeyboard():
    keyboard['keys'] = pygame.key.get_pressed()

# Tworzymy słownik 'keyboard' z klawiszami i funkcją odświeżającą
keyboard = {
    'keys': pygame.key.get_pressed(),  
    'refresh': lambda: updateKeysInKeyboard()   
}