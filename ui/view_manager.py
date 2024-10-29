import game.game_manager.main_game as game
appGame = game.CreateGame()

class ViewManager:
    __INSTANCE = None
    def __new__(cls):
        if not ViewManager.__INSTANCE:
            ViewManager.__INSTANCE = super(ViewManager, cls).__new__(cls)
        return cls.__INSTANCE
    
    def __init__(self):
        self.activeView = 'game'
        self.views = {
            "game" : appGame,
        }

    def updateView(self, viewName):
        if self.views[str( viewName )]:
            self.activeView = viewName

    def render(self):
        self.views[self.activeView].render()