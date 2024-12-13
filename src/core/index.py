from ..utils.viewManager import viewManager
from ..config.screen import screen
from ..utils import writeUtils
from .game_manager.players import ModuleGamePlayers
from .game_manager.caption import ModuleGameCaptions
from .game_manager.timmer import ModuleGameTimmer
from .game_manager.map import MAP1


class MainGame( ModuleGamePlayers, ModuleGameCaptions, ModuleGameTimmer):
    def __init__(self):
        super().__init__()

        self.addCaption( 'title' , writeUtils.createSignSurface('Wersja testowa alfa aplikacji "Tag GAME"!'))
        self.map = MAP1

    def render(self):
        screen.blit( self.CAPTIONS['title'], [100,30])
        self.drawTimmer()

        for p in self.PLAYERS:
            p.run( self.map.mapSurfaceWithMask[1], self.map.mapPos )
            self.map.drawOnMap( p.characterSurface, p.pos)

            if self.getTagPlayerId() == p.getId():
                self._drawTagerCaption(p, self.map)
                self._checkCatchByTagger(p)

        self.map.run()




    