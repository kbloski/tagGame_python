from src.config.screen import screen
from src.utils import writeUtils
from src.ui.models.viewModel import ViewModel

class CreateMenu( ViewModel ):
    def __init__(self):
        pass 

    def render(self):
        writeUtils.drawSign(screen, 'MAIN')