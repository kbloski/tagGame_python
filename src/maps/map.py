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

        self.players = [ 
                player.Player(drawPlayer.drawCharacter()),
                player.Player(drawPlayer.drawCharacter()),
            ]
        self.players[0].setControlKeys(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        self.players[1].setControlKeys( pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        self.players[1].setBoost()

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