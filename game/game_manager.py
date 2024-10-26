import pygame # type: ignore
import utils.writeUtils as writeUtils
import game.characters.player as player
import game.characters.drawPlayer as drawPlayer
from game.map.map import map 
from screen import screen

class CreateGame:
    def __init__(self):
        self.map = map
        self.players = [ 
                player.Player(drawPlayer.drawCharacter()),
                player.Player(drawPlayer.drawCharacter()),
            ]
        self.players[0].setControlKeys(
            pygame.K_LEFT, 
            pygame.K_RIGHT, 
            pygame.K_UP, 
            pygame.K_DOWN
        )
        self.players[1].setControlKeys( 
            pygame.K_a, 
            pygame.K_d, 
            pygame.K_w, 
            pygame.K_s
        )
        self.players[1].setBoost()


    def run(self):
        writeUtils.drawSign( screen , 'Wersja testowa alfa aplikacji "Tag GAME"', [100,50])

        for p in self.players:
            p.run( self.map.mapSurfaceWithMask[1], self.map.mapPos )
            self.map.drawOnMap( p.characterSurface, p.pos)

        self.map.run()
    
