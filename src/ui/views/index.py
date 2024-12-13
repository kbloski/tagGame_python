from ..viewManager import viewManager
from .game import CreateGame
from .menu import CreateMenu

appGame = CreateGame()
menu = CreateMenu()

viewManager.createView( 'main', menu)
viewManager.createView( 'game', appGame)

viewManager.setActiveView('game')