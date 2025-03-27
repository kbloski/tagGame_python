import pygame
from ...config.screen import screen
from ...graphics.drawText import CreateSign, createSignSurface

class CreateButton: 
    def __init__(self, 
                 text = 'button', 
                 bgColor = '#555555',
                 position = [0,0], 
                 width = None, 
                 height = None ):
        
        self.size = [100, 50]
        self.pos = position
        # self.size = [width, height]
        self.bgColor = bgColor
        self.signSurface = createSignSurface( text )
        self.surfaces = {
            'basic' : None,
            'hover' : None
        }
        
        self._createButtonImgs()

    def _createButtonImgs( self ):
        baseSurface = pygame.Surface( self.size)
        baseSurface.fill( self.bgColor )
        self.surfaces['basic'] = baseSurface

    def draw( self ):
        screen.blit( self.surfaces['basic'],  self.pos)

