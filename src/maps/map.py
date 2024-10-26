import pygame
from screen import screen
from src.maps.drawMap1 import map1
import src.characters.player as player
import src.utils.maskUtils as maskUtils
import src.characters.drawPlayer as drawPlayer

class CrateMap:
    def __init__(self, mapSurface):
        self.frameSurface = pygame.Surface( screen.get_size())
        self.mapSurfaceWithMask = [ 
            mapSurface, 
            maskUtils.getMaskFromSurface(mapSurface)
        ]
        self.mapPos = [0,0]

        self.players = [ player.Player(drawPlayer.drawCharacter()) ]

    def __newFrame(self):
        self.frameSurface = pygame.Surface( screen.get_size()).convert_alpha()
        self.frameSurface.fill( (0,0,0,0) )

    def drawOnMap(self,  anySurface, position ):
        self.frameSurface.blit( anySurface, position )

    def drawMapOnScreen(self):
        self.frameSurface.blit( self.mapSurfaceWithMask[0], self.mapPos)
        screen.blit(self.frameSurface, (0,0))

    def run(self):
        for p in self.players:
            p.run( self.mapSurfaceWithMask[1], self.mapPos )
            self.drawOnMap( p.characterSurface, p.pos)

        self.drawMapOnScreen()
        self.__newFrame()

        

map = CrateMap(map1.getMapSurface())