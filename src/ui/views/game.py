from ...core.game_manager.main_game import MainGame
from ..models.viewModel import ViewModel

class CreateGame(MainGame, ViewModel):
    def __init__(self):
        super().__init__()

        