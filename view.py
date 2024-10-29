from utils.viewManager import viewManager
from ui.game import CreateGame
from ui.menu import CreateMenu

appGame = CreateGame()
menu = CreateMenu()

viewManager.createView( 'main', menu)
viewManager.createView( 'game', appGame)

viewManager.setActiveView('game')