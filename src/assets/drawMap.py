import pygame # type: ignore
from ..config.screen import screen

class CreateMapSurface:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.mapSurface = pygame.Surface( (self.WIDTH, self.HEIGHT) ).convert_alpha()
        self.mapSurface.fill((0,0,0,0))
    
    def __drawBorderMap(self):
        borderColor = "#000020"
        borderWidth = 5
        pygame.draw.rect( self.mapSurface, borderColor, [0,0,self.WIDTH, borderWidth])
        pygame.draw.rect( self.mapSurface, borderColor, [0,self.HEIGHT-borderWidth,self.WIDTH, borderWidth])
        pygame.draw.rect( self.mapSurface, borderColor, [0,0,borderWidth, self.HEIGHT])
        pygame.draw.rect( self.mapSurface, borderColor, [self.WIDTH-borderWidth,0,borderWidth, self.HEIGHT])

    def createRamp(self, x, y, width, height, color='#000000'):
        pygame.draw.rect(self.mapSurface, color, (x,y,width, height) )

    def getMapSurface(self):
        self.__drawBorderMap()
        return self.mapSurface

