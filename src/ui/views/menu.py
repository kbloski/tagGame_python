from ...config.screen import screen
from ...graphics import drawText
from ..models.viewModel import ViewModel

class CreateMenu( ViewModel ):
    def __init__(self):
        pass 

    def render(self):
        drawText.drawSign(screen, 'MAIN')