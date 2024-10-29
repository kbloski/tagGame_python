import pygame # type: ignore
import utils.writeUtils as writeUtils
import utils.randomUtils as randomUtils
from utils.clock import CreateClock
import game.characters.player as player
import game.characters.drawPlayer as drawPlayer
from game.map.map import map 
from screen import screen


class ModuleGameCaptions:
    CAPTIONS = {}
    def addCaption(self, name = 'caption-name', surface = pygame.surface ):
        self.CAPTIONS[name] = surface

class ModuleGamePlayers( ModuleGameCaptions ):
    PLAYERS =  [ 
        player.Player(drawPlayer.drawCharacter()),
        player.Player(drawPlayer.drawCharacter()),
    ]
    def __init__(self):
        super().__init__()

        self.PLAYERS[0].setControlKeys(
            pygame.K_LEFT, 
            pygame.K_RIGHT, 
            pygame.K_UP, 
            pygame.K_DOWN
        )
        self.PLAYERS[1].setControlKeys( 
            pygame.K_a, 
            pygame.K_d, 
            pygame.K_w, 
            pygame.K_s
        )

        self.addCaption(
            'tagCaption', writeUtils.createSignSurface("TagPlayer!", 16) 
        )
        self.taggerClock = CreateClock()
        self.taggerClock.setCountdown(3)
        self.taggerClock.start()
        self.tagPlayerId = randomUtils.getRandomElFromArr(self.PLAYERS).id
        tagPlayer = self._getPlayerById( self.tagPlayerId )
        tagPlayer.addBoost()

    def _getPlayerById(self, id):
        for p in self.PLAYERS:
            if p.id == id:
                return p
        return None
    
    def _addBoost(self, playerId):
        player = self._getPlayerById( playerId )
        if player:
            player.addBoost()

    def _removeBost(self, playerId):
        player = self._getPlayerById( playerId)
        if player:
            player.removeBost()

    def _setNewTagger(self, playerId):
        self.taggerClock.reset()
        self.taggerClock.start()
        tagPlayer = self._getPlayerById( self.tagPlayerId )
        tagPlayer.removeBost()
        self.tagPlayerId = playerId
        self._addBoost( playerId )

    def _drawTagerCaption(self, player, map):
        signPos = player.getCurrentPos()
        signPos[1] -= 25
        map.drawOnMap( self.CAPTIONS['tagCaption'], signPos )


class CreateGame( ModuleGamePlayers, ModuleGameCaptions):
    def __init__(self):
        super().__init__()

        self.addCaption( 'title' , writeUtils.createSignSurface('Wersja testowa alfa aplikacji "Tag GAME"!'))
        
        self.map = map

    def run(self):
        screen.blit( self.CAPTIONS['title'], [100,30])

        for p in self.PLAYERS:
            p.run( self.map.mapSurfaceWithMask[1], self.map.mapPos )
            self.map.drawOnMap( p.characterSurface, p.pos)

            if self.tagPlayerId == p.getId():
                self._drawTagerCaption(p, map)
                for i in self.PLAYERS:
                    if self.taggerClock.hasEnded():
                        if i.id != p.id and p.colisionWithOtherMask(i.getCurrentMask(), i.getCurrentPos()):
                            self._setNewTagger( i.id )
        self.map.run()
    
