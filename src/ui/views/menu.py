from ...config.screen import screen
from ...graphics import drawText
from ..models.viewModel import ViewModel

from ..elements.button import CreateButton

class CreateMenu( ViewModel ):
    def __init__(self):
        self.startButton = CreateButton()
        pass 

    def render(self):
        self.startButton.draw()
        drawText.drawSign(screen, 'MAIN')