import pygame # type: ignore
from ...config.screen import screen
from ...config.screen import screen
from ...graphics.drawText import drawSign

class ViewModel:
    def __init__(self):
        pass

    def render(self):
        # Default
        drawSign(screen, "Custom - ViewModel.render(self): function.", [50,50], 25)