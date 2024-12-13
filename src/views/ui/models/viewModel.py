import pygame # type: ignore
from ....config.screen import screen
from ....config.screen import screen
from ....utils.writeUtils import drawSign

class ViewModel:
    def __init__(self):
        pass

    def render(self):
        drawSign(screen, "Custom - ViewModel.render(self): function.", [50,50], 25)