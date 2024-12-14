from ...utils.clock import CreateClock
from ...config.screen import screen
from ...graphics import drawText
from ...utils.measurementUtils import roundNumber

class ModuleGameTimmer:
    def __init__(self, roundTime = 20):
        self.gameClock = CreateClock()

        self.gameClock.setCountdown( roundTime )
        self.gameClock.start()

        self.sign = drawText.CreateSign( self.gameClock.getCountdownTime() , [100, 100])

    def _updateSignSurface(self):
        savedTime = int( self.sign.innerText )
        if (savedTime > self.gameClock.getCountdownTime()):
            self.sign.updateSign( int( self.gameClock.getCountdownTime() ))

    def drawTimmer(self):
        self._updateSignSurface()
        self.sign.draw(screen)