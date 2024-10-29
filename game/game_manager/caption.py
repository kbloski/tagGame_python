import pygame # type: ignore

class ModuleGameCaptions:
    CAPTIONS = {}
    def addCaption(self, name = 'caption-name', surface = pygame.surface ):
        self.CAPTIONS[name] = surface