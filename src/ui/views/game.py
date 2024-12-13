from ...core.game_manager.index import MainGame
from ..models.viewModel import ViewModel

class CreateGame(MainGame, ViewModel):
    def __init__(self):
        super().__init__()

        