import pygame # type: ignore
from src.config.screen import screen
import src.utils.surfaceUtils as surfaceUtils

class CreateMap:
    def __init__(self, mapSurface):
        self.mapIsReady = False
        self.frameSurface = pygame.Surface( screen.get_size())
        self.mapSurfaceWithMask = [ 
            mapSurface, 
            surfaceUtils.getMaskFromSurface(mapSurface)
        ]
        self.mapPos = [0,0]
       
    def __newFrame(self):
        self.frameSurface = pygame.Surface( screen.get_size()).convert_alpha()
        self.frameSurface.fill( (0,0,0,0) )

    def drawOnMap(self,  anySurface, position ):
        self.frameSurface.blit( anySurface, position )

    def drawMapOnScreen(self):
        self.frameSurface.blit( self.mapSurfaceWithMask[0], self.mapPos)
        screen.blit(self.frameSurface, (0,0))

    def run(self):
        self.drawMapOnScreen()
        self.__newFrame()

