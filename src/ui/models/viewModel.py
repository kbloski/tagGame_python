import pygame # type: ignore
from src.config.screen import screen
from src.config.screen import screen
from src.utils.writeUtils import drawSign

class ViewModel:
    def __init__(self):
        pass

    def render(self):
        drawSign(screen, "Custom - ViewModel.render(self): function.", [50,50], 25)