import pygame
import utils.writeUtils as writeUtils
from game.maps.map import map 
from screen import screen

class CreateGame:
    def __init__(self):
        pass

    def run(self):
        writeUtils.drawSign( screen , 'Wersja testowa alfa aplikacji "Tag GAME"', [100,50])

        map.run()
    
