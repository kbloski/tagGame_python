import pygame
import src.characters.player as player
from src.maps.map import map

class Game:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        map.run()
    


