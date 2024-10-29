import utils.writeUtils as writeUtils
from .map import MAP1
from screen import screen
from .players import ModuleGamePlayers
from .caption import ModuleGameCaptions

class CreateGame( ModuleGamePlayers, ModuleGameCaptions):
    def __init__(self):
        super().__init__()

        self.addCaption( 'title' , writeUtils.createSignSurface('Wersja testowa alfa aplikacji "Tag GAME"!'))
        
        self.map = MAP1

    def run(self):
        screen.blit( self.CAPTIONS['title'], [100,30])

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




    
