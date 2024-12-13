from ...utils import randomUtils
from ...utils.clock import CreateClock
from ..characters.player import Player
from ..graphics.index import player1, player2
from ...utils import writeUtils
from .caption import ModuleGameCaptions
from ...config import settings

class ModuleGamePlayers( ModuleGameCaptions ):
    PLAYERS =  [ 
        Player(player1),
        Player(player2),
    ]
    def __init__(self):
        super().__init__()

        self.PLAYERS[0].setControlKeys( settings.PLAYER_CONTROLS[0]['keys'] )
        self.PLAYERS[1].setControlKeys( settings.PLAYER_CONTROLS[1]['keys'] )

        self.addCaption(
            'tagCaption', writeUtils.createSignSurface("TagPlayer!", 16) 
        )

        self.taggerClock = CreateClock()
        self.taggerClock.setCountdown(3)
        self.taggerClock.start()
        self.__tagPlayerId = randomUtils.getRandomElFromArr(self.PLAYERS).id
        tagPlayer = self._getPlayerById( self.__tagPlayerId )
        tagPlayer.addBoost()

    def getTagPlayerId(self):
        return self.__tagPlayerId

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

    def _checkCatchByTagger(self, player):
        for i in self.PLAYERS:
            if self.taggerClock.hasEnded():
                if i.id != player.id and player.colisionWithOtherMask(i.getCurrentMask(), i.getCurrentPos()):
                    self._setNewTagger( i.id )


    def _setNewTagger(self, playerId):
        self.taggerClock.reset()
        self.taggerClock.start()
        tagPlayer = self._getPlayerById( self.__tagPlayerId )
        tagPlayer.removeBost()
        self.__tagPlayerId = playerId
        self._addBoost( playerId )

    def _drawTagerCaption(self, player, map):
        signPos = player.getCurrentPos()
        signPos[1] -= 25
        map.drawOnMap( self.CAPTIONS['tagCaption'], signPos )