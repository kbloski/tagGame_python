from ..ui.models.viewModel import ViewModel
from ..game.game_manager.main_game import MainGame

class CreateGame(MainGame, ViewModel):
    def __init__(self):
        super().__init__()

        