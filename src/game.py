import pygame
import src.characters.player as player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.players = [
            player.Player(self.screen)
        ]
        self.tree = pygame.image.load('./tree.png').convert_alpha()
        for p in range(1):
            self.players.append(player.Player(self.screen) )

    def run(self):
        for p in self.players:
            p.run()


