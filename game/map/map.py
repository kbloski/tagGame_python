import pygame
from screen import screen
from .drawMap1 import map1
import utils.surfaceUtils as surfaceUtils


class CrateMap:
    def __init__(self, mapSurface):
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

map = CrateMap(map1.getMapSurface())