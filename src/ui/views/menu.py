from ...config.screen import screen
from ...utils import writeUtils
from ..models.viewModel import ViewModel

class CreateMenu( ViewModel ):
    def __init__(self):
        pass 

    def render(self):
        writeUtils.drawSign(screen, 'MAIN')