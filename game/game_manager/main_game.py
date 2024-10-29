from screen import screen
from utils import writeUtils
from .players import ModuleGamePlayers
from .caption import ModuleGameCaptions
from .timmer import ModuleGameTimmer
from .map import MAP1

class CreateGame( ModuleGamePlayers, ModuleGameCaptions, ModuleGameTimmer):
    def __init__(self):
        super().__init__()

        self.addCaption( 'title' , writeUtils.createSignSurface('Wersja testowa alfa aplikacji "Tag GAME"!'))
        self.map = MAP1


    def run(self):
        screen.blit( self.CAPTIONS['title'], [100,30])
        self.drawTimmer()
        # print( self.gameClock.getCountdownTime())
        # writeUtils.drawSign( screen, str( self.gameClock.getCountdownTime() ), [50, 20])
        # screen.blit( writeUtils.createSignSurface( self.gameClock.getCountdownTime() , 10))

        for p in self.PLAYERS:
            p.run( self.map.mapSurfaceWithMask[1], self.map.mapPos )
            self.map.drawOnMap( p.characterSurface, p.pos)

            if self.tagPlayerId == p.getId():
                self._drawTagerCaption(p, self.map)
                for i in self.PLAYERS:
                    if self.taggerClock.hasEnded():
                        if i.id != p.id and p.colisionWithOtherMask(i.getCurrentMask(), i.getCurrentPos()):
                            self._setNewTagger( i.id )
        self.map.run()




    
