from src.utils.clock import CreateClock
from src.config.screen import screen
from src.utils import writeUtils

class ModuleGameTimmer:
    def __init__(self):
        self.gameClock = CreateClock()
        self.gameClock.setCountdown( 20 )
        self.gameClock.start()

        self.signHeight = 10

    def _setRoundTime(self, roundTime = 100):
        self.gameClock.setCountdown( roundTime )

    def drawTimmer(self):
        writeUtils.drawSign(
            screen,
            self.gameClock.getCountdownTime(),
        )