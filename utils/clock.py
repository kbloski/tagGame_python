from .measurementUtils import roundNumber

class CreateClock:
    __CURRENTGAMETIME = 0

    def __init__(self):
        self.isActive = False
        self.isReady = False
        self.currentTime = 0
        self.countdown_seconds = 999_999_999

    @classmethod
    def increment(self, tickMiliseconds):
        CreateClock.__CURRENTGAMETIME += tickMiliseconds
    
    def __getCurrentTime(self):
        return roundNumber( self.__CURRENTGAMETIME / 1000 )
    
    def setCountdown(self, seconds = 999_999_999):
        self.countdown_seconds = seconds

    def reset( self ):
        self.currentTime = 0
        self.isReady = True

    def start( self):
        self.isActive = True

    def stop( self ):
        self.isActive = False

    def hasEnded(self):
        if (self.countdown_seconds <= self.currentTime):
            self.isActive = False
            return True
        return False
    