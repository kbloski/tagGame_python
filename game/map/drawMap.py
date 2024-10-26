import pygame
from screen import screen

class MapSurfaceControl:
    def __init__(self):
        self.WIDTH = screen.get_width()
        self.HEIGHT = screen.get_height()
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


map1 = MapSurfaceControl()
map1.createRamp(100,900, 300,5)
map1.createRamp(300,700, 20,3)
