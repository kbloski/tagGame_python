from .measurementUtils import roundNumber

class CreateClock:
    __CURRENT_GAME_TIME = 0
    __CURRENT_TICK = 0
    __WATCHERS = []

    def __init__(self):
        self.__WATCHERS.append( self )
        self.isActive = False
        #TODO self.isReady = True 
        self.__currentTime = 0
        self.countdown_seconds = 999_999_999

    @classmethod
    def increment(self, tickMiliseconds):
        CreateClock.__CURRENT_TICK = tickMiliseconds
        CreateClock.__CURRENT_GAME_TIME += tickMiliseconds
        for watch in self.__WATCHERS:
            if watch.isActive:
                watch.__currentTime += tickMiliseconds
    
    def getTime(self):
        return roundNumber( self.__currentTime / 1000 )

    def setCountdown(self, seconds = 999_999_999):
        self.countdown_seconds = seconds * 1000

    def reset( self ):
        self.__currentTime = 0
        self.isActive = False

    def start( self):
        self.isActive = True

    def stop( self ):
        self.isActive = False

    def hasEnded(self):
        self.__currentTime += self.__CURRENT_TICK

        if (self.countdown_seconds <= self.__currentTime):
            self.isActive = False
            return True
        return False
    

