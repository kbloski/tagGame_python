import pygame # type: ignore
import utils.writeUtils as writeUtils
import utils.randomUtils as randomUtils
from utils.clock import CreateClock
import game.characters.player as player
import game.characters.drawPlayer as drawPlayer
from game.map.map import map 
from screen import screen

class CreateGame:
    def __init__(self):
        self.captions = {
            'tagger' : writeUtils.createSignSurface("TagPlayer!", 16),
            'title' : writeUtils.createSignSurface('Wersja testowa alfa aplikacji "Tag GAME"!'),
        }
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

        self.taggerClock = CreateClock()
        self.taggerClock.setCountdown(10)
        self.taggerClock.start()
        self.tagPlayerId = randomUtils.getRandomElFromArr(self.players).id

    def __setTagger(self, playerId):
        self.taggerClock.reset()
        self.taggerClock.start()
        self.tagPlayerId = playerId


    def __drawTagerCaption(self, player, map):
        signPos = player.getCurrentPos()
        signPos[1] -= 25
        self.map.drawOnMap( self.captions['tagger'], signPos )

    def run(self):
        screen.blit( self.captions['title'], [100,30])

        for p in self.players:
            p.run( self.map.mapSurfaceWithMask[1], self.map.mapPos )
            self.map.drawOnMap( p.characterSurface, p.pos)

            if self.tagPlayerId == p.getId():
                self.__drawTagerCaption(p, map)
                for i in self.players:
                    if self.taggerClock.hasEnded():
                        if i.id != p.id and p.colisionWithOtherMask(i.getCurrentMask(), i.getCurrentPos()):
                            # self.tagPlayerId = i.id
                            self.__setTagger( i.id )




        self.map.run()
    
